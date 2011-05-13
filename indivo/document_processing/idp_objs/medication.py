from indivo.lib import iso8601
from indivo.models import Medication

XML = 'xml'
DOM = 'dom'

class IDP_Medication:

  def post_data(self, orderType=None,
											orderedBy=None,
											dateTimeOrdered=None,
											dateTimeExpires=None,
											indication=None,
                      name=None,
                      name_type=None,
                      name_value=None,
                      name_abbrev=None,
                      form=None,
                      form_type=None,
                      form_value=None,
                      form_abbrev=None,
                      activeIngredient_name=None,
                      activeIngredient_name_type=None,
                      activeIngredient_name_value=None,
                      activeIngredient_name_abbrev=None,
                      dose_unit=None,
                      dose_textvalue=None,
                      dose_value=None,
                      dose_unit_type=None, 
                      dose_unit_value=None,
                      dose_unit_abbrev=None,
                      route=None,
                      route_type=None,
                      route_value=None,
                      route_abbrev=None,
                      activeIngredient_strength_value=None,
                      activeIngredient_strength_textvalue=None,
                      activeIngredient_strength_unit=None,
                      activeIngredient_strength_unit_type=None,
                      activeIngredient_strength_unit_value=None,
                      activeIngredient_strength_unit_abbrev=None,
                      frequency=None,
                      frequency_type=None,
                      frequency_value=None,
                      frequency_abbrev=None,
                      amountOrdered_unit=None,
                      amountOrdered_textvalue=None,
                      amountOrdered_value=None,
                      amountOrdered_unit_type=None, 
                      amountOrdered_unit_value=None,
                      amountOrdered_unit_abbrev=None,
											refills=None,
											substitutionPermitted=None,
											instructions=None,
											dateTimeStarted=None,
											dateTimeStopped=None,
											reasonStopped=None):

    """
    SZ: More error checking needs to be performed in this method
    """
    try:
      if dateTimeStarted:
        """
        Elliot: 3/4 changed parse_utc_date to parse_date as it more correctly maps to the XML component.
        """
        dateTimeStarted = iso8601.parse_date(dateTimeStarted)

      if dateTimeStopped:
        dateTimeStopped = iso8601.parse_date(dateTimeStopped)

      if dateTimeOrdered:
        dateTimeOrdered = iso8601.parse_date(dateTimeOrdered)
      if dateTimeExpires:
        dateTimeExpires = iso8601.parse_date(dateTimeExpires)

      medication_obj = Medication.objects.create(   datetime_started=dateTimeStarted,
  																				          datetime_stopped=dateTimeStopped,
                                                    order_type=orderType,
                                                    ordered_by=orderedBy,
                                                    datetime_ordered=dateTimeOrdered,
	                                                  datetime_expires=dateTimeExpires,
	                                                  indication=indication,
                                                    name=name,
                                                    name_type=name_type,
                                                    name_value=name_value,
                                                    name_abbrev=name_abbrev,
                                                    activeingredient_name=activeIngredient_name,
                                                    activeingredient_name_type=activeIngredient_name_type,
                                                    activeingredient_name_value=activeIngredient_name_value,
                                                    activeingredient_name_abbrev=activeIngredient_name_abbrev,
                                                    form=form,
                                                    form_type=form_type,
                                                    form_value=form_value,
                                                    form_abbrev=form_abbrev,
                                                    dose_textvalue=dose_textvalue,
                                                    dose_value=dose_value,
                                                    dose_unit=dose_unit,
                                                    dose_unit_type=dose_unit_type,
                                                    dose_unit_value=dose_unit_value,
                                                    dose_unit_abbrev=dose_unit_abbrev,
                                                    route=route,
                                                    route_type=route_type,
                                                    route_value=route_value,
                                                    route_abbrev=route_abbrev,
                                                    activeingredient_strength_textvalue=activeIngredient_strength_textvalue,
                                                    activeingredient_strength_value=activeIngredient_strength_value,
                                                    activeingredient_strength_unit=activeIngredient_strength_unit,
                                                    activeingredient_strength_unit_type=activeIngredient_strength_unit_type,
                                                    activeingredient_strength_unit_value=activeIngredient_strength_unit_value,
                                                    activeingredient_strength_unit_abbrev=activeIngredient_strength_unit_abbrev,
                                                    frequency=frequency,
                                                    frequency_type=frequency_type,
                                                    frequency_value=frequency_value,
                                                    frequency_abbrev=frequency_abbrev,
                                                    amount_ordered_unit=amountOrdered_unit,
                                                    amount_ordered_textvalue=amountOrdered_textvalue,
                                                    amount_ordered_value=amountOrdered_value,
                                                    amount_ordered_unit_type=amountOrdered_unit_type,
                                                    amount_ordered_unit_value=amountOrdered_unit_value,
                                                    amount_ordered_unit_abbrev=amountOrdered_unit_abbrev,
	                                                  refills=refills,
	                                                  substitution_permitted=substitutionPermitted,
	                                                  instructions=instructions,
	                                                  reason_stopped=reasonStopped)

      return medication_obj
    except Exception, e:
      raise ValueError("problem processing medication report " + str(e))
