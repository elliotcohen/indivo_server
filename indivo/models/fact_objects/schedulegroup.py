"""
Indivo Model for ScheduleGroup
"""

from fact import Fact
from django.db import models
from django.conf import settings

class ScheduleGroup(Fact):
  scheduled_by = models.CharField(max_length=200) 
  datetime_scheduled = models.DateField(null=True) 
  datetime_start = models.DateField(null=True) 
  datetime_end = models.DateField(null=True)
  frequency = models.CharField(max_length=200)
  frequency_type = models.CharField(max_length=200, null=True)
  frequency_value = models.CharField(max_length=200, null=True)
  frequency_abbrev = models.CharField(max_length=20, null=True)
  datetime_until = models.DateField(null=True)
  count = models.IntegerField(null=True)

  def schedule_items(self):
    relationship = DocumentSchema.objects.get(type=DocumentSchema.expand_rel('ScheduleItem'))
    docs = Document.objects.filter(record=self.document.record,
                                   status=self.document.status,
                                   rels_as_doc_1__document_0__original=self.document.original_id, # doc is related to passed document
                                   rels_as_doc_1__relationship=relationship) # AND relation type is correct
    if len(docs):
      return docs
    else:
      return []

  def __unicode__(self):
    return 'Medication %s' % self.id

