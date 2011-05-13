
AUTHORIZATION_MODULE_LOADED = False

def check_safety():
  if not AUTHORIZATION_MODULE_LOADED:
    print "Authorization Module not loaded, refusing to serve."
    raise Exception("Authorization Module not loaded, refusing to serve.")
