from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, NewTodoForm
from django.views.generic import (
    View,
)


class IndexView(View):
    def get(self,request):
        todo_list = Todo.objects.order_by('id')
        # form = TodoForm()
        form = NewTodoForm()
        context = {
            'todo_list':todo_list,
            'form':form,
        }
        return render(request,'todo/index.html',context)
    def post(self,request):
        # form = TodoForm(request.POST)
        # if form.is_valid():
        #     new_todo = Todo(text=request.POST['text'])
        #     new_todo.save()
        #     return redirect('home')

        # todo_id = Todo.objects.get(id=14)
        # form = NewTodoForm(request.POST, instance=todo_id)
        
        form = NewTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

class ComplateView(View):
    def get(self,request,id):
        todo = Todo.objects.get(id=id)
        todo.complete=True
        todo.save()
        return redirect('home')

class DeleteCompleteView(View):
    def get(self,request):
        todo = Todo.objects.filter(complete=True)
        todo.delete()
        return redirect('home')

class DeleteAllView(View):
    def get(self,request):
        todo = Todo.objects.all()
        todo.delete()
        return redirect('home')