# read a particular line from a file. User provides both the line
# number and the file name

file_str = input("Open what file:")
find_line_str = input("Which line (integer):")

try:
	input_file = open(file_str)
	find_line_int = int(find_line_str)
	line_count_int = 1
	for line_str in input_file:
		if line_count_int == find_line_int:
			print("Line {} of file {} is {}".format(find_line_int, file_str,line_str))
			break
		line_count_int += 1
	else:
		print("Line {} of file{} not found".format(find_line_int, file_str))
	input_file.close()
except:
	pass
