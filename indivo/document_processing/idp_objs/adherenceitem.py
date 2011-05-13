from indivo.lib import iso8601
from indivo.models import AdherenceItem

XML = 'xml'
DOM = 'dom'

class IDP_AdherenceItem:

  def post_data(self, 
    name=None,
    name_type=None,
    name_value=None,
    name_abbrev=None,
    reportedBy=None,
    dateTimeReported=None,
    adherence=None,
    nonadherenceReason=None):

    """
    SZ: More error checking needs to be performed in this method
    """

    try:
      """
      Elliot: 3/4 changed parse_utc_date to parse_date
      """
      if dateTimeReported:
        dateTimeReported = iso8601.parse_date(dateTimeReported)

      print "creating adherence obj"
      print "Reported By: " + str(reportedBy)
      adherenceitem_obj = AdherenceItem.objects.create(   
                            name=name,
                            name_type=name_type,
                            name_value=name_value,
                            name_abbrev=name_abbrev,
                            reported_by=reportedBy,
                            datetime_reported=dateTimeReported,
                            adherence=adherence,
                            nonadherence_reason=nonadherenceReason)


      print "object created"
      return adherenceitem_obj
    except Exception, e:
      print str(e)
      raise ValueError("problem processing medicationscheduleitem report " + str(e))
