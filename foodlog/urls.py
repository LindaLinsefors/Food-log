from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Lists
    url(r'^list$', 'food.views.home', name='food_stuff_list'),
    url(r'^list$', 'food.views.home', name='food_entry_list'),

    # Menu
    url(r'^$', 'food.views.menu', name='menu'),
    url(r'^$', 'food.views.menu', name='home'),

    # Data
    url(r'^data$', 'food.views.data',  name='data'),

    # FoodStuff
    url(r'^food_stuff/new$', 
            'food.views.new_food_stuff',  name='new_food_stuff'),
    url(r'^food_stuff/(?P<id>\d+)/$', 
            'food.views.edit_food_stuff', name='edit_food_stuff'),
    url(r'^delete_food_stuff$', 
            'food.views.delete_food_stuff', name='delete_food_stuff'),

    # FoodEntry
    url(r'^food_entry/new$', 
            'food.views.new_food_entry',  name='new_food_entry'),
    url(r'^food_entry/(?P<id>\d+)/$', 
            'food.views.edit_food_entry', name='edit_food_entry'),
    url(r'^food_entry/(?P<id>\d+)/delete$', 
            'food.views.delete_food_entry', name='delete_food_entry'),

    # Internal
    url(r'^get_info/$', 
            'food.views.get_food_stuff_info', name='get_food_stuff_info'),

    url(r'^js/$',
            'food.views.food_entry_js', name='food_entry_js'),


    # Admin    
    url(r'^admin/', include(admin.site.urls)),
)
