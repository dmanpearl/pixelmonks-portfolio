import logging
import time

logger = logging.getLogger(__name__)

HONEYPOT_FIELD = "website"
TIMING_FIELD = "form_rendered_at"
MIN_SUBMIT_SECONDS = 3


def check_honeypot(post_data):
    """Return (triggered, reason) for raw POST data.

    Three checks:
    1. Hidden decoy field was filled (bot filled every field)
    2. Timing field is missing or non-numeric (bot skipped JS / field injection)
    3. Form submitted faster than a human could read it
    """
    if post_data.get(HONEYPOT_FIELD, "").strip():
        return True, "honeypot_filled"

    raw_ts = str(post_data.get(TIMING_FIELD, "")).strip()
    if not raw_ts.isdigit():
        return True, "missing_timestamp"

    elapsed = time.time() - int(raw_ts)
    if elapsed < MIN_SUBMIT_SECONDS:
        return True, "submitted_too_fast"

    return False, ""
