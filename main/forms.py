from django import forms

class createNewList(forms.Form):
    name = forms.CharField(label="Enter Todo List Name: ", max_length=200)

class createNewItem(forms.Form):
    list = forms.Select()
    text = forms.CharField(label="Enter Your mission: ", max_length=200)
    complete = forms.BooleanField(label="Complete ? ", required=False)