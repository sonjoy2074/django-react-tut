from django.urls import path
from status import views

urlpatterns =[
    path('all/', views.all_statuses.as_view(), name='all_statuses'),
]