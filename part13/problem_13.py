import sys	

def getValueByMode(program, index, mode):
	if mode == 0:
		return int(program[int(program[index])])
	
	return int(program[index])

def add(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val1 = getValueByMode(program, index + 1, mode1)
	val2 = getValueByMode(program, index + 2, mode2)

	total = val1 + val2

	dest = int(program[index + 3])
	program[dest] = total

def mult(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val1 = getValueByMode(program, index + 1, mode1)
	val2 = getValueByMode(program, index + 2, mode2)

	total = val1 * val2

	dest = int(program[index + 3])
	program[dest] = total

def getInput(program, index, inputs):
	total = inputs.pop(0)

	dest = int(program[index + 1])
	program[dest] = total

def writeOutput(program, index, outputs):
	opcode = int(program[index])

	mode = (opcode % 1000) // 100

	val = getValueByMode(program, index + 1, mode)

	outputs.append(val)

def jumpIfTrue(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val = getValueByMode(program, index + 1, mode1)
	dest = getValueByMode(program, index + 2, mode2)

	if val != 0:
		return dest

	return index

def jumpIfFalse(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val = getValueByMode(program, index + 1, mode1)
	dest = getValueByMode(program, index + 2, mode2)

	if val == 0:
		return dest

	return index

def lessThan(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val1 = getValueByMode(program, index + 1, mode1)
	val2 = getValueByMode(program, index + 2, mode2)

	dest = int(program[index + 3])
	
	total = 0
	if val1 < val2:
		total = 1

	program[dest] = total

def equals(program, index):
	opcode = int(program[index])

	mode1 = (opcode % 1000) // 100
	mode2 = (opcode % 10000) // 1000

	val1 = getValueByMode(program, index + 1, mode1)
	val2 = getValueByMode(program, index + 2, mode2)

	dest = int(program[index + 3])
	
	total = 0
	if val1 == val2:
		total = 1

	program[dest] = total

def intcode_program(program, inputs, outputs):
	i = 0
	while i < len(program):
		if int(program[i]) == 99:
			break
		
		opcode = int(program[i]) % 100
		if opcode == 1:
			add(program, i)
			i += 4
		elif opcode == 2:
			mult(program, i)
			i += 4
		elif opcode == 3:
			getInput(program, i, inputs)
			i += 2
		elif opcode == 4:
			writeOutput(program, i, outputs)
			i += 2
		elif opcode == 5:
			prev = i
			i = jumpIfTrue(program, i)

			if i == prev:
				i += 3
		elif opcode == 6:
			prev = i
			i = jumpIfFalse(program, i)

			if i == prev:
				i += 3
		elif opcode == 7:
			lessThan(program, i)
			i += 4
		elif opcode == 8:
			equals(program, i)
			i += 4
		else:
			i += 1

def runAmpSeries(program, phase_settings):
	output = 0
	for i in range(len(phase_settings)):
		temp_program = program[:]
		inputs = [phase_settings[i], output]
		outputs = []

		intcode_program(temp_program, inputs, outputs)
		output = outputs[0]

	return output

def allPermutations(l):
	if len(l) == 0 or len(l) == 1:
		return [l]

	ret = []
	for i in range(len(l)):
		first = l[i]
		remainder = l[:]
		remainder.remove(l[i])
		permute_remainder = allPermutations(remainder)
		for r in permute_remainder:
			temp = [first]
			temp.extend(r)
			ret.append(temp)

	return ret

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_13.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	program = f.readlines()[0].strip("\n").split(",")

	max_output = 0
	phase_settings_permutations = allPermutations([0, 1, 2, 3, 4])
	for phase_settings in phase_settings_permutations:
		output = runAmpSeries(program, phase_settings)
		if output > max_output:
			max_output = output

	print(max_output)