import time
import os
import openai
openai.api_key = "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"
# file_obj = openai.File.create(
#     file=open(
#         "/Users/advaitpaliwal/Projects/youlearn-backend-v2/manim-fine-tune/mydata.jsonl", "rb"),
#     purpose='fine-tune'
# )

# print(file_obj)

# response = openai.FineTuningJob.create(
#     training_file="file-VvAfaWZ7K7DHtIwKsid2s9w8", model="gpt-3.5-turbo")


while True:
    res = openai.FineTuningJob.retrieve("ftjob-dLCsEQan4JMDzOddXLZmubMO")
    print(res)
    if res["finished_at"] != None:
        break
    else:
        print(".", end="")
        time.sleep(100)
