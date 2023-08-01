from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# t = ToDoList(name="othman")
# ToDoList.objects.all()
# ToDoList.objects.get(id=1)
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# t.item_set.all()
# t.item_set.create(text= "go shopping", complete= False)
# t.item_set.get(id=1)
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text