from indivo.lib import iso8601
from indivo.models import ScheduleGroup

XML = 'xml'
DOM = 'dom'

class IDP_ScheduleGroup:

  def post_data(self, scheduledBy=None, 
                      dateTimeScheduled=None, 
                      dateTimeStart=None, 
                      dateTimeEnd=None,
                      frequency=None,
                      frequency_type=None,
                      frequency_value=None,
                      frequency_abbrev=None,
                      dateTimeUntil=None,
                      count=None):

    """
    SZ: More error checking needs to be performed in this method
    """

    try:
      """
      Elliot: 3/4 changed parse_utc_date to parse_date
      """
      if dateTimeScheduled:
        dateTimeScheduled = iso8601.parse_date(dateTimeScheduled)
      if dateTimeStart:
        dateTimeStart = iso8601.parse_date(dateTimeStart)
      if dateTimeEnd:
        dateTimeEnd = iso8601.parse_date(dateTimeEnd)
      if dateTimeUntil:
        dateTimeUntil = iso8601.parse_date(dateTimeUntil)

      schedulegroup_obj = ScheduleGroup.objects.create(   
                      scheduled_by=scheduledBy, 
                      datetime_scheduled=dateTimeScheduled, 
                      datetime_start=dateTimeStart, 
                      datetime_end=dateTimeEnd,
                      frequency=frequency,
                      frequency_type=frequency_type,
                      frequency_value=frequency_value,
                      frequency_abbrev=frequency_abbrev,
                      datetime_until=dateTimeUntil,
                      count=count)

      return schedulegroup_obj
    except Exception, e:
      raise ValueError("problem processing medicationscheduleitem report " + str(e))
