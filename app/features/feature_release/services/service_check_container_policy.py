# Verify the Dockerfile is non-root and never uses ARG/ENV for credential names.
from pathlib import Path
import re

def service_check_container_policy(path: str) -> bool:
    source = Path(path).read_text(encoding='utf-8')
    lines = [line.strip() for line in source.splitlines() if line.strip() and not line.lstrip().startswith('#')]
    users = [line.split(maxsplit=1)[1] for line in lines if line.upper().startswith('USER ')]
    if not users or users[-1] in ('root', '0'):
        raise ValueError('Image must run as a non-root user')
    if re.search(r'(?im)^\s*(ARG|ENV)\s+\w*(TOKEN|SECRET|PASSWORD|API_KEY)\w*', source):
        raise ValueError('Build-time secret exposure forbidden')
    return True
