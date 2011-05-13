"""
Indivo Model for Medication Schedule Item
"""

from fact import Fact
from django.db import models
from django.conf import settings

class MedicationScheduleItem(Fact):
  name = models.CharField(max_length=200)
  name_type = models.CharField(max_length=200, null=True)
  name_value = models.CharField(max_length=200, null=True)
  name_abbrev = models.CharField(max_length=20, null=True)
  dose_textvalue = models.CharField(null=True, max_length=100)
  dose_value = models.CharField(null=True, max_length=20)
  dose_unit = models.CharField(null=True, max_length=40)
  dose_unit_type = models.CharField(null=True, max_length=200)
  dose_unit_value = models.CharField(null=True, max_length=20)
  dose_unit_abbrev = models.CharField(null=True, max_length=20)
  instructions = models.TextField(null=True)
  datetime_scheduled = models.DateField(null=True)
  scheduled_by = models.CharField(max_length=200)

  def scheduled_actions():
    relationship = DocumentSchema.objects.get(type=DocumentSchema.expand_rel('ScheduledAction'))
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

