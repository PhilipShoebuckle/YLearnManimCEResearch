from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
import langchain


OPENAI_API_KEY = "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"


manim_llm = ChatOpenAI(temperature=0.2, model_name="ft:gpt-3.5-turbo-0613:personal::7zdQkRm1", streaming=True, callbacks=[StreamingStdOutCallbackHandler()], openai_api_key=OPENAI_API_KEY)


while True:
    query = input("Question: ")
    if query == 'break':
        break
    print()
    print("__________________________")
    response = manim_llm.predict(query)
    print("\n__________________________")