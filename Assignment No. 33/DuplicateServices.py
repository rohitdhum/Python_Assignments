import os
import sys
import re
import time
import hashlib
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SENDER_EMAIL = "pothole.detection.sys@gmail.com"
SENDER_PASSWORD = "vjsw oimr iwgk dcuk" 

def PrintHelp():
    HelpText = """
Duplicate File Removal Automation
---------------------------------
This script scans a directory, identifies duplicate files using checksums,
deletes duplicate files, creates a log file, and sends the log file through email.

Usage:
    python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Options:
    -h, --help     Display help information.
    -u, --usage    Display usage information.
"""
    print(HelpText) 

def PrintUsage():
    UsageText = f"Usage: python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>"
    print(UsageText)  

def ValidateEmailAddress(Email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, Email) is not None

def ValidateInput(DirPath, IntervalStr, ReceiverEmail):
    # Directory Validation
    if not DirPath:
        print("Directory Path not provided")
        return False, "Directory Path not provided"

    if not os.path.isabs(DirPath):
        print(f"Directory path {DirPath} is not an absolute path")
        return False, "Not an absolute path"

    if not os.path.exists(DirPath):
        print(f"Directory path {DirPath} does not exist")
        return False, "Directory does not exist"

    if not os.path.isdir(DirPath):
        print(f"Path {DirPath} is not a directory")
        return False, "Path is not a directory"

    if not os.access(DirPath, os.R_OK | os.W_OK):
        print(f"Permission denied for directory {DirPath}")
        return False, "Permission denied"

    # Interval Validation
    if not IntervalStr:
        print("Time interval not provided")
        return False, "Time interval not provided"

    if not IntervalStr.isdigit():
        print(f"Interval {IntervalStr} must be a valid numeric value")
        return False, "Invalid interval format"

    Interval = int(IntervalStr)
    if Interval <= 0:
        print("Time interval must be greater than zero")
        return False, "Interval must be > 0"

    # Email Validation
    if not ReceiverEmail:
        print("Receiver email address not provided")
        return False, "Receiver email not provided"

    if not ValidateEmailAddress(ReceiverEmail):
        print(f"Invalid receiver's email format: {ReceiverEmail}")
        return False, "Invalid email format"

    return True, "Validation Successful"

def CreateLogDirectory():
    LogDir = "Marvellous"
    if not os.path.exists(LogDir):
        os.makedirs(LogDir)
    return LogDir

def CalculateCheckSum(FilePath, BlockSize=1024):
    Hasher = hashlib.md5()
    try:
        with open(FilePath, "rb") as fobj:
            Buf = fobj.read(BlockSize)
            while len(Buf) > 0:
                Hasher.update(Buf)
                Buf = fobj.read(BlockSize)
        return Hasher.hexdigest()
    except Exception:
        return None

def ScanAndRemoveDuplicate(DirPath, LogFilePath):
    Stats = {
        "StartTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "StartTimeFormatted": datetime.now().strftime("%d %B %Y, %I:%M:%S %p"),
        "CompletionTime": "",
        "CompletionTimeFormatted": "",
        "DirPath": DirPath,
        "TotalFiles": 0,
        "TotalDuplicates": 0,
        "TotalDeleted": 0,
        "EmailStatus": "Pending"
    }

    CheckSumDict = {}

    with open(LogFilePath, "w") as LogFile:
        LogFile.write("=" * 50 + "\n")
        LogFile.write(".....Marvellous Duplicate File Removal Log.....\n")
        LogFile.write("=" * 50 + "\n")
        LogFile.write(f"Start Time       : {Stats['StartTime']}\n")
        LogFile.write(f"Target Directory : {DirPath}\n")
        LogFile.write("_" * 50 + "\n")
        LogFile.write("....LOG ENTRIES....\n")

        for FolderName, SubFolder, Files in os.walk(DirPath):
            for FileName in Files:
                FilePath = os.path.join(FolderName, FileName)
                Stats["TotalFiles"] += 1

                # File Validation
                if not os.path.exists(FilePath):
                    LogFile.write(f"Error, file missing : {FilePath}\n")
                    continue

                if not os.path.isfile(FilePath):
                    LogFile.write(f"Skip, not a regular file : {FilePath}\n")
                    continue

                CheckSum = CalculateCheckSum(FilePath)
                if CheckSum is None:
                    LogFile.write(f"Error, could not calculate checksum for : {FilePath}\n")
                    continue

                if CheckSum in CheckSumDict:
                    Stats["TotalDuplicates"] += 1

                    try:
                        if os.access(FilePath, os.W_OK):
                            os.remove(FilePath)
                            Stats["TotalDeleted"] += 1
                            LogFile.write(f"Deleted, Path : {FilePath} | Checksum : {CheckSum}\n")

                        else:
                            LogFile.write(f"Error, deletion failed (Permission Denied) : {FilePath}\n")

                    except Exception as e:
                        LogFile.write(f"Error, deletion failed for {FilePath} : {str(e)}\n")

                else:
                    CheckSumDict[CheckSum] = FilePath

        Stats["CompletionTime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Stats["CompletionTimeFormatted"] = datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

        LogFile.write("\n" + "_" * 50 + "\n")
        LogFile.write("-----SUMMARY-----\n")
        LogFile.write(f"Completion Time          : {Stats['CompletionTime']}\n")
        LogFile.write(f"Total Files Scanned      : {Stats['TotalFiles']}\n")
        LogFile.write(f"Total Duplicates Found   : {Stats['TotalDuplicates']}\n")
        LogFile.write(f"Total Duplicates Deleted : {Stats['TotalDeleted']}\n")

    return Stats

def SendEmailWithLog(ReceiverEmail, LogFilePath, Stats):
    try:
        Msg = MIMEMultipart()
        Msg['From'] = SENDER_EMAIL
        Msg['To'] = ReceiverEmail
        Msg['Subject'] = "Duplicate File Removal Operation Report"

        Body = f"""Jay Ganesh,

The DuplicateFile removal operation has been completed successfully.

Operation Statistics:
Starting time of scanning: {Stats['StartTimeFormatted']}
Completion time of scanning: {Stats['CompletionTimeFormatted']}
Directory scanned: {Stats['DirPath']}
Total number of files scanned: {Stats['TotalFiles']}
Total number of duplicate files found: {Stats['TotalDuplicates']}
Total number of duplicate files deleted: {Stats['TotalDeleted']}

Please find the detailed log file attached to this email.

Regards,
Marvellous Automation System
"""

        Msg.attach(MIMEText(Body, "plain"))   

        if os.path.exists(LogFilePath):
            FileName = os.path.basename(LogFilePath)

            with open(LogFilePath, "rb") as Attachment:
                Part = MIMEBase("application", "octet-stream")
                Part.set_payload(Attachment.read())
                encoders.encode_base64(Part)
                Part.add_header("Content-Disposition", f"attachment; filename={FileName}")
                Msg.attach(Part)

        Server = smtplib.SMTP("smtp.gmail.com", 587)
        Server.starttls()
        Server.login(SENDER_EMAIL, SENDER_PASSWORD)
        Server.send_message(Msg)
        Server.quit()
        return True, "Email sent successfully"

    except Exception as e:
        return False, f"Email delivery failed :{str(e)}"

def UpdateLogEmailStatus(LogFilePath, EmailStatusMessage):
    try:
        with open(LogFilePath, "a") as LogFile:
            LogFile.write(f"Email Status :{EmailStatusMessage}\n")    
            LogFile.write("_" * 40 + "\n")

    except Exception:
        pass