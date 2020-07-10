import re

message = 'Call me 415-555-1011 tomorrow, or at 281-687-8491'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo)

#finall return list
#search return first match as string