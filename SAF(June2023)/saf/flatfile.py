import re

# Specify the file paths
input_file_path = "C:\\Python Codes\\flat file\\test.txt"
output_file_path = "C:\\Python Codes\\flat file\\test1.txt"

# Get the person ID from the user
person_id = input("Enter the person ID: ")

# Create a regular expression pattern to match the person ID and the corresponding row
pattern = r"\b" + person_id + r"\b\s+([\d\s/]+)"

# Read the input file and search for matches
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        matches = re.findall(pattern, line)
        if matches:
            # Write the matching data to the output file
            output_file.write(matches[0] + "\n")
            break

# If no matches were found
if not matches:
    print("No data found for person ID:", person_id)
else:
    print("Data for person ID", person_id,
          "has been extracted to", output_file_path)
