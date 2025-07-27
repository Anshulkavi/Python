try:
    with open('sample.txt', 'r') as file:
        reading_file = file.read()
        print("Reading file content:")
        print(reading_file)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
