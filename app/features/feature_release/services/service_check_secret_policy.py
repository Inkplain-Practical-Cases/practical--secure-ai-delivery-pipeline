# Fail closed when runtime secrets have been copied to image metadata.
import re

def service_check_secret_policy(image_env: dict[str,str], runtime_keys: set[str]) -> bool:
    if any(re.search(r'(SECRET|TOKEN|PASSWORD|API_KEY)',key,re.I) for key in image_env):
        raise ValueError('Image environment must not contain credential keys')
    if not runtime_keys or any(not key or '=' in key for key in runtime_keys):
        raise ValueError('Runtime secret names must be valid')
    return True
