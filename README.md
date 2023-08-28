# Twilio-SMS-Medication-Reminder
This uses the Twilio API, to send my phone number messages every 2 days to take my medication

# Twilio Medication Reminder
Welcome to the Twilio Medication Reminder repository! This Python script utilizes the Twilio API to help you stay on track with your medication regimen by sending timely reminders to your phone.

## Overview
The Twilio Medication Reminder script automates the process of sending medication reminders to your phone. It uses the Twilio service to send messages containing your specified reminder text at regular intervals. By setting the script to run in the background, you can ensure that you receive your reminders consistently.

## Setup
Ensure you have Python installed on your system.
Clone this repository to your local machine.
Open the terminal and navigate to the repository's directory.
Install the required dependencies using pip install twilio.
Open the medication_reminder.py file and update the Account_SID, Auth_Token, to, and from_ variables with your Twilio account details and phone numbers.
Customize the msg variable to include your medication reminder.
## Usage
Run the script using the command: python medication_reminder.py.
The script will send the specified medication reminder to your phone.
It will wait for approximately 48 hours before sending the next reminder, allowing for day-on, day-off reminders.
## Dependencies
twilio: The Twilio Python library is used for sending messages.
time: The Time Python library is used for keeping track of time.
## Important Note
This script serves as a basic medication reminder tool. Always consult your healthcare provider for accurate and personalized medication instructions.
Adjust the sleep time (time.sleep()) as needed to suit your specific timing preferences.
Feel free to customize and modify the script according to your needs. By utilizing this script, you can ensure that you stay consistent with your medication schedule and prioritize your health.
