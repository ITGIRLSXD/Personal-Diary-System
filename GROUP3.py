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
def read():
    try:
        file = open(FILE_NAME, "r")
        lines = file.readlines()
        print("\n--- Entries ---")
        for line in lines:
            print(line.strip())
        print("Total entries:", len(lines))
        file.close()
    except:
        print("No file found.\n")
