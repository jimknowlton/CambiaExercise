import sys, os

# open file
fobj = open(sys.argv[1], "r")

# strip out spaces
for line in fobj:
    stripped_line = line.strip()

# close file
fobj.close()

item_list = stripped_line.split(",")  # create list
item_list.sort(reverse=True)  # sort list in descending order
item_output = ",".join(item_list)

# TODO Python file write not working for some reason within Docker - below is a workaround
# create output file and write sorted list to it
os.chdir("./output")
output_command = "echo " + item_output + " > output.csv"
os.system(output_command)

# open output file and show contents
print("\nInput file contents: ")
print(stripped_line)
fobj = open("output.csv", "r")
print("\nOutput file contents: ")
for line in fobj:
    print(line)
fobj.close()
