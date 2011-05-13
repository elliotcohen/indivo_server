"""
Indivo Model for VideoMessage
"""

from fact import Fact
from django.db import models
from django.conf import settings

class VideoMessage(Fact):
  file_id=models.CharField(max_length=200)
  storage_type=models.CharField(max_length=200)   
  subject=models.CharField(max_length=200) 
  from_str=models.CharField(max_length=200)
  datetime_recorded=models.DateField(null=True)
  datetime_sent=models.DateField(null=True)

  def __unicode__(self):
    return 'Medication %s' % self.id

