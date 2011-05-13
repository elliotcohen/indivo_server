"""
Indivo Views -- Medication Order
"""

from django.http import HttpResponseBadRequest
from indivo.lib.view_decorators import *
from indivo.lib.utils import render_template, carenet_filter
from indivo.models import *
from reportutils import report_orderby_update


@marsloader
def medicationorder_list(request, limit, offset, status, order_by='created_at', record=None, carenet=None):
  """For 1:1 mapping of URLs to views. Calls _medication_list"""
  return _medicationorder_list(request, limit, offset, status, order_by, record, carenet)


@marsloader
def carenet_medicationorder_list(request, limit, offset, status, order_by='created_at', record=None, carenet=None):
  """For 1:1 mapping of URLs to views. Calls _medication_list"""
  return _medicationorder_list(request, limit, offset, status, order_by, record, carenet)


def _medicationorder_list(request, limit, offset, status, order_by='created_at', record=None, carenet=None):
  if carenet:
    record = carenet.record
  if not record:
    return HttpResponseBadRequest()

  processed_order_by = report_orderby_update(order_by)

  type_obj = DocumentSchema.objects.get(type='http://indivo.org/vocab/xml/documents#MedicationOrder')
  medicationorders = carenet_filter(carenet, Document.objects.filter(type=type_obj, replaced_by=None, record=record, status=status).order_by(processed_order_by)) 

  return render_template('reports/medicationorders', 
                          { 'medicationorders' : medicationorders[offset:offset+limit],
                            'trc' : len(medicationorders),
                            'limit' : limit,
                            'offset' : offset,
                            'order_by' : order_by
                          }, 
                          type="xml")
