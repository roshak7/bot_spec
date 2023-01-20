import smtplib

# Get the email and password from the user
email = input("Enter your email: ")
password = input("Enter your password: ")

# Get the recipient's email and the subject and body of the email
to_email = input("Enter the recipient's email: ")
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")

# Set up the SMTP server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(email, password)

# Send the email
msg = f'Subject: {subject}\n\n{body}'
server.sendmail(email, to_email, msg)

# Disconnect from the server
server.quit()