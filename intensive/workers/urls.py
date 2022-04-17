from django.urls import re_path
from .views import Task1View, Task2View, Task3View, Task4View

urlpatterns = [
    re_path(r'task-1/$', Task1View.as_view()),
    re_path(r'task-2/$', Task2View.as_view()),
    re_path(r'task-3/$', Task3View.as_view()),
    re_path(r'task-4/$', Task4View.as_view()),
]