"""
Models module for the application.

This module defines the database models using Django's ORM.
Each class represents a database table.
"""

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Model class for storing data.
    
    Attributes:
        user: The user who sent the message
        content: The content of the message
        timestamp: The time when the message was created
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'aplicacion'

    def __str__(self):
        return f"{self.user.username}: {self.content}"
