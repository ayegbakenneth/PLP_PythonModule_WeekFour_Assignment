# •	File Read & Write Challenge 🖋️:
#  Create a program that reads a file and writes a modified version to a new file.
# Reading from file

with open("example.txt", "r") as file:
    data = file.read()
    print(data)
# Writing to files
with open("output.txt", "w") as file:
    data = file.write("He is working hard to be among the best in his field.")
    print(data)
# •	Error Handling Lab 🧪: 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    collectData = input("Enter a file name ")
    if collectData == "example.txt" or "output.txt":
        with open(collectData, "r") as file:
            readFile = file.read()
            print(readFile)
except FileNotFoundError:
    print("Invalid file name")