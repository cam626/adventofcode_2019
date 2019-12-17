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

def getInput(program, index):
	total = int(input("Enter a number: "))

	dest = int(program[index + 1])
	program[dest] = total

def writeOutput(program, index):
	opcode = int(program[index])

	mode = (opcode % 1000) // 100

	val = getValueByMode(program, index + 1, mode)

	print("Output:", val)

def intcode_program(program):
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
			getInput(program, i)
			i += 2
		elif opcode == 4:
			writeOutput(program, i)
			i += 2

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_3.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	program = f.readlines()[0].strip("\n").split(",")
	
	intcode_program(program)

	print(program)