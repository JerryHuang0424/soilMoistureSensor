import smtplib
from email.message import EmailMessage
import RPi.GPIO as GPIO
import time
from datetime import datetime
import schedule

def send_mail(message):
	#Set the sender email and password and recipient emaic
	from_email_addr = '17321421572@qq.com'
	from_email_pass = 'xafamfbqyqnidcec' 
	to_email_addr = 'jerryhuang0424@qq.com'

	msg = EmailMessage()

	body = message
	msg.set_content(body)

	msg ['From'] = from_email_addr
	msg['To'] = to_email_addr

	msg['Subject'] = 'Water condition'


	server = smtplib.SMTP_SSL('smtp.qq.com', 465)


	server.login(from_email_addr, from_email_pass)

	server.send_message(msg)

	print('Email sent')

	server.quit()


#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		now = datetime.now()
		formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
		message = f"Water lack! The time is: {formatted_time}" 
		print(message)
		send_mail(message)
	else:
		now = datetime.now()
		formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
		message = f"Not need water! The time is: {formatted_time}"
		print(message)
		send_mail(message)
		
# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
# GPIO.add_event_callback(channel,callback)

# infinite loop
def main():
	schedule.every().day.at("09:00").do(lambda : callback(channel))
	schedule.every().day.at("12:00").do(lambda : callback(channel))
	schedule.every().day.at("15:00").do(lambda : callback(channel))
	schedule.every().day.at("19:00").do(lambda : callback(channel))

    
	GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
	GPIO.add_event_callback(channel,callback)

    
	try:

		while True:
			schedule.run_pending()
			time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
		
if __name__ == "__main__":
	print('Program is Running!')
	main()
