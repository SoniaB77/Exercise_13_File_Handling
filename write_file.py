infile=open('pelican.txt', 'a+')

infile.write("A wonderful bird is the pelican,")
infile.write("\nHis bill holds more than his belican.")

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
#creating a list to store the lines.

infile.writelines(lines)

infile.close()

