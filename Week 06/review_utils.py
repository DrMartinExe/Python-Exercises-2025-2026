# =========================================
# review_utils.py
# Supporting module for Week 6 Mini-Project Challenge
#
# Contains helper functions for managing contacts.
# =========================================

def add_contact(contacts, name, phone, email):
    """Add a new contact to the list of contacts."""
    contacts.append({'name': name, 'phone': phone, 'email': email})


def find_contact(contacts, name):
    """Find a contact by name (case-insensitive)."""
    for c in contacts:
        if c['name'].lower() == name.lower():
            return c
    return None


def remove_contact(contacts, name):
    """Remove a contact by name and return it if found."""
    for i, c in enumerate(contacts):
        if c['name'].lower() == name.lower():
            return contacts.pop(i)
    return None
