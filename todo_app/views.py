from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#
from .models import ToDoList, ToDoItem
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import ItemForm, ListtitleForm




def add_todo_list(request):
    submitted=False
    if request.method=="POST":
        form=ListtitleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_todo_list?submitted=True')
    else:
        form=ListtitleForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'todo_list/add_todo_list.html', {'form':form, 'submitted':submitted})

def update_todo_list(request, event_id):
    event = ToDoList.objects.get(pk=event_id)
	#if request.user.is_superuser:
		#form = ItemFormAdmin(request.POST or None, instance=event)	
	#else:
    form=ListtitleForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-todo_lists')
    return render(request, 'todo_list/update_todo_list.html', {'event':event, 'form':form}) 
def delete_todo_list(request, event_id):
    event=ToDoList.objects.get(pk=event_id)
    event.delete()
    return redirect('list-todo_lists')  






def add_todo_item(request):
    submitted=False
    if request.method=="POST":
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_todo_item?submitted=True')
    else:
        form=ItemForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'todo_list/add_todo_item.html', {'form':form, 'submitted':submitted})


def delete_todo_item(request, item_id):
    item=ToDoItem.objects.get(pk=item_id)
    item.delete()
    return redirect('list-todo_items')

def update_todo_item(request, item_id):
	item = ToDoItem.objects.get(pk=item_id)
	#if request.user.is_superuser:
		#form = ItemFormAdmin(request.POST or None, instance=event)	
	#else:
	form = ItemForm(request.POST or None, instance=item)
	
	if form.is_valid():
		form.save()
		return redirect('list-todo_items')

	return render(request, 'todo_list/update_todo_item.html', {'item':item, 'form':form})   








def all_todo_lists(request):
	#venue_list = Venue.objects.all().order_by('?')
	events = ToDoList.objects.all()

	# Set up Pagination
	#p = Paginator(Venue.objects.all(), 3)
	#page = request.GET.get('page')
#	nums = "a" * venues.paginator.num_pages
	return render(request, 'todo_list/todo_list.html', {'events': events })

def all_todo_items(request):
    todo_item=ToDoItem.objects.all().order_by('due_date')
    return render(request, 'todo_list/todo_item.html', {'todo_item': todo_item})






def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month=month.capitalize()
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)
    cal=HTMLCalendar().formatmonth(year, month_number)
    now=datetime.now()
    current_year=now.year
    time=now.strftime('%I:%M:%S %p')
    Todo_list=ToDoItem.objects.filter(due_date__year=year, due_date__month=month_number)
    return render(request, 'todo_list/calendar.html', {
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal":cal,
        "current_year": current_year,
        "time": time,
        "Todo_list":Todo_list,
        })
    #return render(request, 'home.html', {})
def welcome(request):
    caption="welcome user please login to experience the Todolist website"
    return render(request, 'todo_list/home.html', {"caption":caption} ) 

# Create your views here.
