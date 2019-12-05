"""
Reads the provided input of the wire paths to find the closest intersecting
point of the two wires.
We first generate two lists of line segments for each wire
(horizontal and vertical). Then we find if there are any intersecting lines
between the two wires, and get the closest point to (0, 0) where they intersect.
"""


def get_wire_lines(wire_path):
    """
    Reads a wire path and returns two lists of lines (horizontal and vertical)
    :param wire_path: A list of the form <dir><num>, <dir><num>, ...
                      where <dir> can be L, R, U, D and <num> is any number
    :return: Two lists of tuples of the form (x1, y1, x2, y2) for horizontal and
             vertical lines
    """
    start_x = 0
    start_y = 0
    horizontal = []
    vertical = []

    for dir_num in wire_path:
        dir = dir_num[0]
        distance = int(dir_num[1:])
        end_x = start_x
        end_y = start_y

        if dir == 'U':
            end_y += distance
        elif dir == 'D':
            end_y -= distance
        elif dir == 'L':
            end_x -= distance
        elif dir == 'R':
            end_x += distance

        line = tuple([start_x, start_y, end_x, end_y])

        if end_x == start_x:
            # Vertical line
            vertical.append(line)
        elif end_y == start_y:
            # Horizontal line
            horizontal.append(line)

        # Update the start point for the next line segment
        start_x = end_x
        start_y = end_y

    return horizontal, vertical


def get_intersection_point(line_1, line_2):
    """
    Given two lines - this method returns the point where they intersect
    or 0, 0 if they don't intersect since central port is to be ignored.
    Since we are only working with horizontal and vertical lines we do not need
    to find the slope and intercept to calculate the intersection point.
    :param line_1: A tuple of the form x1, y1, x2, y2
    :param line_2: A tuple of the form x1, y1, x2, y2
    :return: A tuple of the form x, y
    """
    x = 0
    y = 0
    if line_1[0] == line_1[2] and line_2[0] == line_2[2]:
        # Two vertical lines won't intersect
        return tuple([x, y])

    if line_1[1] == line_1[3] and line_2[1] == line_2[3]:
        # Two horizontal lines won't intersect
        return tuple([x, y])

    if line_1[1] == line_1[3] and line_2[0] == line_2[2]:
        # Swap the two lines such that line 1 is vertical
        # and line2 is horizontal
        line_1, line_2 = line_2, line_1

    if line_1[0] == line_1[2] and line_2[1] == line_2[3]:
        # line_1 is vertical and line_2 is horizontal
        x = line_1[0]
        y = line_2[1]

        line_2_min_x = min(line_2[0], line_2[2])
        line_2_max_x = max(line_2[0], line_2[2])
        if not line_2_min_x < x < line_2_max_x:
            # No intersection
            return tuple([0, 0])

        line_1_min_y = min(line_1[1], line_1[3])
        line_1_max_y = max(line_1[1], line_1[3])

        if not line_1_min_y < y < line_1_max_y:
            # No intersection
            return tuple([0, 0])

    return tuple([x, y])


def main():
    # Read the inputs
    with open("wire_paths.txt", "r") as fin:
        wires = fin.readlines()

    wire_a = wires[0].split(',')
    wire_b = wires[1].split(',')

    central_port = tuple([0, 0])

    # Get the line segments for the two wires
    a_horizontal, a_vertical = get_wire_lines(wire_a)
    b_horizontal, b_vertical = get_wire_lines(wire_b)

    # Get the intersection points of the two wires
    intersection_points = set()

    for vert in a_vertical:
        for hor in b_horizontal:
            intersection_points.add(get_intersection_point(vert, hor))

    for vert in b_vertical:
        for hor in a_horizontal:
            intersection_points.add(get_intersection_point(vert, hor))

    # Remove the central port as that does not count as an intersection point
    intersection_points.remove(central_port)
    # print(intersection_points)

    # Print the manhattan distances of the intersection points from the central
    # port as a sorted list
    manhattan_distances = sorted([x + y for x, y in intersection_points])
    print(manhattan_distances)


if __name__ == '__main__':
    main()
