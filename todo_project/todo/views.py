from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# 전체 할 일 목록 보기 (Read)


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

# 개별 할 일 보기 (Read)


def detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'detail.html', {'todo': todo})

# 할 일 추가 (Create)


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

# 할 일 수정 (Update)


def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})

# 할 일 삭제 (Delete)


def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'delete_todo.html', {'todo': todo})
