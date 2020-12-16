from django.urls import path
from basic_app import views

#template tagging here app_name variable is always named by convention
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]