from django.urls import include, path
from .views import *

urlpatterns = [
    path('games',get_games,name='list_games'),
    path('games/<int:pk>',get_games,name='game'),

]