import sys

def flattenEnd(number, index):
	for i in range(index, len(number)):
		number[i] = number[i-1]

def nextNonDecreasing(number):
	for i in range(1, len(number)):
		if number[i] < number[i-1]:
			flattenEnd(number, i)

	return number

def containsDouble(number):
	if number[0] == number[1] and number[1] != number[2]:
		return True

	if number[-1] == number[-2] and number[-2] != number[-3]:
		return True

	for i in range(2, len(number)-1):
		if number[i] == number[i-1] and number[i] != number[i-2] and number[i] != number[i+1]:
			return True

	return False

def lessThanEqual(number1, number2):
	temp1 = int("".join(number1))
	temp2 = int("".join(number2))

	return temp1 <= temp2

def intToNumber(integer):
	return list(str(integer))

def increment(number):
	return intToNumber(int("".join(number))+1)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 problem_7.py [filename]")
		exit(1)

	filename = sys.argv[1]
	f = open(filename, "r")

	low, high = f.read().strip("\n").split("-")
	low = list(low)
	high = list(high)

	count = 0
	number = nextNonDecreasing(low)
	while lessThanEqual(number, high):
		if containsDouble(number):
			count += 1

		number = nextNonDecreasing(increment(number))

	print(count)
