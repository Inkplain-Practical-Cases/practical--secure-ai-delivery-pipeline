# Recovery must target a previously verified immutable digest.
def service_resolve_rollback(target: str, verified_digests: set[str]) -> str:
    if not target.startswith('sha256:') or target not in verified_digests:
        raise ValueError('Rollback digest is not verified')
    return target
