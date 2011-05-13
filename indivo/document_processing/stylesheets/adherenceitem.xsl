<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:AdherenceItem">
    <facts>
      <fact>
        <xsl:if test="indivodoc:name">
	        <name><xsl:value-of select='indivodoc:name/text()' /></name>
	        <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
	        <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
	        <name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
        </xsl:if>
        <reportedBy><xsl:value-of select='indivodoc:reportedBy/text()' /></reportedBy>
        <dateTimeReported><xsl:value-of select='indivodoc:dateTimeReported/text()' /></dateTimeReported>
        <adherence><xsl:value-of select='indivodoc:adherence/text()' /></adherence>
        <nonadherenceReason><xsl:value-of select='indivodoc:nonadherenceReason/text()' /></nonadherenceReason>
      </fact>
    </facts>
  </xsl:template>
</xsl:stylesheet>


