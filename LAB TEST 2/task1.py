import re

def mask_sensitive_info(log_line):
    # Mask emails: user@*.com
    email_pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'
    def mask_email(match):
        return f"{match.group(1)}@*.com"

    # Mask phone numbers: ***43210 (last 5 digits visible)
    phone_pattern = r'(\b\d{10}\b)'
    def mask_phone(match):
        return f"*{match.group(1)[-5:]}"

    # Apply masking
    masked_line = re.sub(email_pattern, mask_email, log_line)
    masked_line = re.sub(phone_pattern, mask_phone, masked_line)
    return masked_line

# Sample Input
log = """User Raj logged in with email raj.kumar@example.com and phone
9876543210"""

# Masked Output
masked_log = mask_sensitive_info(log)
print(masked_log)