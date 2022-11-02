import smtplib

sender = "ricsneakers@gmail.com"
receiver = "lhobbes@protonmail.com"
password = "husaffazjjrcrrdj"
subject = "Sup buddy - Python Test"
body = "I sent this email via python, aren't I fucking so cool!! ;D"

# header
message = f"""From: {sender}
TO: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("You logged in!")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in, try again.")
