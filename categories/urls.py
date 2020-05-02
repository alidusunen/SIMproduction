from .views import *
from django.urls import path

app_name = 'categories'

urlpatterns = [
    path('', view_categories, name='view-categories'),
    path('cat/create/', cat_create, name='cat-create'),
    path('subcat/create/', subcat_create, name='subcat-create'),

]
