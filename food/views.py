from __future__ import division 
from django.shortcuts import get_object_or_404, render
from django import forms
from models import FoodEntry, FoodStuff, DayTotal, MonthTotal, YearTotal
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist 
from django.core import serializers
from django.db.models import Sum
import datetime


# Now and Today

def now():
    return datetime.datetime.now()

def today():
    return datetime.datetime.now().date()



# Home

def home(request):
    food_entries = FoodEntry.objects.all()
    food_stuffs  = FoodStuff.objects.all()
    return render(request, 
                  'food/home', 
                  {'food_entries': FoodEntry.objects.all(),
                   'food_stuffs' : FoodStuff.objects.all() } )



# Menu

def menu(request):
    return render(request, 'food/menu.html')





# Data

def data(request):

    date = today()
    try:
        day_total = DayTotal.objects.get( date=date )
    except ObjectDoesNotExist:
        day_total = False

    date -= datetime.timedelta(days=1)
    try:
        month_total = MonthTotal.objects.get( year=date.year, month=date.month )
    except ObjectDoesNotExist:
        if save_month_total( year=date.year, month=date.month ):
            month_total = MonthTotal.objects.get( year=date.year, month=date.month )
            save_year_total( year=date.year )
        else:
            month_total = False
    else:
        if month_total.last_updated < today():
            save_month_total(date.year, date.month)
            month_total = MonthTotal.objects.get( year=date.year, month=date.month )

    try:
        year_total = YearTotal.objects.get( year=date.year )
    except ObjectDoesNotExist:
        if save_year_total( year=date.year ):
            year_total = YearTotal.objects.get( year=date.year )
        else:
            year_total = False

    return render(request, 'food/data_google.html',
                    {   'day_total': day_total,
                        'month_total': month_total,
                        'year_total': year_total, 
                    })






# Totals

def save_day_total( date ):
    try:
        day_total = DayTotal.objects.get( date=date )
    except ObjectDoesNotExist: 
        day_total = DayTotal( date=date )

    
    #food_entries = FoodEntry.objects.raw('''
    #                    SELECT id,
    #                    fruit * quantity / 100 AS fruit
    #                    FROM food_FoodEntry
    #                    ''')
                                                



    food_entries = FoodEntry.objects.filter( datetime__year=date.year,
                                        datetime__month=date.month,
                                        datetime__day=date.day,     ) 

    if food_entries.count() == 0:
        try:
            day_total.delete()
        except:
            pass
        finally:
            return False
        
    day_total.fruit = 0
    day_total.dairy = 0
    day_total.water = 0
    day_total.junk  = 0
    day_total.veg   = 0
    day_total.protein = 0
    day_total.startch = 0
    day_total.unknown = 0

    for food_entry in food_entries:
        day_total.fruit += food_entry.fruit * food_entry.quantity / 100
        day_total.dairy += food_entry.dairy * food_entry.quantity / 100
        day_total.water += food_entry.water * food_entry.quantity / 100
        day_total.junk  += food_entry.junk * food_entry.quantity / 100
        day_total.veg   += food_entry.veg * food_entry.quantity / 100
        day_total.protein += food_entry.protein * food_entry.quantity / 100
        day_total.startch += food_entry.startch * food_entry.quantity / 100
        day_total.unknown += food_entry.unknown * food_entry.quantity / 100

    day_total.save()

    return True



def save_month_total(year, month):
    try:
        month_total = MonthTotal.objects.get( year=year, month=month )
    except ObjectDoesNotExist: 
        month_total = MonthTotal( year=year, month=month )

    days = DayTotal.objects.filter(date__year=year, date__month=month
                ).exclude( date=today() )

    month_total.days = days.count()

    if month_total.days == 0:
        try:
            month_total.delete()
        except:
            pass
        finally:
            return False

    month_total.fruit = days.aggregate( Sum('fruit') ).values()[0]
    month_total.dairy = days.aggregate( Sum('dairy') ).values()[0]
    month_total.water = days.aggregate( Sum('water') ).values()[0]
    month_total.junk  = days.aggregate( Sum('junk')  ).values()[0]
    month_total.veg   = days.aggregate( Sum('veg')   ).values()[0]
    month_total.protein = days.aggregate( Sum('protein') ).values()[0]
    month_total.startch = days.aggregate( Sum('startch') ).values()[0]
    month_total.unknown = days.aggregate( Sum('unknown') ).values()[0]

    month_total.last_updated = today()

    month_total.save()

    return True


