# This program is to be used with good intent, with the express permission of the target.
# Using this program as a ‘prank’, ‘joke’, ’practical joke’, is not condoned.
# This program WILL spam the target email with the number of emails you specify.
# The email you input will be shown to the target email.


# Imports module to test connection and send email
import smtplib

# Clear function -- Password Security
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# Defines Function
def sendMail(subject, message):
  
  # Makes sure connection works, if not, excepts
  try:
    
    # Tests connection
    smtpServer = smtplib.SMTP('smtp.gmail.com:587')
    
    # Identifies to Server with ELHO
    smtpServer.ehlo()

    # Put connection in TLS (Transport Layer Security) Mode
    smtpServer.starttls()
    
    # Logs in with provided credentials
    smtpServer.login(myEmailAddress, password)
    
    # Defines message
    message = "Subject: %s\n\n%s"%(subject, message)
    
    # Sends mail
    smtpServer.sendmail(myEmailAddress, targetEmailAddress, message)
    
    # Quits and Outputs
    smtpServer.quit()
    print("Success: Email sent!")
    
  except:
    
    # Outputs
    print("Failure: Email failed to send.")
    print("Note: Large spams may cause a connection failure.")
    exit()

# Warns User
readDisclaimer = input("Are you SURE that you want to use this program (Y/N): ")

if readDisclaimer.upper() == "Y":
  pass
else:
  exit()

# Asks for Input
numberOfTimes = int(input("Enter the amount of emails you want to send: "))
myEmailAddress = input("Enter your email address: ")
password = input("Enter your password: ")

# Password Security
clear()

# Composes Message
targetEmailAddress = input("Enter the email address of the target: ")
subject = input("Enter a subject: ")
message = input("Enter a message: ")

# Warns User
lastWarning = input("Last Warning: Are you 100% sure that you want to run this (Y/N): ")

if lastWarning.upper() == "Y":
  pass
else:
  exit()
  
# Spams the Emails
for i in range(1, numberOfTimes+1):
  # Calls Function
  sendMail(subject, message)
