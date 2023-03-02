from django.shortcuts import render, redirect
from .forms import Todoforms
from .models import Todo
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
class TodoListview(ListView):
     model = Todo
     template_name = 'home.html'
     context_object_name = 'toi'
class Tododetail(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name ='toi'
class Todoupdate(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'toi'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy("cdetail", kwargs={"pk":self.object.id})
class Tododelete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url =reverse_lazy("clist")
def add(request):
    to1 = Todo.objects.all()
    if request.method=='POST':
        name=request.POST['task']
        priority=request.POST['priority']
        date=request.POST['date']
        to=Todo(name=name,priority=priority,date=date)
        to.save()
    return render(request,'home.html',{"toi":to1})
def delete(request,taskid):
    tas=Todo.objects.get(id=taskid)
    if request.method=='POST':
        ta=tas
        ta.delete()
        return redirect("/")
    return  render(request,'delete.html')
def update(request,id):
    toi=Todo.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=toi)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,"update.html",{"toi":toi,"form":form})
