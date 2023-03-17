from django.db import models
import datetime


class GDP(models.Model):

    # year= models.DateTimeField( null=True, blank=True)
    year = models.IntegerField(('year'))
    '''year = models.DateField(null=True, blank=True)
    year = models.IntegerField(_('year'), , default=current_year)'''
    gdp_usd = models.FloatField()

    def __str__(self):
        return f"{self.year} - {self.gdp_usd}  USD" 