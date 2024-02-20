from django.shortcuts import render
from django.http import HttpResponse
from google import generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import pathlib
import textwrap
import os

# Create your models here.
"""TEXT-TO-TEXT
   IMAGE-TO-TEXT"""


def geminichat(request):
    def to_markdown(text):
        text = text.replace("•", "  *")
        return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

   
    # API THROUGH VARIABLE OF google-generativeai
    genai.configure(os.environ.get("GOOGLE_API_KEY"))

    # PART - 3
    def run_conversation(initial_message, num_turns=3):
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=[])

        for _ in range(num_turns):
            user_input = input("User: ")
            chat_response = chat.send_message(user_input)
            # The RESPONSE IN Here
            return (f"Model: {chat_response.parts[0].text}\n")

    initial_message = ""
    num_turns = 3  # Adjust the number of turns as needed

    # Call the run_conversation function
    conversation_result = run_conversation(initial_message, num_turns)

    # Return the conversation_result as an HTTP response
    return HttpResponse(conversation_result)
