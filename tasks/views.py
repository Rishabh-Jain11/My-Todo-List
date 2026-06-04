from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class TaskListView(LoginRequiredMixin,ListView):
    model=Task
    template_name="tasks/task_list.html"
    context_object_name="tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model=Task
    template_name="tasks/add_task.html"
    fields=["task","description"]
    success_url=reverse_lazy("task_list")

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    fields=["task"]
    template_name="tasks/add_task.html"
    success_url=reverse_lazy("task_list")
    def get_queryset(self):
        # ensures users can only edit their own tasks
        return Task.objects.filter(user=self.request.user)
    
class TaskToggleView(LoginRequiredMixin,View):
    def post(self,request,pk):
        task=get_object_or_404(Task ,id=pk,user=request.user)
        task.completed=not task.completed
        task.save()
        return redirect("task_list")
    
class TaskDeleteView(LoginRequiredMixin,DeleteView):
        model=Task
        template_name="tasks/task_confirm_delete.html"
        success_url=reverse_lazy("task_list")

        def get_queryset(self):
            return Task.objects.filter(user=self.request.user)
        
class TaskDeleteView(LoginRequiredMixin,DeleteView):
        model=Task
        template_name="tasks/task_confirm_delete.html"
        success_url=reverse_lazy("task_list")
        def get_queryset(self):
            return Task.objects.filter(user=self.request.user)
        def delete(self,request,*args,**kwargs):
            messages.success(request, "Task Deleted Successfully")
            return super().delete(request,*args,**kwargs)

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name="registration/signup.html"
    success_url=reverse_lazy("login")





# @login_required
# def delete_task(request,task_id):
#     task=get_object_or_404(Task,id=task_id,user=request.user)
#     task.delete()
#     return redirect("task_list")  



# @login_required
# def add_task(request):
#     if request.method=="POST":
#         title=request.POST.get("title")

#         Task.objects.create(
#             user=request.user,
#             title=title,
#             completed=False
#         )
#         return redirect("task_list")
#     return render(request,"tasks/add_task.html")

# @login_required
# def task_list(request):
#     tasks=Task.objects.filter(user=request.user)
#     return render(request,'tasks/task_list.html',{'tasks':tasks})
