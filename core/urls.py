from django.urls import path,include
from . import views

app_name='core'

urlpatterns = [
    path('',views.PlayView.as_view(),name='play'),
    path('results/',views.results.as_view(),name='results'),
    path('round/',views.RoundView.as_view(),name='round')
    
]