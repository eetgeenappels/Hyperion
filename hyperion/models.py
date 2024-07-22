from django.db import models


class Message(models.Model):
    sender_type = models.CharField(max_length=1)
    conversation_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    message_index = models.IntegerField()


class User(models.Model):
    user_id = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=100)
