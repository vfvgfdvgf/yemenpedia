from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Notification

@receiver(post_save, sender=Task)
def create_task_notification(sender, instance, created, **kwargs):
    if created:
        if instance.assigned_to:
            Notification.objects.create(
                user=instance.assigned_to,
                message=f"مهمة جديدة: {instance.title}",
                link=f"/tasks/{instance.id}/"
            )
    else:
        if instance.status == Task.STATUS_DONE:
            Notification.objects.create(
                user=instance.created_by,
                message=f"تم إكمال المهمة: {instance.title}",
                link=f"/tasks/{instance.id}/"
            )
