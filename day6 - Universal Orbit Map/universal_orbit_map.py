"""
Reads the universal orbit map data and counts the number of direct and indirect
orbits.
aaa)bbb means that bbb directly orbits aaa
bbb)ccc means ccc directly orbits bbb, but indirectly orbits aaa
So, orbit relationships have a transitive property.
COM does not orbit anything.
Consider this as a list of edges, we will do a BFS from COM, and add 1 at each
level to keep track of indirect orbital relationship.
"""

import sys


def read_input(input_file="map_data.txt"):
    with open(input_file, "r") as fin:
        edges = fin.readlines()
        # This dict stores the relation 'key' orbits 'value'
        orbits = {edge.strip().split(')')[1]: edge.strip().split(')')[0]
                  for edge in edges}
        # This dict will store the relation 'key' is orbited by all elements
        # in the value list
        orbited_by = {}
        for key, value in orbits.items():
            x = orbited_by.setdefault(value, [])
            x.append(key)

        return orbits, orbited_by


def get_num_orbits(orbited_by):
    """
    Does a straightforward BFS keeping track of heights to count the
    number of direct and indirect orbits
    :param orbited_by: Map maintaining the relation 'key' is orbited by all
                       elements in 'value' (list)
    :return: The total number of direct and indirect orbits
    """
    num_orbits = 0
    queue = [("COM", 0)]

    while len(queue) != 0:
        planet, height = queue.pop(0)
        for orbiter in orbited_by.get(planet, []):
            queue.append((orbiter, height + 1))
            num_orbits += height + 1

    return num_orbits


def get_num_orbital_transfers(source, destination, orbits):
    """
    Find the lowest common ancestor of the source and destination
    by following the links until COM for each of them and storing the distance.
    Then add the distances from source and destination to the lowest common
    ancestor to get the distance from source to destination
    :param source: string type to represent "YOU"
    :param destination: string type to represent "SAN"
    :param orbits: Map maintaining the relation 'key' orbits 'value'
    :return: Distance from source to destination (number of orbital transfers)
    """
    distance_to_source = {orbits[source]: 0}
    point = orbits[source]
    while point != "COM":
        distance_to_source[orbits[point]] = distance_to_source[point] + 1
        point = orbits[point]

    distance_to_destination = {orbits[destination]: 0}
    point = orbits[destination]
    while point not in distance_to_source.keys():
        distance_to_destination[orbits[point]] = \
            distance_to_destination[point] + 1
        point = orbits[point]

    orbital_transfers = distance_to_source[point] + max(
        distance_to_destination.values())
    return orbital_transfers


def main():
    orbits, orbited_by = read_input()
    print(get_num_orbits(orbited_by))
    print(get_num_orbital_transfers("YOU", "SAN", orbits))
    return 0


sys.exit(main())
