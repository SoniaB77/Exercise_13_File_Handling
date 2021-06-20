#Exercise 13 – File Handling

Objectives:

* To read and write to files

Question 1:

1. Create a new PyCharm project: Exercise13.
2. Create a new python file in the project called write_file.py
3. Write a line of code to create a file handle to open and append to a file called pelican.txt
4. Append the following line to the file using the write method of the file handle:
“A wonderful bird is the pelican,”
5. Append the following second line using the write method:
“His bill holds more than his belican.”
6. Create a list that contains the following lines: lines = [

`“He can take in his beak,\n”, “Enough food for a week,\n”, “But I’m damned if I see how the helican.\n”]`

7. Append this list to the file using the writelines method.
Why are the “\n” required?
8. Run the script and confirm a new file called pelican.txt was created and that it contains the limerick as expected.

Question 2:

1. Create a new python file in the project called read_file.py
2. Use the open and read methods to slurp the entire contents of your pelican.txt file
3. Display the type of the returned data and print the contents of the returned data.
4. What data type is the output?
5. Now, write some code that will read the pelican.txt file into a list and then output the number of items within the list.
6. Now use a loop to iterate over and print the contents of the file. Be sure not to include any blank lines in the output.