from django.contrib import admin
from .models import ChatUser, ChatHistory, ChatResponse

@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'message')
    search_fields = ('user__username', 'message')

@admin.register(ChatResponse)
class ChatResponseAdmin(admin.ModelAdmin):
    list_display = ('history', 'response_message')
