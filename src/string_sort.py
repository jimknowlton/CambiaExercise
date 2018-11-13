
import sys


#open file
fobj = open(sys.argv[1], "r")

#strip out spaces
for line in fobj:
    stripped_line = line.strip()

#close file
fobj.close()

item_list = stripped_line.split(",") #create list
item_list.sort(reverse=True) #sort list in descending order
item_output = ",".join(item_list)

#create output file and write sorted list to it
f = open("output.csv", "w")
f.write(item_output)
f.close



