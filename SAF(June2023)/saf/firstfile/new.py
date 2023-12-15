def fetch_data_by_id(file_path, target_id):
    data_blocks = []
    current_block = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if line.strip():  # Check if the line is not empty or blank
                current_block.append(line.strip())
            elif current_block:  # Check if current block has data
                data_blocks.append(current_block)
                current_block = []

    # Iterate through each data block and check if it matches the target ID
    for block in data_blocks:
        first_line = block[0]
        if target_id in first_line:
            return block

    return None  # Return None if the target ID is not found


# Usage example
file_path = 'C:\\Python Codes\\flat file\\upadated\\test.txt'
target_id = "400136"

result = fetch_data_by_id(file_path, target_id)
if result:
    print("Data Found:")
    for line in result:
        print(line)
else:
    print("ID not found in the file.")
