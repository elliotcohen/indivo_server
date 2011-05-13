from indivo.lib import iso8601
from indivo.models import MedicationScheduleItem

XML = 'xml'
DOM = 'dom'

class IDP_MedicationScheduleItem:

  def post_data(self, name=None,
                      name_type=None,
                      name_value=None,
                      name_abbrev=None,
                      dose_unit=None,
                      dose_textvalue=None,
                      dose_value=None,
                      dose_unit_type=None, 
                      dose_unit_value=None,
                      dose_unit_abbrev=None,
											instructions=None,
											dateTimeScheduled=None,
                      scheduledBy=None):

    """
    SZ: More error checking needs to be performed in this method
    """

    try:
      if dateTimeScheduled:
        """
        Elliot: 3/4 changed parse_utc_date to parse_date to handle XML:datetime
        """
        dateTimeScheduled = iso8601.parse_date(dateTimeScheduled)

      medicationscheduleitem_obj = MedicationScheduleItem.objects.create(   
                      name=name,
                      name_type=name_type,
                      name_value=name_value,
                      name_abbrev=name_abbrev,
                      dose_unit=dose_unit,
                      dose_textvalue=dose_textvalue,
                      dose_value=dose_value,
                      dose_unit_type=dose_unit_type, 
                      dose_unit_value=dose_unit_value,
                      dose_unit_abbrev=dose_unit_abbrev,
											instructions=instructions,
											datetime_scheduled=dateTimeScheduled,
                      scheduled_by=scheduledBy)

      return medicationscheduleitem_obj
    except Exception, e:
      raise ValueError("problem processing medicationscheduleitem report " + str(e))
