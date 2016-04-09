import smtplib

recipients = [
	'alm0415@westminstercollege.edu',
	'aidan.melen94@gmail.com'
]

def compose_message():
	subject = "A Hamath User Requested Teacher Credentials"
	text = "Please verify me as a teacher."
	message = "Subject: %s\n\n%s" % (subject, text)
	return message

def send_teacher_request_email(username, first_name, last_name, user_email_address):
	TO = recipients if type(recipients) is list else [recipients]
	SUBJECT = "Teacher Credentials Requested\n\n"
	TEXT = "User creditials need to be processed.\n\nUSER INFORMATION\nUSERNAME: %s\nFIRSTNAME: %s\n LASTNAME: %s" % (str(first_name.title()), str(last_name.title()), str(username))
	send_email(TO, SUBJECT, TEXT)

def send_thank_you_email_for_teacher_request(username, first_name, last_name, user_email_address):
	TO = [user_email_address]
	SUBJECT = "Welcome to Hamath " + first_name.title() + "!\n\n"
	TEXT = "Thank you for signing up with Hamath! One of our admins will review your request for Teacher credentials shortly.\n\nUSER INFORMATION\nUSERNAME: %s\nFIRSTNAME: %s\n LASTNAME: %s" % (str(first_name.title()), str(last_name.title()), str(username))
	send_email(TO, SUBJECT, TEXT)

def send_thank_you_email(username, first_name, last_name, user_email_address):
	TO = [user_email_address]
	SUBJECT = "Welcome to Hamath " + first_name.title() + "!\n\n"
	TEXT = "Thank you for signing up with Hamath! \n\nUSER INFORMATION\nUSERNAME: %s\nFIRSTNAME: %s\n LASTNAME: %s" % (str(first_name.title()), str(last_name.title()), str(username))
	send_email(TO, SUBJECT, TEXT)

def send_email(TO, SUBJECT, TEXT):
	user = 'hamathmathgame@gmail.com'
	gmail_user = user
	gmail_pwd = 'Helloworld'
	FROM = user

	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.close()
		print 'successfully sent the mail'
	except:
		print "failed to send mail"
