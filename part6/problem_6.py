import sys

def line_intersection(line1, line2):
	'''
		Determine if 2 lines intersect.

		Assumes lines only move horizontally or vertically.

		Line:
		([x1, y1], [x2, y2])
	'''
	if (line1[0][0] == line1[1][0] and line2[0][0] == line2[1][0]) \
			or (line1[0][1] == line1[1][1] and line2[0][1] == line2[1][1]):
		# Lines are parallel
		return False

	vertical = (line1 if line1[0][0] == line1[1][0] else line2)
	horizontal = (line1 if vertical is not line1 else line2)

	if horizontal[0][1] < min(vertical[0][1], vertical[1][1]) \
			or horizontal[0][1] > max(vertical[0][1], vertical[1][1]):
		return False

	if max(horizontal[0][0], horizontal[1][0]) < vertical[0][0] \
			or min(horizontal[0][0], horizontal[1][0]) > vertical[0][0]:
		return False

	return True

def construct_line(start_point, direction, distance):
	start_x = start_point[0]
	start_y = start_point[1]

	if direction == "U":
		end_point = [start_x, start_y + distance]
	elif direction == "D":
		end_point = [start_x, start_y - distance]
	elif direction == "R":
		end_point = [start_x + distance, start_y]
	elif direction == "L":
		end_point = [start_x - distance, start_y]

	return [start_point[:], end_point]

def wire_of_lines(wire):
	'''
		Turn a list of directional strings into a list of lines.
	'''
	new_wire = []
	position = [0, 0]
	for move in wire:
		direction = move[0]
		distance = int(move[1:])

		new_line = construct_line(position, direction, distance)

		position = new_line[1][:]

		new_wire.append(new_line)

	return new_wire

def all_intersections(wire1, wire2):
	intersections = []
	for i in range(1, len(wire1)):
		for j in range(1, len(wire2)):
			if line_intersection(wire1[i], wire2[j]):
				intersections.append([i, j])

	return intersections

def line_length(line):
	return abs(line[0][0] - line[1][0]) + abs(line[0][1] - line[1][1])

def moves_before_intersect(wire, intersect_index):
	moves = 0
	for i in range(intersect_index):
		moves += line_length(wire[i])

	return moves

def moves_during_intersect(line1, line2):
	vertical = (line1 if line1[0][0] == line1[1][0] else line2)
	horizontal = (line1 if vertical is not line1 else line2)

	intersect_point = [vertical[0][0], horizontal[0][1]]

	return line_length([vertical[0], intersect_point]) + line_length([horizontal[0], intersect_point])


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_6.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")
	wire1, wire2 = f.readlines()

	wire1 = wire1.strip("\n").split(",")
	wire2 = wire2.strip("\n").split(",")

	wire1 = wire_of_lines(wire1)
	wire2 = wire_of_lines(wire2)

	intersections = all_intersections(wire1, wire2)
	
	lowest_moves_for_intersection = float("inf")
	for wire1_intersect_index, wire2_intersect_index in intersections:
		wire1_prior = moves_before_intersect(wire1, wire1_intersect_index)
		wire2_prior = moves_before_intersect(wire2, wire2_intersect_index)

		additional_moves = moves_during_intersect(wire1[wire1_intersect_index], wire2[wire2_intersect_index])

		total_moves_for_intersection = wire1_prior + wire2_prior + additional_moves

		if total_moves_for_intersection < lowest_moves_for_intersection:
			lowest_moves_for_intersection = total_moves_for_intersection

	print(lowest_moves_for_intersection)