def save_year_total(year):
    try:
        year_total = YearTotal.objects.get( year=year )
    except ObjectDoesNotExist: 
        year_total = YearTotal( year=year )

    months = MonthTotal.objects.filter( year=year )

    year_total.days = months.aggregate( Sum('days') ).values()[0]

    if year_total.days == None:
        try:
            year_total.delete()
        except:
            pass
        finally:
            return False

    year_total.fruit = months.aggregate( Sum('fruit') ).values()[0]
    year_total.dairy = months.aggregate( Sum('dairy') ).values()[0]
    year_total.water = months.aggregate( Sum('water') ).values()[0]
    year_total.junk  = months.aggregate( Sum('junk')  ).values()[0]
    year_total.veg   = months.aggregate( Sum('veg')   ).values()[0]
    year_total.protein = months.aggregate( Sum('protein') ).values()[0]
    year_total.startch = months.aggregate( Sum('startch') ).values()[0]
    year_total.unknown = months.aggregate( Sum('unknown') ).values()[0]

    year_total.last_updated = today()

    year_total.save()

    return True




# Food Entry

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

    date = datetime.datetime.strptime(post['date'], "%Y-%m-%d").date()

    save_day_total( date )
    
    if date != today():
        save_month_total( date.year, date.month )
        save_year_total( date.year )
    


def food_entry_js(request):
    return render( request, 'food/food_entry.js' )


def new_food_entry(request):
    if request.method == 'POST':
        save( FoodEntry(), request.POST )
        return HttpResponseRedirect( reverse('home') )

    return render(  request, 'food/food_entry.html',
                   {'food_stuffs': FoodStuff.objects.all(),
                    'date': now().strftime("%Y-%m-%d"),
                    'time': now().strftime("%H:%M"),
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
    

# Food Stuff

def get_food_stuff_info(request):
    food_stuff_name = request.POST['food_stuff_name']
    try:
        food_stuff = FoodStuff.objects.get( name=food_stuff_name )
    except ObjectDoesNotExist:
        return HttpResponse('does_not_exist')

    return HttpResponse(serializers.serialize('json', [food_stuff]))

    

def edit_food_stuff(request, id):
    food_stuff = get_object_or_404(FoodStuff, pk=id)

    if request.method == 'POST':
        save_food_stuff( request.POST )
        return HttpResponseRedirect( reverse('data') )
             
    return render(  request, 'food/edit_food_stuff.html',
                   {'food_stuffs': FoodStuff.objects.all(), 
                    'food_stuff': food_stuff,                
                   } )   

def new_food_stuff(request):

    if request.method == 'POST':
        save_food_stuff( request.POST )
        return HttpResponseRedirect( reverse('data') )
             
    return render(  request, 'food/edit_food_stuff.html',
                   {'food_stuffs': FoodStuff.objects.all(),              
                   } )   


def save_food_stuff(post):
    try:
        food_stuff = FoodStuff.objects.get( name=post['food_stuff'] )
    except ObjectDoesNotExist:
        food_stuff = FoodStuff( name=post['food_stuff'] )

    for food_type in (  'fruit', 'dairy', 'water', 'junk',
                        'veg', 'protein', 'startch', 'unknown'):
        if post[food_type] == u'':
            setattr(food_stuff, food_type, 0)
        else:
            setattr(food_stuff, food_type, int(float(post[food_type])) )

    food_stuff.name = post['food_stuff']
    food_stuff.ingredients = post['ingredients']
    food_stuff.save()


def delete_food_stuff(request):
    try:
        food_stuff = FoodStuff.objects.get( name=request.POST['food_stuff'] )
    except ObjectDoesNotExist:
        pass
    else:
        food_stuff.delete()

    return HttpResponseRedirect( reverse('home') )
