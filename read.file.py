infile=open('pelican.txt', 'r')

infile_read = infile.read()
print(infile_read)

print(type(infile_read))

infile.close()

lines = []

with open('pelican.txt','r')as fileopen:
    for line in fileopen:
        lines.append(line)

print(type(lines))
print(len(lines))

with open('pelican.txt','r')as fileopen:
    for line in fileopen:
        print(line, end='')


# line_number = 0
# while line_number<5:
#
#     print(lines[line_number], end='')
#     line_number = line_number + 1
#
# #when using 'with' you don't have to close off file.
