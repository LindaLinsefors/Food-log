from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.


def validate_percent(value):
    if value < 0 or value > 100:
        raise ValidationError(u'%s in neggative' % value)

def validate_poss(value):
    if value <= 0:
        raise ValidationError(u'%s is zero or neggative' % value)

NonNegIntField = models.SmallIntegerField(validators=[validate_percent])


class Food(models.Model):
    class Meta:
        abstract = True

    ingredients = models.CharField( max_length=500 )

    fruit = models.SmallIntegerField(validators=[validate_percent])
    dairy = models.SmallIntegerField(validators=[validate_percent])
    water = models.SmallIntegerField(validators=[validate_percent])
    junk  = models.SmallIntegerField(validators=[validate_percent])
    veg   = models.SmallIntegerField(validators=[validate_percent])
    protein = models.SmallIntegerField(validators=[validate_percent])
    startch = models.SmallIntegerField(validators=[validate_percent])
    unknown = models.SmallIntegerField(validators=[validate_percent])  


class FoodStuff(Food):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    def __unicode__(self):          # for Python 2 
        return unicode(self.name)


class FoodEntry(Food):
    #class Meta:
        #ordering = ['date']
        #verbose_name_plural = _('food entries')

    # date = models.DateTimeField( default=timezone.now() )
    amount = models.CharField( max_length=30 )
    quantity = models.FloatField( validators=validate_poss )
  
    food_stuff = models.CharField(max_length=50)
    
    def __str__(self):
        #return str(self.date) + ': ' + self.amount_text
        return str(self.food_stuff) + ', ' + str(self.amount)

    def __unicode__(self):          # for Python 2 
        #return unicode(self.date) + u': ' + unicode(self.amount_text)
        return unicode(self.food_stuff) + u', ' + unicode(self.amount) 




