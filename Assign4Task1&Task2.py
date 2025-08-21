# Task 1: File Handling - Write,Append,Read

# step 1: Take user input and Write it to output.txt

text = input("Enter text to write to  the file: ")
with open ("output.txt","w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

# step 2 : Append additional data
append_text = input ("Enter additional text to append:")
with open("output.txt","a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt","r") as file:
    content = file.read()
    print(content)





# Task 2: Exception Handling - Reading a File

filename = input("Enter the file name:")
try:
    with open(filename, "r") as file:
        print("\nReading file content:")
        lines = file.readlines()
        for i,line in enumerate(lines,start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}'was not found.")
