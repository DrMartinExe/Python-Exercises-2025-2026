# =========================================
# Week 6 Solutions: Mini-Project Challenge
# Save as solutions6.py
#
# The solutions below demonstrate one straightforward implementation.
# These examples prioritize clarity and teaching value over optimization.
#
# --- review_utils.py content (module to be created) ---
module_code = '''def add_contact(contacts, name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})

def find_contact(contacts, name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            return c
    return None
'''

# Write the module file to disk (so it can be imported in real use)
with open('/mnt/data/review_utils.py', 'w') as f:
    f.write(module_code)

# --- Task A: Contact List Refresher ---
contacts = []

from review_utils import add_contact, find_contact

print('\n--- Task A: Contact List ---')
add_contact(contacts, 'Alice', '07123456789', 'alice@example.com')
add_contact(contacts, 'Bob', '07234567890', 'bob@example.com')
print('Contacts after adding:')
print(contacts)

found = find_contact(contacts, 'Alice')
print('Found contact:', found)

# Remove contact function (inline implementation)
def remove_contact(contacts_list, name):
    for i, c in enumerate(contacts_list):
        if c['name'].lower() == name.lower():
            return contacts_list.pop(i)
    return None

removed = remove_contact(contacts, 'Bob')
print('Removed:', removed)
print('Contacts now:', contacts)

# --- Task B: Simple Survey Analyzer ---
print('\n--- Task B: Survey ---')

def collect_responses():
    responses = []
    print("Enter survey responses. Type 'done' when finished.")
    while True:
        rating = input('Rating (1-5): ')
        if rating.lower() == 'done':
            break
        try:
            r = int(rating)
            if r < 1 or r > 5:
                print('Please enter a rating between 1 and 5 (or done).')
                continue
        except ValueError:
            print('Invalid input — enter a number 1-5 or done.')
            continue
        comment = input('Comment (or press Enter): ')
        responses.append({'rating': r, 'comment': comment})
    return responses


def analyze_responses(responses):
    if not responses:
        return {'count': 0, 'average': None, 'min': None, 'max': None, 'comments': []}
    ratings = [r['rating'] for r in responses]
    comments = [r['comment'] for r in responses if r['comment']]
    return {
        'count': len(ratings),
        'average': sum(ratings) / len(ratings),
        'min': min(ratings),
        'max': max(ratings),
        'comments': comments
    }

# For automated demo purposes, we will simulate responses when run non-interactively.
# If run interactively, use collect_responses().

try:
    import sys
    if sys.stdin.isatty():
        responses = collect_responses()
    else:
        # Simulated responses
        responses = [
            {'rating': 5, 'comment': 'Great!'},
            {'rating': 4, 'comment': ''},
            {'rating': 3, 'comment': 'It was ok.'}
        ]
except Exception:
    responses = [
        {'rating': 5, 'comment': 'Great!'},
        {'rating': 4, 'comment': ''},
        {'rating': 3, 'comment': 'It was ok.'}
    ]

report = analyze_responses(responses)
print('Survey report:')
print(report)

# --- Task C: Module usage & save_report ---
print('\n--- Task C: Module & Save Report ---')

# reuse add_contact from review_utils; already written and imported above

import review_utils as ru
add_contact(contacts, 'Charlie', '07345678901', 'charlie@example.com')
print('Contacts final:', contacts)


def save_report(report_dict, filename='report.txt'):
    lines = []
    lines.append(f"Responses: {report_dict['count']}")
    lines.append(f"Average rating: {report_dict['average']}")
    lines.append(f"Min rating: {report_dict['min']}")
    lines.append(f"Max rating: {report_dict['max']}")
    lines.append('Comments:')
    for c in report_dict['comments']:
        lines.append(f" - {c}")
    content = '\n'.join(str(l) for l in lines)
    with open('/mnt/data/' + filename, 'w') as f:
        f.write(content)
    return '/mnt/data/' + filename

report_file = save_report(report, filename='survey_report.txt')
print('Report saved to:', report_file)

# End of solutions6.py content
