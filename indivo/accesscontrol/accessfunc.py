"""
Shared access functions used by Access Rules in __init__.py
"""

def full_control(principal, record):
    """
    A principal has full control over a record if it is the owner of the record,
    or if it has a full share of the record.
    """
    return principal.ownsRecord(record) \
        or principal.fullySharesRecord(record)

# PHA 3-legged access functions
# Must insure that:
# 1. Account represented by token may access record
# 2. token itself may access record
# 2.A: access token has full share of record
# 3. Account represented by token may access carenet
# 4. Token may access carenet
# 4.A: access token is unconstrained or 
# 4.B: constrained to THIS carenet
# 5. Proxying PHA is the app it should be.#
# (1,2) & (3,4) & 5 are different: now that we have different calls, 
#  they may be handled in different access rules
#
# So 2 functions:
# Note: 'effective principal' is the proxied account if we have 
#  an access token, and principal is the token itself
def pha_record_access(principal, record):
    account = principal.effective_principal
    return principal.scopedToRecord(record) \
        and full_control(account, record)

def pha_carenet_access(principal, carenet):
    account = principal.effective_principal
    return account.isInCarenet(carenet) \
        and principal.isInCarenet(carenet)

# Note: app-and-record-specific storage is NOT for record-sensitive data:
# it merely allows apps to store app-specific data on a record-by-record
# basis. Thus, as long as the PHA is pinned to the record, it may access
# record_app storage
def pha_record_app_access(principal, record, app):
    return principal.scopedToRecord(record) \
        and (principal.isSame(app) or principal.isProxiedByApp(app))

# PHA 2-legged access
# Note on semantics: The AccessToken Principal should always state that it 'Is the same'
# as its proxying PHA. I.e., it 'is' the PHA in a 2-legged call, and it 'is' the PHA
# in a 3-legged call (though it is 'proxying for' an Account).
# In a 3-legged access, it makes sense to think of the AccessToken as follows: The token 'is'
# a PHA 'proxying' an account. Thus, isSame(app) will return true, and effective_principal
# will be the account.
def pha_app_access(principal, app):
    return principal.isSame(app) 
