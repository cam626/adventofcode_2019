import sys

def manhattanDistance(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def encodePosition(position):
	return position[0] * 100000 + position[1]

def decodePosition(encodedPosition):
	return [encodedPosition // 100000, encodedPosition % 100000]

def getWireLocations(wire):
	wire_position = [0, 0]

	wire_locations = set()
	for move in wire:
		direction = move[0]
		distance = int(move[1:])

		old_position = wire_position[:]

		if direction == "U":
			wire_position[1] += distance
			new_positions = set([encodePosition([wire_position[0], i]) for i in range(old_position[1], wire_position[1]+1)])
			wire_locations = wire_locations.union(new_positions)
		elif direction == "D":
			wire_position[1] -= distance
			new_positions = set([encodePosition([wire_position[0], i]) for i in range(old_position[1], wire_position[1]-1, -1)])
			wire_locations = wire_locations.union(new_positions)
		elif direction == "L":
			wire_position[0] -= distance
			new_positions = set([encodePosition([i, wire_position[1]]) for i in range(old_position[0], wire_position[0]-1, -1)])
			wire_locations = wire_locations.union(new_positions)
		elif direction == "R":
			wire_position[0] += distance
			new_positions = set([encodePosition([i, wire_position[1]]) for i in range(old_position[0], wire_position[0]+1)])
			wire_locations = wire_locations.union(new_positions)

	return wire_locations

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_5.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	wire1, wire2 = f.readlines()

	wire1 = wire1.strip("\n").split(",")
	wire2 = wire2.strip("\n").split(",")
	
	wire1_locations = getWireLocations(wire1)
	wire2_locations = getWireLocations(wire2)

	intersections = wire1_locations.intersection(wire2_locations)
	
	min_dist = float("inf")
	closest_intersect = None
	for intersect in intersections:
		new_dist = manhattanDistance(decodePosition(intersect), [0, 0])
		if new_dist < min_dist and new_dist != 0:
			min_dist = new_dist
			closest_intersect = intersect

	print(decodePosition(closest_intersect))
	print(min_dist)