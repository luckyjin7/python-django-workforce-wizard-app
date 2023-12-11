from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserList
from .forms import ListForm

def add(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, ('New user has been added to list!'))
                return redirect('home')
            except:
                pass
    else:
        all_users = ListForm()
        return render(request, 'add.html', {'all_users': all_users})

def home(request):
    all_users = UserList.objects.all()
    return render(request, 'home.html', {'all_users': all_users})

def edit(request, user_id):
    user = UserList.objects.get(id=user_id)
    return render(request, 'edit.html', {'user': user})

def update(request, user_id):
        user = UserList.objects.get(id=user_id)
        form = ListForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, ('User has been updated!'))
            return redirect('home')
        return render(request, 'edit.html', {'user': user})

def delete(request, user_id):
    user = UserList.objects.get(id=user_id)
    user.delete()
    messages.success(request, ('User has been deleted!'))
    return redirect('home')
