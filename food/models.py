from django.db import models
from django import forms

# Create your models here.


def validate_non_neg(value):
    if value < 0:
        raise ValidationError(u'%s in neggative' % value)

def validate_poss(value):
    if value <= 0:
        raise ValidationError(u'%s is zero or neggative' % value)

NonNegIntField = models.SmallIntegerField(validators=[validate_non_neg])


class FoodStuff(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=50, unique=True)
    
    fruit = NonNegIntField
    dairy = NonNegIntField
    water = NonNegIntField
    junk  = NonNegIntField
    veg   = NonNegIntField
    protein = NonNegIntField
    startch = NonNegIntField
    unknown = NonNegIntField   

    def __str__(self):
        return self.name
    def __unicode__(self):          # for Python 2 
        return unicode(self.name)



class FoodEntry(models.Model):
    class Meta:
        ordering = ['date']

    date = models.DateTimeField()
    amount_text = models.CharField(max_length=20)
    amount_value = models.FloatField(validators=validate_poss)
    description = models.CharField(max_length=500)

    fruit = NonNegIntField
    dairy = NonNegIntField
    water = NonNegIntField
    junk  = NonNegIntField
    veg   = NonNegIntField
    protein = NonNegIntField
    startch = NonNegIntField
    unknown = NonNegIntField   

    def __str__(self):
        return str(self.date) + ': ' + self.amount_text
    def __unicode__(self):          # for Python 2 
        return unicode(self.date) + u': ' + unicode(self.amount_text)




