from django.shortcuts import get_object_or_404, render
from django import forms
from models import FoodEntry, FoodStuff
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def test(request):
    return render(request, 'food/food_etnry.html')


def home(request):
    food_entries = FoodEntry.objects.all()
    food_stuffs  = FoodStuff.objects.all()
    return render(request, 
                  'food/home', 
                  {'food_entries': FoodEntry.objects.all(),
                   'food_stuffs' : FoodStuff.objects.all() } )

def new_food_entry(request):
    if request.method != 'POST':
        return render(  request, 'food/food_etnry.html',
                       {'food_stuffs': FoodStuff.objects.all() }   )

    persentages={}    
    for food_type in (  'fruit', 'dairy','water','junk',
                        'veg', 'protein', 'startch', 'unknown'):
        try:
            persentages[food_type] = int(float(request.POST[food_type]))
        except ValueError:
            persentages[food_type] = 0
    
    food_entry=FoodEntry(**persentages)
    food_entry.amount = request.POST['amount']
    food_entry.quantity = float(request.POST['quantity'])
    food_entry.description = request.POST['description']
    food_entry.save()

    return HttpResponseRedirect( reverse('home') )



def edit_food_entry(request, id):
    if request.method != 'POST':
        food_entry = get_object_or_404(FoodEntry, pk=id)
        return render(  request, 'food/food_etnry.html',
                       {'food_stuffs': FoodStuff.objects.all(), 
                        'food_entry': food_entry                }   )   


def delete_food_entry(request, id):
    food_entry = get_object_or_404(FoodEntry, pk=id)
    food_entry.delete()
    return HttpResponseRedirect( reverse('home') )
    








class FoodEntryForm(forms.ModelForm):
    class Meta:
        model=FoodEntry

    description = forms.CharField(max_length=500, widget=forms.Textarea)



class FoodStuffForm(forms.ModelForm):
    class Meta:
        model=FoodStuff




def edit(request, Class, ClassForm, id, template='plots/form_template'):
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


'''
def new_food_entry(request):
    return new(request, FoodEntry, FoodEntryForm, 'food_entry')

def edit_food_entry(request, id):
    return edit(request, FoodEntry, FoodEntryForm, id)
'''

def new_food_stuff(request):
    return new(request, FoodStuff, FoodStuffForm, 'food_stuff')

def edit_food_stuff(request, id):
    return edit(request, FoodStuff, FoodStuffForm, id)
