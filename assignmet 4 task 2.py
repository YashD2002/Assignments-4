user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

additional_input = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

with open("output.txt", "r") as file:
    content = file.read()
    print("\nFinal content of the file:")
    print(content)
