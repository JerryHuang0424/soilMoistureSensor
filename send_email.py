import smtplib
from email.message import EmailMessage

#Set the sender email and password and recipient emaic
from_email_addr = '17321421572@qq.com'
from_email_pass = 'xafamfbqyqnidcec' 
to_email_addr = 'jerryhuang0424@qq.com'

msg = EmailMessage()

body = 'Hello from Raspberry Pi'
msg.set_content(body)

msg ['From'] = from_email_addr
msg['To'] = to_email_addr

msg['Subject'] = 'Test email'


server = smtplib.SMTP_SSL('smtp.qq.com', 465)


server.login(from_email_addr, from_email_pass)

server.send_message(msg)

print('Email sent')

server.quit()
