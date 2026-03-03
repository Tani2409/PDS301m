def deduplicate_emails(email_list):
    unique_email_set = set(email_list)
    return list(unique_email_set)

emails = [
    "user1@example.com",
    "user2@example.com",
    "user1@example.com", # Duplicate
    "user3@example.com",
    "user2@example.com"  # Duplicate
]

unique_emails = deduplicate_emails(emails)
print(f"Original list: {emails}")
print(f"Unique list: {unique_emails}")
