from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'food.views.home', name='home'),

    url(r'^food_stuff/new$', 
            'food.views.new_food_stuf', name='new_food_stuf'),
    url(r'^food_stuff/(?P<id>\d+)/$', 
            'food.views.edit_food_stuf', name='edit_food_stuf'),

    url(r'^food_entry/new$', 
            'food.views.new_food_entry', name='new_food_entry'),
    url(r'^food_entry/(?P<id>\d+)/$', 
            'food.views.edit_food_entry', name='edit_food_entry'),
    
    url(r'^admin/', include(admin.site.urls)),
)
