import sys

def math(row, return_val, i):
	if return_val == 1:
		return 3 if i == 1 else (i + 2) + math(0, 1, i - 1)
	if return_val == 2:
		if row > 3:
			return math(row, 2, i + 1) if row > math(0, 1, i) else i
		return 1
	if return_val == 3:
		return i + 4 if i % 2 == 0 else i + 3
	if row > 1:
		if math(row, 2, 1) == math(row - 1, 2, 1):
			return 2 + math(row - 1, 4, math(0, 3, math(row - 1, 2, 1)))
		else:
			return math(0, 3, math(row, 2, 1)) + math(row - 1, 4, math(0, 3, math(row - 1, 2, 1)))
	return 3

def print_row(max_chars, chars, door):
	i = 0
	while i < max_chars:
		if i < (max_chars // 2) - (chars // 2) or i > (max_chars // 2) + (chars // 2):
			print(" ", end="")
		elif i == (max_chars // 2) - (chars // 2) or i == (max_chars // 2) + (chars // 2):
			print("/", end="") if i == (max_chars // 2) - (chars // 2) else print("\\", end="")
		elif max_chars - chars <= door * 2 - 1 and (i >= (max_chars // 2) - (door // 2) and i <= (max_chars // 2) + (door // 2)):
			if door > 3 and i == (max_chars // 2) + (door // 2) - 1 and max_chars - chars == door - 1:
				print("$", end="")
			else:
				print("|", end="")
		else:
			print("*", end="")
		i += 1
	print()

def pyramid(size):
	i = 1
	max_row = math(0, 1, size)
	max_chars = math(max_row, 4, 0)
	if size > 0:
		size = size - 1 if size % 2 == 0 else size
		while max_row > 0:
			print_row(max_chars, math(i, 4, 0), size)
			i += 1
			max_row -= 1

if __name__ == "__main__":
	for arg in sys.argv[1:]:
		try:
			size = int(arg)
			if size > 0:
				print(f"Size {size}:")
				pyramid(size)
			else:
				print(f"Invalid argument")
		except ValueError:
			print(f"Ivalid argument")
