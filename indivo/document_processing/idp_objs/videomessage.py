from indivo.lib import iso8601
from indivo.models import VideoMessage

XML = 'xml'
DOM = 'dom'

class IDP_VideoMessage:

  def post_data(self, fileId=None, 
                      storageType=None, 
                      subject=None, 
                      from_str=None,
                      dateTimeRecorded=None,
                      dateTimeSent=None):

    """
    SZ: More error checking needs to be performed in this method
    """

    try:
     
      if dateTimeRecorded:
        dateTimeRecorded = iso8601.parse_date(dateTimeRecorded)
      if dateTimeSent:
        dateTimeSent = iso8601.parse_date(dateTimeSent)

      videomessage_obj = VideoMessage.objects.create( 
                      file_id=fileId,
                      storage_type=storageType,   
                      subject=subject, 
                      from_str=from_str,
                      datetime_recorded=dateTimeRecorded,
                      datetime_sent=dateTimeSent)

      return videomessage_obj
    except Exception, e:
      raise ValueError("problem processing medicationscheduleitem report " + str(e))
