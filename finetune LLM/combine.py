import json
import os

input_directory = "manim-fine-tune/data-output/"

# Create output directory if it doesn't exist
if not os.path.exists(input_directory):
    os.makedirs(input_directory)

all_json_content = []
for filename in os.listdir(input_directory):
    filepath = os.path.join(input_directory, filename)
    with open(filepath, 'r') as file:
        content = file.read()
        json_contents = json.loads(content)
        all_json_content.extend(json_contents)

with open("manim-fine-tune/mydata.jsonl", 'w') as file:
    for entry in all_json_content:
        file.write(json.dumps(entry) + "\n")
