from django.contrib import admin
from django.urls import path
from toll.views import news_list,scrape,grape,gaming,entertainment,sports,politics
urlpatterns = [
    path('scrape/', scrape, name="scrape"),
    path('grape/', grape, name="grape"),
    path('gaming/', gaming, name="gaming"),
    path('sports/', sports, name="sports"),
    path('entertainment/', entertainment, name="entertainment"),
    path('politics/', politics, name="politics"),


    path('', news_list, name="home"),
    
]