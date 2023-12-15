def extract_data_block(file_path, id):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_block = []
    for line in lines:
        if line.strip().startswith(id):
            if current_block:
                return current_block
            current_block = []
        current_block.append(line.strip())

    if current_block:
        return current_block

    return None


# Get user input
file_path = input("Enter the file path: ")
id = input("Enter the ID to extract: ")

# Extract the data block
block = extract_data_block(file_path, id)

# Display the extracted data block
if block is not None:
    print(f"Data Block for ID {id}:")
    for line in block:
        print(line)
else:
    print(f"No data block found for ID {id}.")
