"""
    Filename: mail_handler.py
    Author: rathorsunpreet
    License: GNU GPLv3
"""
import smtplib

from email.mime.text import MIMEText

# Get Body of message here
# msg = MIMEText(file content here)

msg['Subject'] = 'The contents of %s' % body_file
msg['From'] = your_own_email_address
msg['To'] = recipient_email_address

s = smtplib.SMTP('localhost')
s.sendmail(From, [To], msg.as_string())
s.quit
