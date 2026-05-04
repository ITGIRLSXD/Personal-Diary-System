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
def update():
    try:
        file = open(FILE_NAME, "r")
        lines = file.readlines()
        file.close()

        for i in range(len(lines)):
            print(f"{i+1}. {lines[i].strip()}")

        num = int(input("Choose entry number to update: "))
        new = input("New text: ")
        lines[num-1] = new + "\n"

        file = open(FILE_NAME, "w")
        file.writelines(lines)
        file.close()
        print("Updated.\n")
    except:
        print("Error.\n")

