import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Send weekly reminder emails.")
parser.add_argument("--email", required=True, help="Sender's email address")
parser.add_argument("--password", required=True,
                    help="Sender's email password")
args = parser.parse_args()


print("Hello")
print("Hello")
print("Hello")
print("Hello")

print("Hello")


# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # SMTP server (Gmail in this case)
SMTP_PORT = 587  # Port for TLS
EMAIL_ADDRESS = args.email  # Read from command-line argument
EMAIL_PASSWORD = args.password  # Read from command-line argument

# Recipients
recipients = [
    "rakeshkhalijol05@gmail.com",
    "rakshithalijol9686399215@gmail.com"
]  # List of recipient emails

# Email content
subject = "Weekly Reminder on data structure"
body = "Hi There!, hope your data structure prep is going well. This is to remind you not to forget your FANG dream. All the best!"


print("Hello")
# Create a MIMEText message
message = MIMEMultipart()
message["From"] = EMAIL_ADDRESS
message["To"] = ", ".join(recipients)
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        # Log in to the SMTP server
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, recipients,
                        message.as_string())  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")


print("Good Night")
