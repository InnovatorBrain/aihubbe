from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
import os
from openai import OpenAI
from .models import ChatUser
from .serializers import MessageSerializer
# Authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ChatAPIView(APIView):
    # permission_classes = [IsAuthenticated] 
    queryset = ChatUser.objects.all()

    def get_queryset(self):
        return self.queryset

    def get_assistant_response(self, messages):
        client = OpenAI(api_key=os.getenv("OPENAI_NLP_KEY"))
        r = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        )
        return r.choices[0].message.content

    def get(self, request, *args, **kwargs):
        # GET method is not supported for this endpoint
        return Response({"message": "GET method is not supported for this endpoint."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        data = request.data
        user_input = data.get("user_input")

        if not user_input:
            return Response({"error": "Missing 'user_input' field in request data."}, status=status.HTTP_400_BAD_REQUEST)

        messages = [{"role": "assistant", "content": "How can I help?"}]
        messages.append({"role": "user", "content": user_input})
        assistant_response = self.get_assistant_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})

        response_data = {
            "messages": messages  
        }
        return Response(response_data, status=status.HTTP_200_OK)
