import json
import smtplib
from email.mime.text import MIMEText


def send_email(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        action = body.get("action")
        to_email = body.get("email")

        if not action or not to_email:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "error",
                    "message": "action and email are required"
                })
            }

        if action == "SIGNUP_WELCOME":
            username = body.get("username", "User")
            subject = "Welcome to Mini HMS"
            message = f"Hello {username}, your account has been created successfully."

        elif action == "BOOKING_CONFIRMATION":
            patient_name = body.get("patient_name", "Patient")
            doctor_name = body.get("doctor_name", "Doctor")
            slot_date = body.get("slot_date", "")
            slot_time = body.get("slot_time", "")

            subject = "Booking Confirmation"
            message = (
                f"Hello {patient_name}, your appointment with Dr. {doctor_name} "
                f"is confirmed for {slot_date} at {slot_time}."
            )
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "error",
                    "message": "Invalid action"
                })
            }

        sender_email = "wwwparamarchandrarash@gmail.com"
        sender_password = "kywjiniywixmizlz"

        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        return {
            "statusCode": 200,
            "body": json.dumps({
                "status": "success",
                "action": action,
                "message": f"Email sent successfully to {to_email}"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "error",
                "message": str(e)
            })
        }