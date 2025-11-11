# =========================================
# Week 6 — 90 minute Review: Mini-Project Challenge
# Save as exercises6.py
#
# Overview:
# This mini-project combines concepts from Weeks 1-5 into three progressively
# harder tasks. Work through each task. You may use the solutions from prior weeks.
#
# Task A — Contact List Refresher (30 mins)
#  - Create a list of contact dictionaries. Each contact should have 'name', 'phone', and 'email' keys.
#  - Write a function add_contact(contacts, name, phone, email) that adds a new contact.
#  - Write a function find_contact(contacts, name) that returns the contact dict or None.
#  - Write a function remove_contact(contacts, name) that removes a contact by name (use list and dict ops).
#  - Demonstrate adding, finding, and removing contacts and print the list after each operation.
#
# Task B — Simple Survey Analyzer (30 mins)
#  - Create a function collect_responses() that asks users for a rating (1-5) and a comment.
#    Keep asking until the user types 'done'. Store responses as dictionaries in a list.
#  - Write analyze_responses(responses) which:
#      * returns a dict with 'count', 'average', 'min', 'max' for ratings
#      * collects all comments into a single list
#  - Print a small report using these results.
#  - Make sure inputs are validated (ratings converted using int() and modulo used where helpful).
#
# Task C — Small Module & Report (30 mins)
#  - Move at least two functions from Task A/B into a separate module file named 'review_utils.py'.
#    (For this exercise, create a small file that will be imported.)
#  - In the main script, import the module using an alias and call the functions.
#  - Create a function save_report(report_text, filename='report.txt') that writes your survey report to a file.
#  - Call save_report() with the report generated in Task B and confirm the file exists.
#
# Notes / Hints:
#  - Use functions liberally to keep code modular.
#  - Use lists and dictionaries for storage.
#  - Use while loops for repeated user input; use flags or 'break' to stop loops.
#  - Protect against modifying lists unintentionally by copying when needed.
#  - Follow PEP 8 spacing and line length where possible.
#
# Deliverable: a working script that demonstrates all tasks above.
