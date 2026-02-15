def main():
    name = input("Enter name of the file: ")
    file_name = name + ".txt"
    file = open(file_name, "w")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file.write(new_line + "\n")
    file.close()

if __name__ == "__main__":
    main()
