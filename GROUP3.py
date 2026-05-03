FILE_NAME = "diary.txt"

# A - Initialize (x and w)
def initialize():
    file = open(FILE_NAME, "w")
    text = input("Enter first diary entry: ")
    file.write(text + "\n")
    file.close()
    print("Diary initialized.\n")
def append():
    file = open(FILE_NAME, "a")
    text = input("Enter new entry: ")
    file.write(text + "\n")
    file.close()
    print("Entry added.\n")
