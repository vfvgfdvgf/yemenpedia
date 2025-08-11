# core/views.py
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Task, Notification
from .forms import TaskForm

def is_owner(user):
    return user.groups.filter(name='Owner').exists()

def is_moderator(user):
    return user.groups.filter(name='Moderator').exists()

@login_required
@user_passes_test(is_owner)
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.status = Task.STATUS_ASSIGNED
            task.save()
            messages.success(request, "تم إنشاء المهمة بنجاح")
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "core/task_create.html", {"form": form})

@login_required
def task_list(request):
    if is_moderator(request.user):
        tasks = Task.objects.filter(assigned_to=request.user)
    elif is_owner(request.user):
        tasks = Task.objects.all()
    else:
        tasks = []
    return render(request, "core/task_list.html", {"tasks": tasks, "is_moderator": is_moderator(request.user)})

@login_required
def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not is_moderator(request.user) or task.assigned_to != request.user:
        return HttpResponseForbidden("غير مسموح")
    task.status = Task.STATUS_DONE
    task.save()
    messages.success(request, "تم إنهاء المهمة")
    return redirect("task_list")

@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user)
    return render(request, "core/notifications.html", {"notifications": notes})
# core/views.py
@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user)
    notes.update(is_read=True)  # تعليم الكل كمقروء
    return render(request, "core/notifications.html", {"notifications": notes})
