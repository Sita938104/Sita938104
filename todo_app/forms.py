from django import forms
from django.forms import ModelForm
from .models import ToDoItem, ToDoList
class ItemForm(ModelForm):
    class Meta:
        model=ToDoItem
        fields=('title', 'description', 'quantity', 'due_date', 'todo_list')
        labels={'title':'', 'description':'', 'quantity':'', 'due_date':'YYYY-MM-DD HH-MM-SS', 'todo_list':'todo_list'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Todoitem Title'}),
                 'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
                 'quantity':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantity'}),
                 'due_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Due_date'}),
                 'todo_list':forms.Select(attrs={'class':'form-select', 'placeholder':'todo_list'})
                }  
class ListtitleForm(ModelForm):
    class Meta:
        model=ToDoList
        fields=('title',)
        labels={'title':''}
        widgets={'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'todolist_title'})}                    
