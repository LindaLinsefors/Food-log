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
    

    fruit = models.SmallIntegerField(validators=[validate_non_neg])
    dairy = models.SmallIntegerField(validators=[validate_non_neg])
    water = models.SmallIntegerField(validators=[validate_non_neg])
    junk  = models.SmallIntegerField(validators=[validate_non_neg])
    veg   = models.SmallIntegerField(validators=[validate_non_neg])
    protein = models.SmallIntegerField(validators=[validate_non_neg])
    startch = models.SmallIntegerField(validators=[validate_non_neg])
    unknown = models.SmallIntegerField(validators=[validate_non_neg])   

    def __str__(self):
        return self.name
    def __unicode__(self):          # for Python 2 
        return unicode(self.name)



class FoodEntry(models.Model):
    class Meta:
        ordering = ['date']
        #verbose_name_plural = _('food entries')

    date = models.DateTimeField()
    amount_text = models.CharField(max_length=20)
    amount_value = models.FloatField(validators=validate_poss)
    description = models.CharField(max_length=500)

    fruit = models.SmallIntegerField(validators=[validate_non_neg])
    dairy = models.SmallIntegerField(validators=[validate_non_neg])
    water = models.SmallIntegerField(validators=[validate_non_neg])
    junk  = models.SmallIntegerField(validators=[validate_non_neg])
    veg   = models.SmallIntegerField(validators=[validate_non_neg])
    protein = models.SmallIntegerField(validators=[validate_non_neg])
    startch = models.SmallIntegerField(validators=[validate_non_neg])
    unknown = models.SmallIntegerField(validators=[validate_non_neg])    

    def __str__(self):
        return str(self.date) + ': ' + self.amount_text
    def __unicode__(self):          # for Python 2 
        return unicode(self.date) + u': ' + unicode(self.amount_text)




