<?xml version='1.0' encoding='ISO-8859-1'?>
<xsl:stylesheet version = '1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform' xmlns:indivodoc="http://indivo.org/vocab/xml/documents#"> 
  <xsl:output method = "xml" indent = "yes" />  
  <xsl:template match="indivodoc:Medication">
    <facts>
      <fact>
        <xsl:if test="indivodoc:name">
	        <name><xsl:value-of select='indivodoc:name/text()' /></name>
	        <name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
	        <name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
	        <name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
        </xsl:if>
        <orderType><xsl:value-of select='indivodoc:orderType/text()' /></orderType>
        <orderedBy><xsl:value-of select='indivodoc:orderBy/text()' /></orderedBy>
        <dateTimeOrdered><xsl:value-of select='indivodoc:dateTimeOrdered/text()' /></dateTimeOrdered>
        <dateTimeExpires><xsl:value-of select='indivodoc:dateTimeExpires/text()' /></dateTimeExpires>
        <indication><xsl:value-of select='indivodoc:indication/text()' /></indication>
        <xsl:for-each select='indivodoc:activeIngredient'>
          <xsl:apply-templates select='indivodoc:activeIngredient' />
        </xsl:for-each>
        <xsl:apply-templates select='indivodoc:dose' /> 
        <xsl:if test="indivodoc:form">
	        <form><xsl:value-of select='indivodoc:form/text()' /></form>
	        <form_type><xsl:value-of select='indivodoc:form/@type' /></form_type>
	        <form_value><xsl:value-of select='indivodoc:form/@value' /></form_value>
	        <form_abbrev><xsl:value-of select='indivodoc:form/@abbrev' /></form_abbrev>
        </xsl:if>
        <xsl:if test="indivodoc:route">
          <route><xsl:value-of select='indivodoc:route/text()' /></route>
          <route_type><xsl:value-of select='indivodoc:route/@type' /></route_type>
          <route_value><xsl:value-of select='indivodoc:route/@value' /></route_value>
          <route_abbrev><xsl:value-of select='indivodoc:route/@abbrev' /></route_abbrev>
        </xsl:if>
        <xsl:if test="indivodoc:frequency">
          <frequency><xsl:value-of select='indivodoc:frequency/text()' /></frequency>
          <frequency_type><xsl:value-of select='indivodoc:frequency/@type' /></frequency_type>
          <frequency_value><xsl:value-of select='indivodoc:frequency/@value' /></frequency_value>
          <frequency_abbrev><xsl:value-of select='indivodoc:frequency/@abbrev' /></frequency_abbrev>
        </xsl:if>
        <xsl:apply-templates select='indivodoc:amountOrdered' />
        <xsl:if test='indivodoc:refills'>
          <refills><xsl:value-of select='indivodoc:refills/text()' /></refills>
        </xsl:if>
        <xsl:if test='indivodoc:substitutionPermitted'>
          <substitutionPermitted><xsl:value-of select='indivodoc:substitutionPermitted/text()' /></substitutionPermitted>
        </xsl:if>
        <xsl:if test='indivodoc:instructions'>
          <instructions><xsl:value-of select='indivodoc:instructions/text()' /></instructions>
        </xsl:if>
        <xsl:if test='indivodoc:dateTimeStarted'>
          <dateTimeStarted><xsl:value-of select='indivodoc:dateTimeStarted/text()' /></dateTimeStarted>
        </xsl:if>
        <xsl:if test='indivodoc:dateTimeStopped'>
          <dateTimeStopped><xsl:value-of select='indivodoc:dateTimeStopped/text()' /></dateTimeStopped>
        </xsl:if>  
        <xsl:if test='indivodoc:reasonStopped'>
          <reasonStopped><xsl:value-of select='indivodoc:reasonStopped/text()' /></reasonStopped>
        </xsl:if>  
      </fact>
    </facts>
  </xsl:template>



  <xsl:template match="indivodoc:activeIngredient">
		<xsl:if test="indivodoc:name">
			<name><xsl:value-of select='indivodoc:name/text()' /></name>
			<name_type><xsl:value-of select='indivodoc:name/@type' /></name_type>
			<name_value><xsl:value-of select='indivodoc:name/@value' /></name_value>
			<name_abbrev><xsl:value-of select='indivodoc:name/@abbrev' /></name_abbrev>
		</xsl:if>  
		<xsl:apply-templates select='indivodoc:strength' />  
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
  <xsl:template match="indivodoc:amountOrdered">
    <xsl:if test="indivodoc:textValue">
      <amountOrdered_textvalue><xsl:value-of select='indivodoc:textValue/text()' /></amountOrdered_textvalue>
    </xsl:if>
    <xsl:if test="indivodoc:value">
      <amountOrdered_value><xsl:value-of select='indivodoc:value/text()' /></amountOrdered_value>
    </xsl:if>
    <xsl:if test="indivodoc:unit">
      <amountOrdered_unit>
        <xsl:value-of select='indivodoc:unit/text()' />
      </amountOrdered_unit>
      <amountOrdered_unit_type><xsl:value-of select='indivodoc:unit/@type' /></amountOrdered_unit_type>
      <amountOrdered_unit_value><xsl:value-of select='indivodoc:unit/@value' /></amountOrdered_unit_value>
      <amountOrdered_unit_abbrev><xsl:value-of select='indivodoc:unit/@abbrev' /></amountOrdered_unit_abbrev>
    </xsl:if>
  </xsl:template>

  <xsl:template match="indivodoc:strength">
    <xsl:if test="indivodoc:textValue">
      <strength_textvalue><xsl:value-of select='indivodoc:textValue/text()' /></strength_textvalue>
    </xsl:if>
    <xsl:if test="indivodoc:value">
      <strength_value>
        <xsl:value-of select='indivodoc:value/text()' />
      </strength_value>
    </xsl:if>
    <xsl:if test="indivodoc:unit">
      <strength_unit>
        <xsl:value-of select='indivodoc:unit/text()' />
      </strength_unit>
      <strength_unit_type>
        <xsl:value-of select='indivodoc:unit/@type' />
      </strength_unit_type>
      <strength_unit_value>
        <xsl:value-of select='indivodoc:unit/@value' />
      </strength_unit_value>
      <strength_unit_abbrev>
        <xsl:value-of select='indivodoc:unit/@abbrev' />
      </strength_unit_abbrev>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
