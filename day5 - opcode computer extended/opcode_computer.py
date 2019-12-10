"""
Reads an input file containing a list of numbers separated by commas.
There are three types of instructions:
1 - Add the numbers in the next two indexes of the list,
    and store it in the third index.
    Ex: [1, 0, 3, 1] => l[1] = l[0] + l[3] => [1, 3, 3, 1]
2 - Multiply the numbers in the next two indexes of the list,
    and store it in the third index.
    Ex: [2, 0, 3, 1] => l[1] = l[0] * l[3] => [2, 2, 3, 1]
3 - Takes a single integer as input and saves it to the position given by
    its only parameter. For example, the instruction 3,50 would take an input
    value and store it at address 50.
4 - Outputs the value of its only parameter. For example, the instruction 4,50
    would output the value at address 50.
99 - Program ends immediately

Also, we need to support "parameter modes" - position(0) and value(1)
Parameter modes are stored in the same value as the instruction's opcode.
The opcode is a two-digit number based only on the ones and tens digit of
the value, that is, the opcode is the rightmost two digits of the first value
in an instruction. Parameter modes are single digits, one per parameter,
read right-to-left from the opcode: the first parameter's mode is in the
hundreds digit, the second parameter's mode is in the thousands digit,
the third parameter's mode is in the ten-thousands digit, and so on.
Any missing modes are 0.

So opcode 1002 means "multiply" because of the rightmost 2 digits of the opcode
is "02".
First parameter's mode is 0 (going right to left) so, by position.
Second parameter's mode is 1, so by value.
Third parameter's mode is 0 (1002 gets converted to 01002 to account for this),
so by position again.
So, the following instruction - 1002, 4, 3, 4, 33 means multiply value in
position 4 (in this example it is 33).
with value 3, (33 * 3 = 99)
and store it in position 4, which means the memory becomes [1002, 4, 3, 4, 99]
"""

import sys

with open("code.txt", "r") as fin:
    input_code = fin.read().split(",")
    input_code = [int(x) for x in input_code]

print(input_code)

def operate(instruction, v1, v2):
    """
    Reads the instruction and parameters, and then computes the output
    """
    if instruction == 1:
        return v1 + v2

    elif instruction == 2:
        return v1 * v2


def get_value(mode, memory, pointer):
    """
    Reads the mode and the instruction pointer, and returns the value
    If mode is 1, returns the value at the pointer
    If mode is 0, returns the value referenced by the pointer
    :param mode: 0 or 1
    :param memory: Address space
    :param pointer: The location in the address space to read
    :return: Integer value
    """
    # Use value if mode is 1 and use position in memory if mode is 0
    if mode == 1:
        return memory[pointer]

    address = memory[pointer]
    return memory[address]


def run_program(memory):
    instruction_pointer = 0
    while instruction_pointer < len(memory):
        opcode = memory[instruction_pointer]
        instruction = opcode % 100

        if instruction == 99:
            break

        if instruction in [1, 2]:

            param_mode_1 = int(opcode / 100) % 10
            param_mode_2 = int(opcode / 1000) % 10
            param_mode_3 = int(opcode / 10000) % 10

            v1 = get_value(param_mode_1, memory, instruction_pointer + 1)
            v2 = get_value(param_mode_2, memory, instruction_pointer + 2)
            v3 = operate(instruction, v1, v2)

            if param_mode_3 == 0:
                address = memory[instruction_pointer + 3]
                memory[address] = v3

            instruction_pointer += 4
            continue

        if instruction == 3:
            address = memory[instruction_pointer + 1]
            memory[address] = int(input("Enter input: "))
            instruction_pointer += 2
            continue

        if instruction == 4:
            address = memory[instruction_pointer + 1]
            print(memory[address])
            instruction_pointer += 2
            continue


sys.exit(run_program(input_code))
