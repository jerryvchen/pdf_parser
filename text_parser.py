"""
text_parser.py

Contains relevent functions to process text.

:author: Jerry Chen
:email: jerryvc@uci.edu
"""

import json
import re
from typing import List, Dict, Union, Optional

def parse_text(text: str) -> List[Dict[str, Union[str, bool, Optional[str]]]]:
    lines = text.split('\n')
    parsed_data = []

    # Patterns
    name_pattern = re.compile(r'(?P<last_name>[A-Z]+)(?:, (?P<suffix>JR\.|SR\.))?, (?P<first_name>[A-Z]+)(?: \((?P<middle_initial>[A-Z])\))?(?: \(BC\))?(?: \(\*\))?')
    phone_pattern = re.compile(r'Office Ph: (?P<office_ph>\d+)')
    fax_pattern = re.compile(r'Office Fax: (?P<office_fax>\d+)')
    nicu_ph_pattern = re.compile(r'Nicu Ph: (?P<nicu_ph>\d+)')
    nicu_fax_pattern = re.compile(r'Nicu Fax: (?P<nicu_fax>\d+)')
    email_pattern = re.compile(r'Email: (?P<email>\S+)')
    second_email_pattern = re.compile(r'(?P<second_email>\S+)')

    for i, line in enumerate(lines):
        name_match = name_pattern.match(line)
        if name_match:
            entry = {
                'last_name': name_match.group('last_name'),
                'first_name': name_match.group('first_name'),
                'middle_initial': name_match.group('middle_initial') or None,
                'suffix': name_match.group('suffix') or None,
                'bc': 'BC' in line,
                'special_member': '*' in line,
                # Initialize optional fields with None
                'address1': None,
                'address2': None,
                'office_ph': None,
                'office_fax': None,
                'nicu_ph': None,
                'nicu_fax': None,
                'email': None,
                'second_email': None,
            }
            if i + 1 < len(lines) and lines[i + 1].strip():  # Check if next line exists and is not empty
                entry['address1'] = lines[i + 1].strip()
                if i + 2 < len(lines) and lines[i + 2].strip():  # Check if the line after the next line exists and is not empty
                    entry['address2'] = lines[i + 2].strip()

            for j, sub_line in enumerate(lines[i+1: i+7]):  # Looking at the next 6 lines for other optional fields
                phone_match = phone_pattern.search(sub_line)
                if phone_match:
                    entry['office_ph'] = phone_match.group('office_ph')
                
                fax_match = fax_pattern.search(sub_line)
                if fax_match:
                    entry['office_fax'] = fax_match.group('office_fax')

                nicu_ph_match = nicu_ph_pattern.search(sub_line)
                if nicu_ph_match:
                    entry['nicu_ph'] = nicu_ph_match.group('nicu_ph')

                nicu_fax_match = nicu_fax_pattern.search(sub_line)
                if nicu_fax_match:
                    entry['nicu_fax'] = nicu_fax_match.group('nicu_fax')

                email_match = email_pattern.search(sub_line)
                if email_match:
                    entry['email'] = email_match.group('email')
                
                second_email_match = second_email_pattern.search(sub_line)
                if second_email_match:
                    entry['second_email'] = second_email_match.group('second_email')

            parsed_data.append(entry)

    return json.dumps(parsed_data)