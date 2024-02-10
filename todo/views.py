from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ToDo
from .forms import MyToDoForm

def home(request):
    form = MyToDoForm()
    todo_lists = ToDo.objects.all()

    if request.method == 'POST':
        form = MyToDoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre nom est enregistré avec succès.')
            return redirect('home')

    else:
        form = MyToDoForm()

    context = {
        'form': form,
        'todo_lists': todo_lists
    }
    return render(request, 'todo/home.html', context)


def update(request, pk):
    todo_list = ToDo.objects.get(id=pk)
    form = MyToDoForm(instance=todo_list)
    if request.method == 'POST':
        todo_list.nom = request.POST.get('nom')
        todo_list.save()
        messages.success(request, 'Modifié avec succès.')
        return redirect('home')
    
    
    context = {
        'form': form,
        'todo_list': todo_list
    }
    return render(request, 'todo/update.html', context)


def delete(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')

    return render(request, 'todo/delete.html', {'todo': todo})