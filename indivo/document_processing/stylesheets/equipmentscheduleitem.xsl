<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:EquipmentScheduleItem">
    <facts>
      <fact>
        <name><xsl:value-of select='indivodoc:name/text()' /></name>
        <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
        <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
        <name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
        <scheduledBy><xsl:value-of select='indivodoc:scheduledBy/text()' /></scheduledBy>
        <dateScheduled><xsl:value-of select='indivodoc:dateScheduled/text()' /></dateScheduled>
        <dateStart><xsl:value-of select='indivodoc:dateStart/text()' /></dateStart>
        <xsl:if test="indivodoc:dateEnd">
          <dateEnd><xsl:value-of select='indivodoc:dateEnd/text()' /></dateEnd>
        </xsl:if>
        <xsl:if test="indivodoc:recurrenceRule">
          <xsl:apply-templates select="indivodoc:recurrenceRule" />
        </xsl:if>
        <xsl:if test="indivodoc:instructions">
          <instructions><xsl:value-of select='indivodoc:instructions/text()' /></instructions>
        </xsl:if>        
      </fact>
    </facts>
  </xsl:template>

  <xsl:template match="indivodoc:recurrenceRule">
    <frequency><xsl:value-of select='indivodoc:frequency/text()' /></frequency>
    <frequency_type><xsl:value-of select='indivodoc:frequency/@type' /></frequency_type>
    <frequency_value><xsl:value-of select='indivodoc:frequency/@value' /></frequency_value>
    <frequency_abbrev><xsl:value-of select='indivodoc:frequency/@abbrev' /></frequency_abbrev>
    <xsl:if test="indivodoc:interval">
      <interval><xsl:value-of select='indivodoc:interval/text()' /></interval>
      <interval_type><xsl:value-of select='indivodoc:interval/@type' /></interval_type>
      <interval_value><xsl:value-of select='indivodoc:interval/@value' /></interval_value>
      <interval_abbrev><xsl:value-of select='indivodoc:interval/@abbrev' /></interval_abbrev>
    </xsl:if>
    <xsl:if test="indivodoc:dateUntil">
      <dateUntil><xsl:value-of select='indivodoc:dateUntil/text()' /></dateUntil>
    </xsl:if>
    <xsl:if test="indivodoc:count">
      <count><xsl:value-of select='indivodoc:count/text()' /></count>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
