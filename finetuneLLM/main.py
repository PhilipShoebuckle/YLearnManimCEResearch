from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import openai
import threading
from threading import BoundedSemaphore

openai.api_key = "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"

MAX_CONCURRENT_REQUESTS = 5  # adjust this based on your needs
semaphore = BoundedSemaphore(MAX_CONCURRENT_REQUESTS)


def process_file(file_name):
    semaphore.acquire()
    try:
        with open(os.path.join(directory_path, file_name), 'r') as f:
            content = f.read()

        system_content = """
        You are helping me create coding data in JSON format to fine-tune a large language model on Manim python.
        """
        assistant_content = """
        OpenAI fine-tuning endpoints require a specific data format: JSON, with each line containing a prompt and a completion.
        Example:
        {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
        {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
        {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
        Convert the given text into the JSON format described above in q/a pairs for fine tuning. Be very specific and comprehensive. The more data you provide, the better the model will be. It's made for coding questions so make sure you include a lot of coding specific questions and answers and comprehensive.
        Always include object types and return types.
        """

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4000,
            chunk_overlap=0,
            length_function=len,
            add_start_index=True,
        )

        chunks = text_splitter.create_documents([content])

        for chunk in chunks:
            text = chunk.page_content
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "assistant", "content": assistant_content},
                    {"role": "user", "content": text}
                ])

            with open(f"manim-fine-tune/data-output/{file_name}.json", "a") as f:
                f.write(completion['choices'][0]['message']['content'] + "\n")
    except Exception as e:
        with open("manim-fine-tune/error_log.txt", "a") as error_log:
            error_msg = f"Error processing {file_name}: {str(e)}\n"
            error_log.write(error_msg)
            print(error_msg)
    finally:
        semaphore.release()


directory_path = "manim-fine-tune/manim-docs"
files = [f for f in os.listdir(directory_path) if os.path.isfile(
    os.path.join(directory_path, f))]

threads = []

# # For each file, start a new thread
# for file_name in files:
#     thread = threading.Thread(target=process_file, args=(file_name,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# process ChangeDecimalToValue.txt, SmoothedVectorizedHomotopy.txt
# MoveToTarget.json
# ScreenRectangle.json
process_file("ScreenRectangle.txt")
print("All files processed!")
