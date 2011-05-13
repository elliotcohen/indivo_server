"""
Indivo Model for Medication
"""

from fact import Fact
from django.db import models
from django.conf import settings

class Medication(Fact):
  datetime_started = models.DateField(null=True)
  datetime_stopped = models.DateField(null=True)
  order_type=models.CharField(null=True, max_length=200)
  ordered_by=models.CharField(null=True, max_length=200)
  datetime_ordered=models.DateField(null=True)
  datetime_expires=models.DateField(null=True)
  indication=models.CharField(null=True, max_length=200)
  name=models.CharField(null=True, max_length=200)
  name_type = models.CharField(max_length=200, null=True)
  name_value = models.CharField(max_length=200, null=True)
  name_abbrev = models.CharField(max_length=20, null=True)
  activeingredient_name = models.CharField(null=True, max_length=200)
  activeingredient_name_type = models.CharField(max_length=200, null=True)
  activeingredient_name_value = models.CharField(max_length=200, null=True)
  activeingredient_name_abbrev = models.CharField(max_length=20, null=True)
  form = models.CharField(null=True, max_length=200)
  form_type = models.CharField(null=True, max_length=200)
  form_value = models.CharField(null=True, max_length=200)
  form_abbrev = models.CharField(null=True, max_length=20)
  dose_textvalue = models.CharField(null=True, max_length=100)
  dose_value = models.CharField(null=True, max_length=20)
  dose_unit = models.CharField(null=True, max_length=40)
  dose_unit_type = models.CharField(null=True, max_length=200)
  dose_unit_value = models.CharField(null=True, max_length=20)
  dose_unit_abbrev = models.CharField(null=True, max_length=20)
  route = models.CharField(null=True, max_length=200)
  route_type = models.CharField(null=True, max_length=200)
  route_value = models.CharField(null=True, max_length=200)
  route_abbrev = models.CharField(null=True, max_length=20)
  activeingredient_strength_textvalue = models.CharField(null=True, max_length=100)
  activeingredient_strength_value = models.CharField(null=True, max_length=20)
  activeingredient_strength_unit = models.CharField(null=True, max_length=40)
  activeingredient_strength_unit_type = models.CharField(null=True, max_length=200)
  activeingredient_strength_unit_value = models.CharField(null=True, max_length=100)
  activeingredient_strength_unit_abbrev = models.CharField(null=True, max_length=20)
  frequency = models.CharField(null=True, max_length=100)
  frequency_type = models.CharField(null=True, max_length=200)
  frequency_value = models.CharField(null=True, max_length=20)
  frequency_abbrev = models.CharField(null=True, max_length=20)

  amount_ordered_unit = models.CharField(null=True, max_length=40)
  amount_ordered_textvalue = models.CharField(null=True, max_length=100)
  amount_ordered_value = models.CharField(null=True, max_length=20)
  amount_ordered_unit_type = models.CharField(null=True, max_length=200) 
  amount_ordered_unit_value = models.CharField(null=True, max_length=100)
  amount_ordered_unit_abbrev = models.CharField(null=True, max_length=20)
  refills = models.IntegerField(null=True)
  substitution_permitted = models.NullBooleanField()
  instructions = models.TextField(null=True)
  reason_stopped = models.TextField(null=True)


  # written as days
  prescription_duration = models.CharField(null=True, max_length=100)
  prescription_refill_info = models.TextField(null=True)
  prescription_instructions = models.TextField(null=True)

  def __unicode__(self):
    return 'Medication %s' % self.id

