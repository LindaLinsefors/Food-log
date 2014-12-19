from django.shortcuts import get_object_or_404, render
from django import forms

# Create your views here.


def home(request):
    food_entries = FoodEntry.objects.all()
    food_stuffs = FoodStuffs.objects.all()
    return render(request, 
                  'food/home.html', 
                  {'food_entries': FoodEntry.objects.all()
                   'food_stuffs' : FoodStuff.objects.all() } )


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model=FoodEntry

    description.widget=forms.Textarea



class FoodStuffForm(forms.ModelForm):
    class Meta:
        model=FoodStuff




def edit(request, Class, ClassForm, id template='plots/form_template'):
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



def new_food_entry(request):
    new(request, FoodEntry, FoodEntryForm, 'food_entry')

def edit_food_entry(request, id):
    edit(request, FoodEntry, FoodEntryForm, id)

def new_food_stuff(request):
    new(request, FoodStuff, FoodStuffForm, 'food_stuff')

def edit_food_entry(request, id):
    edit(request, FoodStuff, FoodStuffForm, id)
