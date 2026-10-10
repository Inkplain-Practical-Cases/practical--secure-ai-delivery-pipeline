# A promotion requires an approving actor, successful gates and a healthy stage.

def service_decide_promotion(role: str, tests_passed: bool, stage_healthy: bool, approved: bool) -> str:
    if role != 'release-approver' or not approved:
        raise PermissionError('Authorized approval required')
    if not tests_passed:
        return 'hold'
    if not stage_healthy:
        return 'rollback'
    return 'promote'
