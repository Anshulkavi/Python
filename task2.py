# Step 1: Write initial data to the file with a newline
data = input("Enter text to write to the file: ").strip()  

with open("output.txt", "w") as file:
    file.write(data + "\n")
    print("Data successfully written to output.txt.\n")

# Step 2: Append additional data with a newline
additional_data = input("Enter additional text to append: ").strip()

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")
    print("Data successfully appended.\n")

# Step 3: Read and display final contents
with open("output.txt", "r") as file:
    final_content = file.read()
    print("Final content of output.txt:\n" + final_content)
