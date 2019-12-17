import sys

def min_fuel_for_module(weight):
    return (weight // 3) - 2

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 problem_1.py [input_file]")
        exit(1)

    filename = sys.argv[1]
    f = open(filename, "r")
    weights = f.readlines()
    
    total_requirement = 0
    for weight in weights:
        weight = int(weight)
        total_requirement += min_fuel_for_module(weight)

    print(total_requirement)