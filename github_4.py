from github import Github

import smtplib
import tinys3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email):
	# me == my email address
	# you == recipient's email address
	me = "emilycon7@gmail.com"
	you = email

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Link"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	html = """\
	<html>
  	<head></head>
	  <body>
	    <p>Hi!<br>
	       How are you?<br>
	       Please log in and fill out your name.<br>
	       Here is the <a href="https://github.com/settings/profile">link</a> you wanted.
	    </p>
	  </body>
	</html>
	"""

	# Record the MIME types of both parts - text/html.
	part1 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	#msg.attach(part1)
	msg.attach(part1)

	# Send the message via local SMTP server.
	s = smtplib.SMTP("smtp.gmail.com", 587)

	s.starttls()
	s.login('emilycon7@gmail.com', 'Run4baby2@')
	s.sendmail(me, you, msg.as_string())
	s.close()

#main class github oject 
git = Github("f035bea0c1f10f4e3a90309133798d3b18efe0c4")
#get organization from github object 
org = git.get_organization("SoundData")


conn = tinys3.Connection('AKIAJWWHY6FOILNL7A6Q', 'zIzaABVZSC7sPekXGGoAKW3VR/Vq/2hc8uHAG80b', tls=True)    
f = open("login.txt", "w+")

    

for user in org.get_members():
	#print(user.name)
	if user.name is None:
		#print (user.login, user.email)
		email = user.email
		#print (email)
		f.write(user.login + "\n")
		if user.email is None:
			print("Please go enter an email in your public profile.")
		else:
			send_email(email)
			#print("Email Sent")		

f = open('login.txt', 'rb')
conn.upload('login.txt', f, 'github-empty-list-names')
f.close

