import re

# Get the file paths from the user
input_file_path = input("Enter the path to the input file: ")
output_file_path = input("Enter the path to the output file: ")

# Read the input file content
with open(input_file_path, "r") as file:
    file_content = file.read()

# Get the person ID from the user
person_id = input("Enter the person ID: ")

# Create a regular expression pattern to match the person ID and the corresponding row
pattern = r"\b" + person_id + r"\b\s+([\d\s/]+)"

# Use the findall() function to extract the matching data
matches = re.findall(pattern, file_content)

# Check if any matches were found
if matches:
    # Create a string to store the extracted data
    extracted_data = ""
    for match in matches:
        extracted_data += match + "\n"

    # Save the extracted data to the output file
    with open(output_file_path, "w") as output_file:
        output_file.write(extracted_data)

    print("Data for person ID", person_id,
          "has been extracted and saved to", output_file_path)
else:
    print("No data found for person ID", person_id)
