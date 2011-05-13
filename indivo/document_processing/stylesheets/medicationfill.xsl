<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:MedicationOrder">
    <facts>
      <fact>
        <name><xsl:value-of select='indivodoc:name/text()' /></name>
        <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
        <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
        <name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
        <filledBy><xsl:value-of select='indivodoc:filledBy/text()' /></filledBy>
        <dateFilled><xsl:value-of select='indivodoc:dateFilled/text()' /></dateFilled>
        <dateOrdered><xsl:value-of select='indivodoc:dateOrdered/text()' /></dateOrdered>
        <xsl:apply-templates select='indivodoc:amountFilled' />
        <xsl:if test="indivodoc:ndc">
          <ndc><xsl:value-of select='indivodoc:ndc/text()' /></ndc>
          <ndc_type><xsl:value-of select='indivodoc:ndc/@type' /></ndc_type>
          <ndc_value><xsl:value-of select='indivodoc:ndc/@value' /></ndc_value>
          <ndc_abbrev><xsl:value-of select='indivodoc:ndc/@abbrev' /></ndc_abbrev>
        </xsl:if>
        <xsl:if test="indivodoc:fillSequenceNumber">
          <fillSequenceNumber><xsl:value-of select='indivodoc:fillSequenceNumber/text()' /></fillSequenceNumber>
        </xsl:if>
        <xsl:if test="indivodoc:lotNumber">
          <lotNumber><xsl:value-of select='indivodoc:lotNumber/text()' /></lotNumber>
        </xsl:if>
        <xsl:if test="indivodoc:refillsRemaining">
          <refillsRemaining><xsl:value-of select='indivodoc:refillsRemaining/text()' /></refillsRemaining>
        </xsl:if>
        <xsl:if test="indivodoc:instructions">
          <instructions><xsl:value-of select='indivodoc:instructions/text()' /></instructions>
        </xsl:if>        
      </fact>
    </facts>
  </xsl:template>

  <xsl:template match="indivodoc:amountFilled">
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
