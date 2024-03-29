# Generated by Django 5.0.2 on 2024-02-21 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0002_chathistory_chatresponse_chatuser_delete_chat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chatresponse',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='chatgpt.chathistory'),
        ),
        migrations.AlterField(
            model_name='chatresponse',
            name='response_message',
            field=models.TextField(),
        ),
    ]
