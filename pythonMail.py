import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import sys
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

fromaddr = "FROM EMAIL"
toaddr = "TO EMAIL"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr


def getBody(filename):
    with open(str(filename),'r') as myfile:
         data=myfile.read().replace('\n', '')
    return data

try:
    body = "Below is the contents of this file: " + str(sys.argv[1]) + "\n\n\n" + getBody(str(sys.argv[1]))
    msg['Subject'] = "Send myself: " + str(sys.argv[1])
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "PASSWORD HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
except (ValueError,IndexError):
    print('You have to specify a FILE.')
