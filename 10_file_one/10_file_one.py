def read_only_file(filename):
    try:
        with open(filename, 'r') as fileptr:
            return fileptr.readlines()
    except FileNotFoundError:
        return "File not found"

def write_only_file(filename, content):
    try:
        with open(filename, 'w') as fileptr:
            fileptr.write(content)
    except Exception as e:
        return e
    return None

def append_only_file(filename, content):
    try:
        with open(filename, 'a') as fileptr:
            fileptr.write(content)
    except Exception as e:
        return e
    return None

def read_write_rplus_file(filename):
    try:
        with open(filename, 'r+') as fileptr:
            print(fileptr.read())
            fileptr.write("Hello World")
    except FileNotFoundError:
        print("File not found")

def write_read_rplus_file(filename):
    try:
        with open(filename, 'r+') as fileptr:
            fileptr.write("Hello World")
            print(fileptr.read())
    except FileNotFoundError:
        print("File not found")

def main():
    print(read_only_file("file_r.txt"))
    write_only_file("file_w.txt", "Write first words\n")
    append_only_file("file_w.txt", "Write second words")
    read_write_rplus_file("file_r.txt")
    write_read_rplus_file("file_r.txt")
    print("Program finished")

if __name__ == '__main__':
    main()