

import re
 
def name(s):
  # Use regular expression to extract the first letter of each word
  initials = re.findall(r'\b\w', s)
  # Use regular expression to extract the last word
  last_name = s.split()[-1]
  # Combine the initials and last name with dots
  # result = '.'.join(initials[:-1]).upper() + '.' + last_name.title()
  result = ''.join(initials[::]).upper()
 
  return result
 
#Driver code
s = "mohandas karamchand gandhi gomez"
print(name(s))
