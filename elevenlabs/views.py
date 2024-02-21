from django.http import HttpResponse
from django.shortcuts import render
import requests


def ElevenLabs(request):
    CHUNK_SIZE = 1024

    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "652e66d3cdb1660244ac5db8102dd2cc",
    }

    data = {
        "text": "Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks and podcasts.",
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }

    try:
        response = requests.post(url, json=data, headers=headers)

        # Check the status code
        print(f"Status Code: {response.status_code}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            audio_content = response.content
            return HttpResponse(audio_content, content_type="audio/mpeg")
        else:
            print(f"Error: {response.text}")
            return HttpResponse("Error in audio generation", status=500)

    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse("An error occurred", status=500)
