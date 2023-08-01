from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import createNewList, createNewItem

# Create your views here.
def home(response):
    return render(response, "main/home.html", {"username": response.user.username})

def create(response):
    if response.method == "POST":
        form = createNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name= n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = createNewList()

    return render(response, "main/create_list.html", {"form": form})

def editList(response, id):
    tdl = ToDoList.objects.get(id=id)
    if response.user.is_authenticated and tdl in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in tdl.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("addItem"):
                txt = response.POST.get("text")
                if len(txt) > 2:
                    tdl.item_set.create(text= txt, complete= False)

        return render(response, "main/edit_list.html", {"tdl": tdl})

    else:
        return render(response, "main/view.html", {})

def view(response):
    render(response, "main/view.html", {})