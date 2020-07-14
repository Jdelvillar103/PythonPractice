import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('josdp23@gmail.com','Charmander23?')
conn.sendmail('josdp23@gmail.com', 'jdelvillar103@outlook.com','Subject: Test Email\n\nThis is a test email\n\nFrom Python')
conn.quit()
