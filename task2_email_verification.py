# ============================================
# TASK 2 - Email ID Verification
# Course: Programming for Problem Solving Lab
# Student: Dasari Sai Balaji
# Roll No: 25951A66G0
# Branch: CSM-C
# ============================================

def is_valid_email(email):
    """Validate an email ID based on defined rules."""

    if len(email) < 1 or len(email) > 100:
        return False, "Email length out of range (1-100)"

    if ' ' in email:
        return False, "Spaces not allowed"

    if not all(32 <= ord(c) <= 126 for c in email):
        return False, "Non-printable ASCII characters found"

    count_at = email.count('@')
    if count_at != 1:
        return False, "Email must contain exactly one @ symbol"

    local, domain = email.split('@')

    if not local:
        return False, "Local part cannot be empty"

    allowed = set('abcdefghijklmnopqrstuvwxyz'
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                  '0123456789_-.')
    if not all(c in allowed for c in local):
        return False, "Invalid characters in local part"

    if '.' not in domain:
        return False, "Domain must contain at least one dot after @"

    return True, "Valid Email ID"

# Main program
email = input("Enter email ID: ").strip()
valid, message = is_valid_email(email)
print(f"Result : {message}")
