# A digest is the artifact's identity; mutable tags are only labels.
import re

def service_verify_artifact_provenance(image_ref: str, expected_digest: str, provenance_digest: str) -> bool:
    pattern = r'^sha256:[a-f0-9]{64}$'
    if not re.fullmatch(pattern, expected_digest):
        raise ValueError('Invalid immutable image digest')
    if not image_ref.endswith('@' + expected_digest):
        raise ValueError('Deployment must reference an immutable image digest')
    if provenance_digest != expected_digest:
        raise ValueError('Provenance does not match artifact')
    return True
