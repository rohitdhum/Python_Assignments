import psutil
import sys
import os
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid", "name", "username", "status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

def SendMail(AttachmentPath, ReceiverEmail):
    SenderEmail = "pothole.detection.sys@gmail.com"      # Sender Email address
    SenderPassword = "vjsw oimr iwgk dcuk"               # App Password
     
    try:
        msg = MIMEMultipart()
        msg['From'] = SenderEmail
        msg['To'] = ReceiverEmail
        msg['Subject'] = "Automated Process Surveillance System Log File"
        
        Body = """Dear Admin,

This is an automated system report containing the running process details logged by the 'Automated Platform Surveillance System'.

Log Details:
- Server Status: Operational
- Attachment Type: System Log File (.log)
- Timestamp: Generated Automatically

Please find the attached log file for further analysis.

Best Regards,
Automated Platform Surveillance System Automation Script
"""

        msg.attach(MIMEText(Body, 'plain'))
        
        fobj = open(AttachmentPath, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(fobj.read())
        fobj.close()
        
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(AttachmentPath)}")
        msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SenderEmail, SenderPassword)
        server.send_message(msg)
        server.quit()
        
        print(f"Log file successfully sent to {ReceiverEmail}")
    except Exception as e:
        print(f"Unable to send mail due to error: {e}")

def PlatformSurvillence(FolderName, MailID=None):
    Border = "_" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not a directory")
            return 
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Automated_%s.log" %timestamp)

    fobj = open(FileName, "w")

    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("_____Automated Platform Survillence System_____\n")
    fobj.write("Log file gets created at :" + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.write("----------System report----------\n")

    # CPU INformation
    fobj.write("Number of active CPU usage : %s\n" %psutil.cpu_count())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border + "\n")

    # RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM available : %s\n" %memory.total)
    fobj.write(Border + "\n")

    # Network usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %2f MB\n" %(netobj.bytes_sent / (1024*1024)))
    fobj.write("Recieve : %2f MB\n" %(netobj.bytes_recv / (1024*1024)))

    # Process log
    Data= ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name: %s\n" %info.get("name"))
        fobj.write("UserName: %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU Usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f\n" %info.get("memory_percent"))
    
        fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("----------End of log file----------\n")
    fobj.write(Border + "\n")

    fobj.close()

    if MailID is not None:
        SendMail(FileName, MailID)

def main():

    Border = "_" * 50
    print(Border)
    print("_____Automated Platform Survillence System_____")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform")
            print("1 : It fetch the information of running processess")
            print("2 : It fetches information about the primary storage as RAM")
            print("3 : It fetches information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessure")
            print("5 : It gets auto schedued periodically")
            print("6 : It maintains all records into the log files")
            print("7 : It sends the log files through email periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name Email_ID")
            print("Time_Interval : Time in minutes for peroidic execution")
            print("Folder_Name   : Name of folder for thr log creation")
            print("Email_ID      : Mail ID to send the log file")
            
        else:
            print("unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for geting more details")

    # Task 3: Local Surveillance Log Creation
    elif(len(sys.argv) == 3):
        print("Schedular started succesfully")
        print("Press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    # Task 4: Surveillance Log Creation + Mail Transfer
    elif(len(sys.argv) == 4):
        print("Schedular with Mail Automation started successfully")
        print("Press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2], sys.argv[3])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for geting more details")

    print(Border)
    print("----Thank you for using our automattion system----")
    print(Border)

if __name__ == "__main__":
    main()
