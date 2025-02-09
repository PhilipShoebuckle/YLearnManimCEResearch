import os
import re
import json
import openai
# Path to the directory containing your files
input_directory = "manim-fine-tune/data-output/"
openai.api_key = "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"
# Create output directory if it doesn't exist

# Regex pattern to extract json objects
pattern = r'\{.*?\}'

# Iterate over all files in the input directory
for filename in os.listdir(input_directory):
    # if filename.endswith(".txt"):
    with open(os.path.join(input_directory, filename), 'r') as file:
        content = file.read()

        # Use regex to find all JSON strings
        matches = re.findall(pattern, content, re.DOTALL)
        print(matches)
        # List to hold dictionaries
        data_list = []
        # Convert each JSON string to a dictionary and append to data_list
        for match in matches:
            if "prompt" not in match and "completion" not in match:
                continue
            max_checks = 5
            while max_checks > 0:
                print("checking", match)
                try:
                    match = json.loads(match)
                    processed_match = {
                        "messages": [
                            {"role": "user", "content": match["prompt"]},
                            {"role": "assistant",
                                "content": match["completion"]}
                        ]
                    }
                    data_list.append(processed_match)
                    break
                except:
                    try:
                        completion = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system",
                                    "content": "You are fixing the json format"},
                                {"role": "assistant",
                                    "content": "I will give you a string, convert it to a valid json format"},
                                {"role": "user", "content": match}
                            ])
                        match = completion['choices'][0]['message']['content']
                        max_checks -= 1
                    except:
                        max_checks -= 1
                        continue

        # Save dictionaries to a new file in the output directory
        if len(data_list) > 0:
            with open(os.path.join(input_directory, filename), 'w') as new_file:
                print(data_list)
                json.dump(data_list, new_file)
            print("Processed", filename)

    # Delete the old file from the input directory
    # os.remove(os.path.join(input_directory, filename))

print("Processing complete.")
