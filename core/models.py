from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    STATUS_NEW = "new"
    STATUS_ASSIGNED = "assigned"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"
    STATUS_CHOICES = [
        (STATUS_NEW, "جديدة"),
        (STATUS_ASSIGNED, "مُسندة"),
        (STATUS_IN_PROGRESS, "قيد التنفيذ"),
        (STATUS_DONE, "مكتملة"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name="created_tasks", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

class Notification(models.Model):
    user = models.ForeignKey(User, related_name="notifications", on_delete=models.CASCADE)
    message = models.CharField(max_length=512)
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    link = models.CharField(max_length=512, blank=True, help_text="رابط اختياري")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"إشعار لـ {self.user}: {self.message[:50]}"
# core/models.py
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)  # جديد
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
