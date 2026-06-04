from django.urls import path
from . import views

urlpatterns=[
    path('',views.TaskListView.as_view(),name='task_list'),
    path('add/',views.TaskCreateView.as_view(),name='add'),
    path('toggle/<int:pk>/',views.TaskToggleView.as_view(),name='toggle'),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(),name='delete'),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name="update"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("signup/",views.SignUpView.as_view(),name="signup"),
]