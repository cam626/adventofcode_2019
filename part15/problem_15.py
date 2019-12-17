import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_15.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	width = 25
	height = 6

	block = f.read().strip("\n")
	layer_size = width * height
	num_layers = len(block) // layer_size
	layers = []

	fewest_zeros = layer_size + 1
	fewest_index = 0
	for layer_index in range(num_layers):
		layers.append(block[layer_index*layer_size:(layer_index+1)*layer_size])
		num_zeros = layers[layer_index].count('0')
		if num_zeros < fewest_zeros:
			fewest_zeros = num_zeros
			fewest_index = layer_index

	print(layers[fewest_index].count('1') * layers[fewest_index].count('2'))