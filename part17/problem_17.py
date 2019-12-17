import sys	

class IntcodeComputer():
	def __init__(self, program, inputs):
		self.program = program
		self.relative_base = 0
		self.outputs = []
		self.inputs = inputs
		self.index = 0

	def getValFromLoc(self, loc):
		return int(self.program[loc])

	def getLocWithMode(self, offset, mode):
		if mode == 0:
			return int(program[self.index + offset])
		elif mode == 1:
			return self.index + offset
		elif mode == 2:
			return self.relative_base + int(program[self.index + offset])

		return -1

	def updateRelativeBase(self):
		opcode = int(self.program[self.index])

		mode = (opcode % 1000) // 100

		loc = self.getLocWithMode(1, mode)
		val = self.getValFromLoc(loc)

		self.relative_base += val

		self.index += 2

	def add(self):
		opcode = int(self.program[self.index])

		mode1 = (opcode % 1000) // 100
		mode2 = (opcode % 10000) // 1000
		dest_mode = (opcode % 100000) // 10000

		loc1 = self.getLocWithMode(1, mode1)
		loc2 = self.getLocWithMode(2, mode2)
		dest = self.getLocWithMode(3, dest_mode)

		val1 = self.getValFromLoc(loc1)
		val2 = self.getValFromLoc(loc2)

		total = val1 + val2
		self.program[dest] = total

		self.index += 4

	def mult(self):
		opcode = int(self.program[self.index])

		mode1 = (opcode % 1000) // 100
		mode2 = (opcode % 10000) // 1000
		dest_mode = (opcode % 100000) // 10000

		loc1 = self.getLocWithMode(1, mode1)
		loc2 = self.getLocWithMode(2, mode2)
		dest = self.getLocWithMode(3, dest_mode)

		val1 = self.getValFromLoc(loc1)
		val2 = self.getValFromLoc(loc2)

		total = val1 * val2
		self.program[dest] = total

		self.index += 4

	def getInput(self):
		input_value = self.inputs.pop(0)

		opcode = int(self.program[self.index])
		dest_mode = (opcode % 1000) // 100

		dest = self.getLocWithMode(1, dest_mode)
		self.program[dest] = input_value

		self.index += 2

	def writeOutput(self):
		opcode = int(self.program[self.index])

		mode = (opcode % 1000) // 100

		loc = self.getLocWithMode(1, mode)
		val = self.getValFromLoc(loc)

		self.outputs.append(val)

		self.index += 2

	def jumpIfTrue(self):
		opcode = int(self.program[self.index])

		mode = (opcode % 1000) // 100
		dest_mode = (opcode % 10000) // 1000

		loc = self.getLocWithMode(1, mode)
		dest = self.getLocWithMode(2, dest_mode)

		val = self.getValFromLoc(loc)

		if val != 0:
			self.index = dest
		else:
			self.index += 3

	def jumpIfFalse(self):
		opcode = int(self.program[self.index])

		mode = (opcode % 1000) // 100
		dest_mode = (opcode % 10000) // 1000

		loc = self.getLocWithMode(1, mode)
		dest = self.getLocWithMode(2, dest_mode)

		val = self.getValFromLoc(loc)

		if val == 0:
			self.index = dest
		else:
			self.index += 3

	def lessThan(self):
		opcode = int(self.program[self.index])

		mode1 = (opcode % 1000) // 100
		mode2 = (opcode % 10000) // 1000
		dest_mode = (opcode % 100000) // 10000

		loc1 = self.getLocWithMode(1, mode1)
		loc2 = self.getLocWithMode(2, mode2)

		dest = self.getLocWithMode(3, dest_mode)

		val1 = self.getValFromLoc(loc1)
		val2 = self.getValFromLoc(loc2)
		
		total = 0
		if val1 < val2:
			total = 1

		self.program[dest] = total

		self.index += 4

	def equals(self):
		opcode = int(self.program[self.index])

		mode1 = (opcode % 1000) // 100
		mode2 = (opcode % 10000) // 1000
		dest_mode = (opcode % 100000) // 10000

		loc1 = self.getLocWithMode(1, mode1)
		loc2 = self.getLocWithMode(2, mode2)

		dest = self.getLocWithMode(3, dest_mode)

		val1 = self.getValFromLoc(loc1)
		val2 = self.getValFromLoc(loc2)

		total = 0
		if val1 == val2:
			total = 1

		self.program[dest] = total

		self.index += 4

	def run(self):
		while self.index < len(self.program):
			if int(self.program[self.index]) == 99:
				return -1
			
			opcode = int(self.program[self.index]) % 100
			print(opcode)
			if opcode == 1:
				self.add()
			elif opcode == 2:
				self.mult()
			elif opcode == 3:
				self.getInput()
			elif opcode == 4:
				self.writeOutput()
				return False
			elif opcode == 5:
				self.jumpIfTrue()
			elif opcode == 6:
				self.jumpIfFalse()
			elif opcode == 7:
				self.lessThan()
			elif opcode == 8:
				self.equals()
			elif opcode == 9:
				self.updateRelativeBase()

		return True

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_17.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	memsize = 500
	memory = [0]*memsize
	program = f.readlines()[0].strip("\n").split(",")

	program.extend(memory)
	comp = IntcodeComputer(program, [1])
	
	done = False
	while not done:
		done = comp.run()

	print(comp.outputs)