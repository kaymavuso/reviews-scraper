from django.forms import ModelForm
from django import forms
from .models import Job

# Django will look into the Project model and create a form
# based on the forms attributes
class JobForm(ModelForm):
    # Model Meta is basically the inner class of your model class.
    # It is basically used to change the behavior of your model fields
    # like changing order options,verbose_name, and a lot of other options.
    # It’s completely optional to add a Meta class to your model.
    class Meta:
        model = Job
        # fields = '__all__'
        fields = ['name', 'selected_store', 'selected_brand', 'selected_product']