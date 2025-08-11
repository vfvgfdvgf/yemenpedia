from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/done/<int:task_id>/", views.mark_task_done, name="mark_task_done"),
    path("notifications/", views.notifications, name="notifications"),
]
