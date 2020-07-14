import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('josdp23@gmail.com','Charmander23?')
conn.select_folder('INBOX',readonly=True)
UID = conn.search([u'UNSEEN'])
rawMessage = conn.fetch([UID[0]], ['BODY[]','FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[UID[0]][b'BODY[]'])
print(message.get_subject())
message.get_addresses('from')
message.text_part
message.html_part
print(message.text_part.get_payload().decode('UTF-8'))

conn.logout