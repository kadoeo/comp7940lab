def main():
	print("Hello World")
	x = 52633
	factors = []
	for i in range(x+1):
		if i > 0:
			if x % i  == 0:
				factors.append(i)
	print(factors)

def print_factor(x):
	factors = []
	for i in range(x+1):
		if i > 0:
			if x % i == 0:
				factors.append(i)
	print(factors)

def print_all_factor(l):
	for x in l:
		print_factor(x)


if __name__ == '__main__':
	main()
	l = [52633, 8137, 1024, 999]
	print_all_factor(l)
