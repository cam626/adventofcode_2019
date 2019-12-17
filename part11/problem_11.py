import sys

def constructTree(direct_orbits):
	tree = {}
	for orbit in direct_orbits:
		orbitted = orbit[0]
		orbitter = orbit[1]

		if orbitted not in tree:
			tree[orbitted] = []

		tree[orbitted].append(orbitter)

	return tree

def constructDistanceTree(tree):
	distance_tree = {
		"COM": 0
	}

	queue = ["COM"]

	while len(queue) > 0:
		node = queue.pop()
		
		children = tree.get(node, [])
		for child in children:
			distance_tree[child] = distance_tree[node] + 1
			queue.append(child)

	return distance_tree

def sumDistanceTree(distance_tree):
	total = 0
	for key, value in distance_tree.items():
		total += value

	return total

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_11.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	direct_orbits = f.readlines()
	for orbit_index in range(len(direct_orbits)):
		direct_orbits[orbit_index] = direct_orbits[orbit_index].strip("\n").split(")")

	tree = constructTree(direct_orbits)
	distance_tree = constructDistanceTree(tree)
	num_orbits = sumDistanceTree(distance_tree)

	print(num_orbits)