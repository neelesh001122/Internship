import re

# Get the file paths from the user
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")

# Read the input file content
with open(input_file_path, "r") as file:
    file_content = file.read()

# Get the person ID from the user
person_id = input("Enter the person ID: ")

# Create a regular expression pattern to match the person ID and the corresponding block
pattern = r"\b" + person_id + r"\b\s+([\s\S]+?)(?=\n\S|\Z)"

# Use the search() function to find the person ID and the corresponding block in the file content
match = re.search(pattern, file_content)

# Check if the person ID was found
if match:
    print("Found")
    # Extract the entire block associated with the person ID
    extracted_data = match.group(0)
    print(extracted_data)

    # Save the extracted data in the output file
    with open(output_file_path, "w") as output_file:
        output_file.write(extracted_data)
    print("Extracted data saved in:", output_file_path)
else:
    print("Not found")
