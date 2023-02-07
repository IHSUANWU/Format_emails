import sys
import re
import pyperclip

# Install Python module
# > pip3 install pyperclip

# pbcopy -> "paste bin copy"; utility on macOS to copy the output of a command to the clipboard

# Read emails from text file:
# python3 format_emails.py < unformatted-emails.txt


def input_multiple_lines():
    contents = []
    for line in sys.stdin:
        contents.append(line)
    return '\n'.join(contents)

print("put in emails, finish with [Ctrl+D]:")
emails = input_multiple_lines()
regex = r'\b[\w\.-]+@gmail\.com'
matched_emails = re.findall(regex, emails)

print('Matched emails:')
for e in matched_emails:
  print(f'  {e}')

email_str = ','.join(matched_emails)
pyperclip.copy(email_str)
