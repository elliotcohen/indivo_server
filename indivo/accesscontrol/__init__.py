"""
Access Rule Initialization
"""
import sys
from accessfunc import *
from access_rule import AccessRule
from indivo.views import *

def load_access_rules():
  """
  Initializes the accesscontrol system by loading the access rules for the views
  """  
  # These are run after the paramloader middleware, which means kw_args have been
  # converted to Django models.
  # Thus, access_funcs should take 'record', 'carenet', 'account', etc. instead of
  # view_args, view_kwargs.
  #
  # The syntax for defining an access rule is:
  #
  # def access_type_name(principal, record, account, **unused_args):
  #   ...func here...
  # views = [view_func_1, view_func_2, ...]
  # AccessRule('Access Type Name', access_type_name, views)
  #
  # For consistency, name AccessRules after the name of the access function.
  # Note the unused_args parameter to the access function. This allows different
  # views with different kw_args to share access functions without throwing exceptions:
  # make sure to include it in every access function.


  # These view functions will always throw 403, as they are either not used in the API or unimplemented:
  # inactive_views = [get_id,
  #                   record_password_reset,
  #                   documents_delete,
  #                   record_inbox,
  #                   carenet_app_permissions] 

  
  # NO PERMISSIONS IN OLD SYSTEM
  views = [user_authorization] 

  # Top-level views
  def basic_access(principal, **unused_args):
    return principal.basicPrincipalRole()
  # WARNING: This gives request tokens and 'no-users' access to these. Is this a problem?
  views = [get_version, # no-users should have access. Should reqtokens?
           all_phas,
           pha] # should either have access?
  AccessRule('Basic Access', basic_access, views)

  # Account-related views
  def account_management_owner(principal, account, **unused_args):
    return principal.isType('MachineApp') or principal.isSame(account)
  views = [account_info,
           account_info_set,
           account_forgot_password,
           account_username_set]
  AccessRule('Account Management Owner', account_management_owner, views)

  def account_management_by_record(principal, record, **unused_args):
    return full_control(principal, record) \
        or principal.isType('MachineApp')
  views = [pha_record_delete]
  AccessRule('Account Management By Record', account_management_by_record, views)

  def account_management_no_admin_app(principal, account, **unused_args):
    return principal.isSame(account)
  views = [account_password_change,
           record_list,
           account_inbox,
           account_inbox_message,
           account_inbox_message_attachment_accept,
           account_message_archive,
           account_notifications,
           account_permissions]
  AccessRule('Account Management No Admin App', 
             account_management_no_admin_app, views)           

  def account_management_admin_app_only(principal, **unused_args):
    return principal.isType('MachineApp')
  views = [account_create, 
           account_search, 
           account_authsystem_add,
           account_check_secrets,
           account_resend_secret,
           account_reset,
           account_set_state,
           account_password_set,
           account_primary_secret,
           record_create,
           record_create_ext,
           record_set_owner,
           record_pha_setup,
           account_secret,
           account_send_message,
           carenet_create] # Is this account Management? Why can only Admins create?
  AccessRule('Account Management Admin App Only', 
             account_management_admin_app_only, views)

  def chrome_app_priveleges(principal, **unused_args):
    return principal.isType('chrome')
  views = [session_create,
           account_initialize]
  AccessRule('Chrome App Priveleges', chrome_app_priveleges, views)

  # PHA-related views
  def app_specific_priveleges(principal, pha, **unused_args):
    return pha_app_access(principal, pha)
  views = [pha_delete]
  AccessRule('App Specific Priveleges', app_specific_priveleges, views)

  # Oauth-related views
  def account_for_oauth(principal, **unused_args):
    return principal.isType('Account')
  views = [request_token_claim, 
           request_token_info,
           surl_verify]
  AccessRule('Account For Oauth', account_for_oauth, views)

  def app_for_oauth(principal, **unused_args):
    return principal.isType('PHA')
  views = [request_token]
  AccessRule('App For Oauth', app_for_oauth, views)

  def reqtoken_for_oauth(principal, **unused_args):
    return principal.isType('ReqToken')
  views = [exchange_token]
  AccessRule('Reqtoken For Oauth', reqtoken_for_oauth, views)

  def accesstoken_for_oauth(principal, **unused_args):
    return principal.isType('AccessToken')
  views = [get_long_lived_token] # IS THIS OUTDATED?
  AccessRule('Accesstoken For Oauth', accesstoken_for_oauth, views)

  def token_approval_admin(principal, reqtoken, **unused_args):
    carenet_reqtoken = False
    carenet = reqtoken.carenet
    if carenet and reqtoken:
      carenet_reqtoken = principal.isInCarenet(carenet) and reqtoken.pha.isInCarenet(carenet)
    token_admin = full_control(principal, reqtoken.record)
    return carenet_reqtoken or token_admin
  views = [request_token_approve]
  AccessRule('Token Approval Admin', token_approval_admin, views)

  # Carenet-related views
  def carenet_read_access(principal, carenet, **unused_args):
    return full_control(principal, carenet.record) \
        or principal.isInCarenet(carenet) \
        or principal.isType('MachineApp')
  views = [carenet_account_list, # WHY CAN'T A PHA DO THESE? (they should)
           carenet_apps_list]
  AccessRule('Carenet Read Access', carenet_read_access, views)

  # Should admins do these? Why can't record-level PHAs do these? define more clearly
  def carenet_control(principal, carenet, **unused_args):
    return full_control(principal, carenet.record)
  views = [carenet_account_create,
           carenet_account_delete,
           carenet_apps_create,
           carenet_apps_delete,
           carenet_document_placement,
           carenet_document_delete,
           document_carenets]
  AccessRule('Carenet Control', carenet_control, views)

  def carenet_read_all_access(principal, carenet, account, **unused_args):
    return (pha_carenet_access(principal, carenet) and principal.effective_principal.isSame(account)) \
        or full_control(principal, carenet.record) \
        or (principal.isInCarenet(carenet) and principal.isSame(account)) \
        or principal.isType('MachineApp')
  views = [carenet_account_permissions]
  AccessRule('Carenet Read All Access', carenet_read_all_access, views)

  # Record-related views

  def record_limited_access(principal, record, **unused_args):
    return full_control(principal, record) \
        or principal.isType('MachineApp')
  views = [record_phas,
           record_pha,
           record_get_owner,
           carenet_list]
  AccessRule('Record Limited Access', record_limited_access, views)

  def record_access(principal, record, **unused_args):
    return pha_record_access(principal, record) \
        or full_control(principal, record) \
        or principal.createdRecord(record) # Admins can only view records they created
  views = [record]
  AccessRule('Record Access', record_access, views)

  def record_full_admin(principal, record, **unused_args):
    return principal.ownsRecord(record) \
        or principal.isType('MachineApp')
  # Decision: PHAs shouldn't be allowed to manipulate sharing, at least not yet.
  views = [record_shares,
           record_share_add,
           record_share_delete]
  AccessRule('Record Full Admin', record_full_admin, views)

  # WHY CAN'T ACCOUNTS DO THIS?
  def record_message_access(principal, record, **unused_args):
    return pha_record_access(principal, record) \
        or principal.isType('MachineApp')
  views = [record_notify,
           record_send_message,
           record_message_attach]
  AccessRule('Record Message Access', record_message_access, views)

  # Document-related views
  def carenet_doc_access(principal, carenet, **unused_args):
    return pha_carenet_access(principal, carenet) \
        or principal.isInCarenet(carenet) \
        or pha_record_access(principal, carenet.record) \
        or full_control(principal, carenet.record)
  views = [carenet_measurement_list,
           carenet_immunization_list,
           carenet_allergy_list,
           carenet_medication_list,
           carenet_procedure_list,
           carenet_problem_list,
           carenet_equipment_list,
           carenet_vitals_list,
           simple_clinical_notes_list,
           carenet_document_list,
           carenet_document,
           carenet_document_meta]
  AccessRule('Carenet Doc Access', carenet_doc_access, views)

  def carenet_special_doc_access(principal, carenet, **unused_args):
    return carenet_doc_access(principal, carenet) \
        or principal.createdRecord(carenet.record)
  views = [read_special_document_carenet]
  AccessRule('Carenet Special Doc Access', carenet_special_doc_access, views)

  def record_doc_access(principal, record, **unused_args):
    return pha_record_access(principal, record) \
        or full_control(principal, record)
  views = [measurement_list,
           immunization_list,
           allergy_list,
           medication_list,
           medicationscheduleitem_list,
           schedulegroup_list,
           adherenceitem_list,
           videomessage_list,
           procedure_list,
           problem_list,
           equipment_list,
           vitals_list,
           lab_list,
           report_ccr,
           record_document_list,
           record_document_meta,
           record_document_meta_ext,
           record_specific_document,
           record_document_label_ext,
           record_document_label,
           document_delete,
           document_create_by_ext_id,
           document_version_by_ext_id,
           document_versions,
           document_create_by_rel,
           document_create_by_rel_with_ext_id,
           get_documents_by_rel,
           document_set_status,
           document_status_history,
           document_rels]
  AccessRule('Record Doc Access', record_doc_access, views)
  
  def record_admin_doc_access(principal, record, **unused_args):
    return record_doc_access(principal, record) \
        or principal.createdRecord(record)  #special case: Admin Apps need to create docs
  views = [document_create,
           document_version]
  AccessRule('Record Admin Doc Access', record_admin_doc_access, views)
  
  def record_special_doc_access(principal, record, **unused_args):
    return record_doc_access(principal, record) \
        or principal.createdRecord(record)
  views = [read_special_document, # should PHAs be able to do this?
           save_special_document]
  AccessRule('Record Special Doc Access', record_special_doc_access, views)

  def record_doc_sharing_access(principal, record, **unused_args):
    return full_control(principal, record)
  views = [document_set_nevershare,
           document_remove_nevershare]
  AccessRule('Record Doc Sharing Access', record_doc_sharing_access, views)

  def record_app_doc_access(principal, record, pha, **unused_args):
    return pha_record_app_access(principal, record, pha)
  views = [record_app_document_meta,
           record_app_document_meta_ext,
           record_app_document_list,
           record_app_specific_document,
           record_app_document_create,
           record_app_document_create_or_update_ext,
           record_app_document_update,
           record_app_document_label]
  AccessRule('Record App Doc Access', record_app_doc_access, views)
  

  # NOTE: old system checked that there was no record passed in. We don't have to
  # do this because all of the views are known to be app-specific
  def app_doc_access(principal, pha, **unused_args):
    return pha_app_access(principal, pha)
  views = [app_document_meta,
           app_document_meta_ext,
           app_document_list,
           app_specific_document,
           app_document_create,
           app_document_create_or_update,
           app_document_create_or_update_ext,
           app_document_update,
           app_document_label]
  AccessRule('App Doc Access', app_doc_access, views)

  # Audit-related views
  # OLD SYSTEM permissions: account: full control, accesstoken: pha access to record
  # does this make sense? should admins have audit access?
  def audit_access(principal, record, **unused_args):
    return full_control(principal, record)
  views = [audit_record_view,
           audit_document_view,
           audit_function_view]
  AccessRule('Audit Access', audit_access, views)

  # Autoshare-related views: should phas or admins be able to do this?
  def autoshare_permissions(principal, record, **unused_args):
    return full_control(principal, record)
  views = [autoshare_list,
           autoshare_list_bytype_all,
           autoshare_create,
           autoshare_delete,
           autoshare_revert] # IN OLD SYSTEM, unpermissioned
  AccessRule('Autoshare Permissions', autoshare_permissions, views)

load_access_rules()
