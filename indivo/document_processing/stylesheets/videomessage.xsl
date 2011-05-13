<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:Medication">
    <facts>
      <fact>
        <fileId><xsl:value-of select='indivodoc:fileId/text()' /></fileId>
        <storageType><xsl:value-of select='indivodoc:storageType/text()' /></storageType>
        <subject><xsl:value-of select='indivodoc:subject/text()' /></subject>
        <from_str><xsl:value-of select='indivodoc:from/text()' /></from_str>
        <dateTimeRecorded><xsl:value-of select='indivodoc:dateTimeRecorded/text()' /></dateTimeRecorded>
        <dateTimeSent><xsl:value-of select='indivodoc:dateTimeSent/text()' /></dateTimeSent>
      </fact>
    </facts>
  </xsl:template>
</xsl:stylesheet>


