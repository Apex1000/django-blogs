from django.urls import path
from todo import views
urlpatterns = [
    path('todo/', views.todos_list),
    path('todo/<int:id>', views.todo_detail),

]
