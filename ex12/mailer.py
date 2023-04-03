import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "test4ex12@seznam.cz"
receiver_email = "xhelp00@gmail.com"
subject = "Email with attachment"
filename = "attachment.txt"
filepath = "./attachment.txt"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

with open(filepath, "rb") as attachment:
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
message.attach(part)

with smtplib.SMTP("smtp.seznam.cz", 25) as server:
	server.starttls()
	server.login("test4ex12@seznam.cz", "Pokemonblue89")
	server.sendmail(sender_email, receiver_email, message.as_string())
