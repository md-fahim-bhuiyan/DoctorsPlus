import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from django.utils import timezone
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_google_meet_link(appointment):
    # Load the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        f'C:\\Users\\User\\Documents\\GitHub\\DoctorsPlus/credentials.json',
        scopes=['https://www.googleapis.com/auth/calendar']
    )

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Set the appointment start and end time
    start_time = datetime.datetime.combine(appointment.appointment_date, appointment.appointment_time)
    end_time = start_time + timedelta(minutes=30)

    # Create the event
    event = {
        'summary': 'Appointment with {}'.format(appointment.doctor),
        'start': {
            'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'your-timezone',  # Replace 'your-timezone' with the appropriate time zone
        },
        'end': {
            'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'your-timezone',  # Replace 'your-timezone' with the appropriate time zone
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'sample123',
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet',
                },
            },
        },
    }

    try:
        # Call the Google Calendar API to create the event
        event = service.events().insert(calendarId='primary', body=event).execute()

        # Get the Google Meet link from the conference data
        meet_link = event['conferenceData']['entryPoints'][0]['uri']

        return meet_link
    except HttpError as e:
        # Handle any errors that occur during the API request
        print('An error occurred: {}'.format(e))
        return None