import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

with open("credentials.json", "r") as file:
    credentials = json.load(file)


# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # SMTP server (Gmail in this case)
SMTP_PORT = 587  # Port for TLS
EMAIL_ADDRESS = "rakeshhalijol@gmail.com"  # Replace with your email
# Replace with your app password or email password
EMAIL_PASSWORD = credentials.get("password")

# Recipients
recipients = ["rakeshkhalijol05@gmail.com",
              "rakshithalijol9686399215@gmail.com"]  # List of recipient emails

# Email content
subject = "Weekly Reminder on data structure"
body = "Hi There!, hope your data structure prep is going well this is to keep remind that don't forgot your fang dream, All the best."

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
