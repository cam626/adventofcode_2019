import sys	

def add(program, loc1, loc2, dest):
	total = int(program[loc1]) + int(program[loc2])
	program[dest] = total

def mult(program, loc1, loc2, dest):
	total = int(program[loc1]) * int(program[loc2])
	program[dest] = total

def intcode_program(program):
	for i in range(0, len(program), 4):
		if int(program[i]) == 99:
			break
		
		if int(program[i]) == 1:
			loc1 = int(program[i + 1])
			loc2 = int(program[i + 2])
			dest = int(program[i + 3])
			add(program, loc1, loc2, dest)
		elif int(program[i]) == 2:
			loc1 = int(program[i + 1])
			loc2 = int(program[i + 2])
			dest = int(program[i + 3])
			mult(program, loc1, loc2, dest)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_3.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	initial_program = f.readlines()[0].strip("\n").split(",")
	
	for noun in range(100):
		for verb in range(100):
			program = initial_program[:]
			program[1] = noun
			program[2] = verb

			intcode_program(program)

			if program[0] == 19690720:
				print(noun, verb)
				print(100*noun + verb)
				break