from django.urls import path
from . import views


# ALL app specific paths will be connected to the urls.py file in the job root directory via Django's built in urls include() method
urlpatterns = [
    # path('jobs/', views.jobs, name="jobs"),
    path('', views.jobs, name="jobs"),
    path('job/<str:primary_key>/', views.job, name="job"),

    path('create-scrape-job', views.createScrapeJob, name="create-scrape-job"),
    path('update-scrape-job/<str:primary_key>', views.updateScrapeJob, name="update-scrape-job"),
    path('delete-scrape-job/<str:primary_key>', views.deleteScrapeJob, name="delete-scrape-job"),
]