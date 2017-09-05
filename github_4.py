from github import Github

import smtplib
import tinys3

#packages for email 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#send email function with user's email passed in as the parameter from the for loop
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
	s.login('emilycon7@gmail.com', 'Gmail Password')
	s.sendmail(me, you, msg.as_string())
	s.close()

#main class github oject 
git = Github("O Auth Generated Token Value")
#get organization from github object 
org = git.get_organization("SoundData")

#Establish connection with AWS S3 account 
conn = tinys3.Connection('Access Key', 'Access Key', tls=True) 
# Create a text file to create and/or write to text file if not already created
f = open("login.txt", "w+")

    
#For loop to go through members of github organization
for user in org.get_members():
	#Check if member has a public name or not 
	if user.name is None:
		# Save the email if no public name member 
		email = user.email
		#Write the name of the user's login to a text file 
		f.write(user.login + "\n")
		# Special case if user also does not have a public email to send a successful email
		if user.email is None:
			print("Please go enter an email in your public profile.")
		#Call email function to send email to nameless user	
		else:
			send_email(email)
			#print("Email Sent")		

# Access file again to read binary in order for AWS S3 bucket to read the file
f = open('login.txt', 'rb')
# Create connection to upload file to AWS S3 bucket 
# Parameters: name of file, file variable name, and bucket name file gets sent to
conn.upload('login.txt', f, 'github-empty-list-names')
# Close the connection
f.close

