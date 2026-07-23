""" 6: Write a program that schedules the following messages:
• Monday at 9:00 AM: Start your weekly goals
• Wednesday at 5:00 PM: Review your weekly progress
• Friday at 6:00 PM: Weekly work completed
Use:
schedule.every().monday.at(...)
schedule.every().wednesday.at(...)
schedule.every().friday.at(...)
"""

import schedule
import time
import datetime

def Display(message):

    Time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print(f"[{Time}] : Notification :{message}")

def main():
    print("....Program is started....")

    message1 = "Start your weekly goals"

    message2 = "Review your weekly progress"

    message3 = "Weekly work completed"

    schedule.every().monday.at("09:00").do(Display, message = message1 )

    schedule.every().wednesday.at("17:00").do(Display, message = message2 )

    schedule.every().friday.at("18:00").do(Display, message = message3 )

    print("Tasks scheduled successfully")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()