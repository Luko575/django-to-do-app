from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm


def home(request):
    tasks = Task.objects.filter(is_archived=False, is_deleted=False)
    context = {'tasks': tasks, 'form': TaskForm}
    return render(request, 'home.html', context=context)


def archived(request):
    tasks_archived = Task.objects.filter(is_archived=True, is_deleted=False)
    context = {'tasks_archived': tasks_archived}
    return render(request, 'archived.html', context=context)


def deleted(request):
    tasks_deleted = Task.objects.filter(is_archived=False, is_deleted=True)
    context = {'tasks_deleted': tasks_deleted}
    return render(request, 'deleted.html', context=context)


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
    return redirect('home')


def update(request, pk):
    obj = Task.objects.get(pk=pk)
    if request.method == 'POST':
            form = TaskForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
    else:
        action = request.GET.get('action')
        if action == 'is_completed':
            obj.is_completed = not obj.is_completed
        elif action == 'is_archived':
            obj.is_archived = not obj.is_archived
            obj.is_deleted = False 
        elif action == 'is_deleted':
            obj.is_deleted = not obj.is_deleted
            obj.is_archived = False   
        else:
            return redirect('home')
        obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


def empty_recycle_bin(request):
    obj = Task.objects.filter(is_deleted=True)
    obj.delete()
    return redirect('deleted')