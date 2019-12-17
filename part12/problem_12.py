import sys

def constructTree(direct_orbits):
	tree = {}
	for orbit in direct_orbits:
		orbitted = orbit[0]
		orbitter = orbit[1]

		if orbitted not in tree:
			tree[orbitted] = []

		if orbitter not in tree:
			tree[orbitter] = []

		tree[orbitted].append(orbitter)
		tree[orbitter].append(orbitted)

	return tree

def DFS(tree, start, end):
	hops = 0

	distances = {
		start: 0
	}
	queue = [start]
	while len(queue) > 0:
		node = queue.pop(-1)
		
		if node == end:
			return distances[node]

		children = tree.get(node, [])
		for child in children:
			if child not in distances:
				queue.append(child)
				distances[child] = distances[node] + 1

	return None


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

	start = tree["YOU"][0]
	end = tree["SAN"][0]

	num_hops = DFS(tree, start, end)
	print(num_hops)