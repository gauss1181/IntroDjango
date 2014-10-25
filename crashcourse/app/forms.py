from django import forms
from app.models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Enter new task:")
    category = forms.CharField(max_length=200, help_text="Enter a category for this task:")

    # Inline class to provide additional information about this form
    class Meta:
        model = Task
