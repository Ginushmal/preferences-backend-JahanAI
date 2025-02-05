from django.contrib.auth.models import User
from django.db import models

class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=[("light", "Light"), ("dark", "Dark")], default="light")
    notifications = models.BooleanField(default=True)
    email_frequency = models.CharField(max_length=10, choices=[("daily", "Daily"), ("weekly", "Weekly")], default="daily")
    profile_visibility = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=True)
    notification_type = models.CharField(
        max_length=20, choices=[("email", "Email"), ("push", "Push Notifications")], default="push"
    )
    notification_frequency = models.CharField(
        max_length=10, choices=[("daily", "Daily"), ("weekly", "Weekly")], default="daily"
    )

    def __str__(self):
        return f"{self.user.username} Notification Settings"

class ThemeSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(
        max_length=10, choices=[("light", "Light"), ("dark", "Dark")], default="light"
    )
    font_style = models.CharField(
        max_length=20, choices=[("default", "Default"), ("serif", "Serif"), ("sans-serif", "Sans-serif")], default="default"
    )
    layout = models.CharField(
        max_length=20, choices=[("standard", "Standard"), ("compact", "Compact"), ("spacious", "Spacious")], default="standard"
    )

    def __str__(self):
        return f"{self.user.username} Theme Settings"

class PrivacySettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_visibility = models.BooleanField(default=True)
    data_sharing = models.CharField(
        max_length=10, choices=[("all", "Share with everyone"), ("friends", "Share with friends"), ("private", "Don't share")], default="private"
    )

    def __str__(self):
        return f"{self.user.username} Privacy Settings"
