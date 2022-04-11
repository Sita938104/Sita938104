from django import views
from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    #path('<int:year>/<str:month>/', views.home, name="home"),
    path('', views.welcome, name="welcome"),
    path('todo_items', views.all_todo_items, name="list-todo_items"),
    path('todo_list', views.all_todo_lists, name="list-todo_lists"),
    path('add_todo_item', views.add_todo_item, name='add-todo_item'),
    path('update_item/<item_id>', views.update_todo_item, name='update-todo_item'),
    path('delete_item/<item_id>', views.delete_todo_item, name='delete-todo_item'),
    path('add_todo_list', views.add_todo_list, name='add-todo_list'),
    path('update_event/<event_id>', views.update_todo_list, name='update-event'),
    path('delete_event/<event_id>', views.delete_todo_list, name='delete-event'),
]