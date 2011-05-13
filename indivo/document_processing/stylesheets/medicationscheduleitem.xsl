<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:MedicationScheduleItem">
    <facts>
      <fact>
        <xsl:if test="indivodoc:name">
	        <name><xsl:value-of select='indivodoc:name/text()' /></name>
	        <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
	        <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
	        <name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
        </xsl:if>
        <scheduledBy><xsl:value-of select='indivodoc:scheduledBy/text()' /></scheduledBy>
        <dateTimeScheduled><xsl:value-of select='indivodoc:dateTimeScheduled/text()' /></dateTimeScheduled>
        <xsl:apply-templates select='indivodoc:dose' /> 
        <xsl:if test="indivodoc:instructions">
          <instructions><xsl:value-of select='indivodoc:instructions/text()' /></instructions>
        </xsl:if>        
      </fact>
    </facts>
  </xsl:template>


  <xsl:template match="indivodoc:dose">
    <xsl:if test="indivodoc:textValue">
      <dose_textvalue><xsl:value-of select='indivodoc:textValue/text()' /></dose_textvalue>
    </xsl:if>
    <xsl:if test="indivodoc:value">
      <dose_value><xsl:value-of select='indivodoc:value/text()' /></dose_value>
    </xsl:if>
    <xsl:if test="indivodoc:unit">
      <dose_unit>
        <xsl:value-of select='indivodoc:unit/text()' />
      </dose_unit>
      <dose_unit_type><xsl:value-of select='indivodoc:unit/@type' /></dose_unit_type>
      <dose_unit_value><xsl:value-of select='indivodoc:unit/@value' /></dose_unit_value>
      <dose_unit_abbrev><xsl:value-of select='indivodoc:unit/@abbrev' /></dose_unit_abbrev>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
