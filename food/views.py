from __future__ import division 
from django.shortcuts import get_object_or_404, render
from django import forms
from models import FoodEntry, FoodStuff
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist 
from django.core import serializers
import datetime


# Home

def home(request):
    food_entries = FoodEntry.objects.all()
    food_stuffs  = FoodStuff.objects.all()
    return render(request, 
                  'food/home', 
                  {'food_entries': FoodEntry.objects.all(),
                   'food_stuffs' : FoodStuff.objects.all() } )



# Data

def data(request):
    return render(request, 'food/data.html')




# Imput

def save(food_entry, post):
    try:
        food_stuff = FoodStuff.objects.get( name=post['food_stuff'] )
    except ObjectDoesNotExist:
        food_stuff = FoodStuff( name=post['food_stuff'] )

    for food_type in (  'fruit', 'dairy', 'water', 'junk',
                        'veg', 'protein', 'startch', 'unknown'):
        if post[food_type] == u'':
            setattr(food_entry, food_type, 0)
            setattr(food_stuff, food_type, 0)
        else:
            setattr(food_entry, food_type, int(float(post[food_type])) )
            setattr(food_stuff, food_type, int(float(post[food_type])) )

    datetime_string = post['date']+' '+post['time']
    food_entry.datetime = datetime.datetime.strptime(
                                datetime_string, "%Y-%m-%d %H:%M")

    food_entry.amount = post['amount']
    food_entry.quantity = float(post['quantity'])
    food_entry.food_stuff = post['food_stuff']
    food_entry.ingredients = post['ingredients']
    food_entry.save()

    food_stuff.name = post['food_stuff']
    food_stuff.ingredients = post['ingredients']
    food_stuff.save()


def food_entry_js(request):
    return render( request, 'food/food_entry.js' )


def new_food_entry(request):
    if request.method == 'POST':
        save( FoodEntry(), request.POST )
        return HttpResponseRedirect( reverse('home') )

    now = datetime.datetime.now()

    return render(  request, 'food/food_entry.html',
                   {'food_stuffs': FoodStuff.objects.all(),
                    'date': now.strftime("%Y-%m-%d"),
                    'time': now.strftime("%H:%M"),
                   } )   


def edit_food_entry(request, id):
    food_entry = get_object_or_404(FoodEntry, pk=id)

    if request.method == 'POST':
        save( food_entry, request.POST )
        return HttpResponseRedirect( reverse('home') )

             
    return render(  request, 'food/edit_food_entry.html',
                   {'food_stuffs': FoodStuff.objects.all(), 
                    'food_entry': food_entry,                
                    'quantity': round(food_entry.quantity,2),    
                    'date': food_entry.datetime.strftime("%Y-%m-%d"),
                    'time': food_entry.datetime.strftime("%H:%M"),
                   } )   


def delete_food_entry(request, id):
    food_entry = get_object_or_404(FoodEntry, pk=id)
    food_entry.delete()
    return HttpResponseRedirect( reverse('home') )
    


def get_food_stuff_info(request):
    food_stuff_name = request.POST['food_stuff_name']
    try:
        food_stuff = FoodStuff.objects.get( name=food_stuff_name )
    except ObjectDoesNotExist:
        return HttpResponse('does_not_exist')

    return HttpResponse(serializers.serialize('json', [food_stuff]))

    



class FoodStuffForm(forms.ModelForm):
    class Meta:
        model=FoodStuff

    ingredients = forms.CharField(max_length=500, widget=forms.Textarea, required=False )




def edit(request, Class, ClassForm, id, template='food/form_template'):
    class_instance = get_object_or_404(Class, pk=id)

    if request.method == 'POST':
        class_form = ClassForm(request.POST, instance=class_instance)
        if class_form.is_valid():
            class_form.save()
    else:
        class_form = ClassForm(instance=class_instance)     

    return render(  request, template,
                   {'class_form': class_form, 
                    'id':id,
                    'class_instance': class_instance}   )   



def new(request, Class, ClassForm, url, template='food/form_template'):
    if request.method == 'POST':
        class_form = ClassForm(request.POST)
        if class_form.is_valid():
            class_form.save()
            return HttpResponseRedirect(            
                reverse(url, args=(class_form.instance.id,))  )
    else:
        class_form = ClassForm()

    return render(  request, template,
                   {'class_form': class_form}   )  



def new_food_stuff(request):
    return new(request, FoodStuff, FoodStuffForm, 'food_stuff', 
        template='food/food_stuff.html')

def edit_food_stuff(request, id):
    return edit(request, FoodStuff, FoodStuffForm, id,
        template='food/food_stuff.html')

def delete_food_stuff(request, id):
    food_stuff = get_object_or_404(FoodStuff, pk=id)
    food_stuff.delete()
    return HttpResponseRedirect( reverse('home') )
