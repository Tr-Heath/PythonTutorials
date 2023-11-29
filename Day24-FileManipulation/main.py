#Some common modes, "a" is append, "w" for standard write (this replaces the contents of the file)
#Standard write mode will also create the file for you if it does not already exist
with open("testFile.txt", mode= "a") as file: 
    file.write("Additional text.")

with open("testFile.txt") as file:
    contents = file.read()
    print(contents)