from django.http import HttpResponse
from openai import OpenAI
import os


"""
    TEXT-TO-TEXT
"""


def index(request):

    client = OpenAI(
        # OPENAI_API_KEY
        api_key=os.getenv("OPENAI_NLP_KEY"),
    )

    def display_chat_history(messages):
        for message in messages:
            print(f"{message['role'].capitalize()}: {message['content']}")

    def get_assistant_response(messages):
        r = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        )
        response = r.choices[0].message.content
        return response

    messages = [{"role": "assistant", "content": "How can I help?"}]

    while True:
        display_chat_history(messages)

        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})

        assistant_response = get_assistant_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})
        # Display chat from here
        return HttpResponse(assistant_response)
