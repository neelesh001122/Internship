from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/extract', methods=['POST'])
def extract_data():
    input_file = request.files['input_file']
    output_file = request.files['output_file']

    # Save the uploaded files to a temporary location
    input_file.save('temp/input.txt')
    output_file.save('temp/output.txt')

    # Read the file content
    with open('temp/input.txt', 'r') as file:
        file_content = file.read()

    # Get the person ID from the user
    person_id = request.form['person_id']

    # Create a regular expression pattern to match the entire block of data containing the ID
    pattern = r"\b" + person_id + r"\b\s+([\s\S]+?)(?=\n\S|\Z)"
    # Use the findall() function to extract all matching blocks of data
    matching_data = re.findall(pattern, file_content)

    # Check if any data blocks were found
    if matching_data:
        # Save the extracted data to the output file
        with open('temp/output.txt', 'w') as output:
            for data in matching_data:
                output.write(data)
                output.write('\n\n')

        return 'Found'
    else:
        return 'Not found'


if __name__ == '__main__':
    app.run()
