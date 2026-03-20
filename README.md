# Mini Hospital Management System

A Django-based Mini Hospital Management System that supports doctor and patient authentication, doctor slot creation, patient appointment booking, and serverless email notification integration.

## Features

- Doctor and Patient signup/login
- Role-based access control
- Doctor can add appointment slots
- Patient can view available slots
- Patient can book appointments
- Booked slots are hidden from other patients
- Booking history for patients
- Separate serverless email notification service
- Lambda endpoint triggered from Django backend

## Tech Stack

- Backend Framework: Django
- Database: SQLite
- ORM: Django ORM
- Authentication: Django Auth
- Email Service: Python Serverless Function
- Serverless Framework: serverless-offline for local demo

## Project Structure

```
mini_hms/
├── core/
├── hospital/
├── templates/core/
├── email_service/
├── requirements.txt
├── .gitignore
├── readme.md
├── db.sqlite3
├── manage.py






