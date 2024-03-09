import datetime
import os.path
import sqlite3

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dateutil import parser
from sys import argv


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())
  
  if argv[1] == 'add':
        duration = argv[2]
        description = argv[3]
        addEvent(creds, duration, description)
  if argv[1] == 'commit':
        commitTime(creds)



def commitTime(creds):
  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    today = datetime.date.today()
    timeStart=str(today)+"T00:00:00Z"
    timeEnd=str(today)+"T23:59:59Z"
    print("Getting time spent :")
    events_result = (
        service.events()
        .list(
            calendarId="ADD YOUR CALENDAR ID HERE", #<------------------------------ FILL THIS
            timeMin=timeStart,
            timeMax=timeEnd,
            singleEvents=True,
            orderBy="startTime",
            timeZone="TIME ZONE HERE" #<------------------------------ FILL THIS
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return
    total_duration=datetime.timedelta(seconds=0,minutes=0,hours=0)

    id =0
    print("Hours of Time spent : ")
    for event in events:
      start=event["start"].get("dateTime",event["start"].get("date"))
      end=event["end"].get("dateTime",event["end"].get("date"))
      form_start=parser.isoparse(start)
      form_end=parser.isoparse(end)
      duration = form_end-form_start

      total_duration+=duration
      print(f"{event['summary']},duration : {duration}")
    print(f"Time in total : {total_duration}")


    conn = sqlite3.connect('hours.db')
    cur = conn.cursor()
    print("Opened database successfully")


    date=datetime.date.today()
    form_tot_duration=total_duration.seconds/60/60
    coding_hours=(date,'Coding',form_tot_duration)
    cur.execute("INSERT INTO hours VALUES(?, ?, ?);",coding_hours)
    conn.commit()
    print("Time added successfully to hours.db file")




  except HttpError as error:
    print(f"An error occurred: {error}")


def addEvent(creds, duration, description):
    start = datetime.datetime.utcnow()
    
    end = datetime.datetime.utcnow() + datetime.timedelta(hours=int(duration))
    form_start = start.isoformat() + 'Z'
    form_end = end.isoformat() + 'Z'
    event = {
    'summary': description,
    'start': {
        'dateTime': form_start,
        'timeZone': "TIME ZONE HERE", #<------------------------------ FILL THIS
        },
    'end': {
        'dateTime': form_end,
        'timeZone': "TIME ZONE HERE", #<------------------------------ FILL THIS
        },
    }

    service = build('calendar', 'v3', credentials=creds)
    event = service.events().insert(calendarId="ADD YOUR CALENDAR ID HERE", body=event).execute() #<------------------------------ FILL THIS
    print('Event created: %s' % (event.get('htmlLink')))





if __name__ == "__main__":
  main()