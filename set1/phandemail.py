#! python3
import re
import pyperclip

#TODO: Create a regex object for phone #s and email address
phoneRegex = re.compile(r'''
# 415-555-0000, 555-000, (451) 555-0000, 555-000 EXT 12345, EXT.12345, x1234
(
((\d\d\d) | (\(\d\d\d\)))? # area code optional
(\s|-) # separator
\d\d\d # 1st 3 digits
- # separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s)|x) # optional extension
(\d{2,5}))?
)
''', re.VERBOSE)

# EmailRegex
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # symbol 
[a-zA-Z0-9_.+]+ # email domain

''', re.VERBOSE)

#TODO: get text off clipboard
text = pyperclip.paste()
#Extract email/phone from text
exPhone = phoneRegex.findall(text)
exEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in exPhone:
    allPhoneNumbers.append(phoneNumber[0])
# print(allPhoneNumbers) Returns list of PhoneNumbers
# print(exEmail) returns list of emails
#Copy the extraced email/phone

# results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(exEmail)

#for phone with email list
i=0
result = ''
while i < len(allPhoneNumbers):
    result += allPhoneNumbers[i] + ' ' + exEmail[i] + '\n'
    i = i+1
pyperclip.copy(result)


