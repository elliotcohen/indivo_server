<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:Medication">
    <facts>
      <fact>
        <scheduledBy><xsl:value-of select='indivodoc:scheduledBy/text()' /></scheduledBy>
        <dateTimeScheduled><xsl:value-of select='indivodoc:dateTimeScheduled/text()' /></dateTimeScheduled>
        <dateTimeStart><xsl:value-of select='indivodoc:dateTimeStart/text()' /></dateTimeStart>
        <xsl:if test="indivodoc:dateTimeEnd">
          <dateTimeEnd><xsl:value-of select='indivodoc:dateTimeEnd/text()' /></dateTimeEnd>
        </xsl:if>
        <xsl:if test="indivodoc:recurrenceRule">
          <xsl:apply-templates select='indivodoc:recurrenceRule' />
        </xsl:if>
      </fact>
    </facts>
  </xsl:template>
  <xsl:template match="indivodoc:recurrenceRule">
		<xsl:if test="indivodoc:frequency">
			<frequency><xsl:value-of select='indivodoc:frequency/text()' /></frequency>
			<frequency_type><xsl:value-of select='indivodoc:frequency/@type' /></frequency_type>
			<frequency_value><xsl:value-of select='indivodoc:frequency/@value' /></frequency_value>
			<frequency_abbrev><xsl:value-of select='indivodoc:frequency/@abbrev' /></frequency_abbrev>
		</xsl:if>
    <xsl:if test="indivodoc:dateTimeUntil">
      <dateTimeUntil><xsl:value-of select='indivodoc:dateTimeUntil/text()' /></dateTimeUntil>
    </xsl:if>  
    <xsl:if test="indivodoc:count">
      <count><xsl:value-of select='indivodoc:count/text()' /></count>
    </xsl:if>  
  </xsl:template>
</xsl:stylesheet>
