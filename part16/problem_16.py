import sys

def layersFromBlock(block):
	layer_size = width * height
	num_layers = len(block) // layer_size
	layers = []

	for layer_index in range(num_layers):
		layers.append(block[layer_index*layer_size:(layer_index+1)*layer_size])

	return layers

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_16.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	width = 25
	height = 6

	block = f.read().strip("\n")
	layers = layersFromBlock(block)

	final = [[0]*width]*height

	for i in range(height):
		for j in range(width):
			for layer_index in range(len(layers)):
				if layers[layer_index][i*width + j] == '2':
					continue

				final[i][j] = layers[layer_index][i*width + j]
				break

		final[i] = "".join(final[i])

	for row in final:
		for char in row:
			if char == "0":
				print(" ", end="")
			else:
				print("#", end="")

		print()
