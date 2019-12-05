"""
Reads an input file containing a list of numbers separated by commas.
There are three types of instructions:
1 - Add the numbers in the next two indexes of the list,
    and store it in the third index. Ex: [1, 0, 3, 1] => l[1] = l[0] + l[3] => [1, 3, 3, 1]
2 - Multiply the numbers in the next two indexes of the list,
    and store it in the third index. Ex: [2, 0, 3, 1] => l[1] = l[0] * l[3] => [2, 2, 3, 1]
99 - Program ends immediately
Prints the list after the program ends.
"""
import sys

with open("code.txt", "r") as fin:
    input_code = fin.read().split(",")
    input_code = [int(x) for x in input_code]

print(input_code)

def operate(opcode, index_1, index_2, output_index, input_list):
    assert 0 <= index_1 < len(input_list)
    assert 0 <= index_2 < len(input_list)
    assert 0 <= output_index < len(input_list)
    assert opcode in [1, 2]

    if opcode == 1:
        input_list[output_index] = input_list[index_1] + input_list[index_2]
    elif opcode == 2:
        input_list[output_index] = input_list[index_1] * input_list[index_2]


def run_program(memory):
    for instruction_pointer in range(0, len(memory), 4):
        opcode = memory[instruction_pointer]
        if opcode == 99:
            break

        operate(
            opcode,
            memory[instruction_pointer + 1],
            memory[instruction_pointer + 2],
            memory[instruction_pointer + 3],
            memory
        )

    # print(memory)
found = False

for noun in range(100):
    for verb in range(100):
        new_memory = [x for x in input_code]
        new_memory[1] = noun
        new_memory[2] = verb
        run_program(new_memory)
        if new_memory[0] == 19690720:
            print("Noun: %s, Verb: %s, answer: %s" % (
                noun, verb, 100 * noun + verb))
            sys.exit(0)
