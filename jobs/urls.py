from django.urls import path
from . import views


# ALL app specific paths will be connected to the urls.py file in the project root directory via Django's built in urls include() method
urlpatterns = [
    path('jobs/', views.jobs, name="jobs"),
    path('job/<str:primary_key>/', views.job, name="job"),
    
]