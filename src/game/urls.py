from django.urls import path

from game.views import *

urlpatterns = [
    path('', index, name='create'),
    path('cat_stats/', stats, name='stats'),
]
