import sys
import time
from datetime import datetime
import DuplicateServices as DS

def RunAutomation(DirPath, ReceiverEmail):
    try:
        print("\n" + "_" * 50)
        print("[Step 1] creating log directory...")
        LogDir = DS.CreateLogDirectory()

        # Create log filename with date and time format
        TimeStamp = datetime.now().strftime("%d %m %Y %H %M %S")
        LogFileName = f"DuplicateRemovalLog {TimeStamp}.log"
        LogFilePath = f"{LogDir}/{LogFileName}"

        print("[Step 2] Scanning for duplicates and deleting...")
        Stats = DS.ScanAndRemoveDuplicate(DirPath, LogFilePath)
        print(f"         Scanned: {Stats['TotalFiles']} files | Deleted: {Stats['TotalDeleted']} duplicates")

        print("[Step 3] Connecting to Gmail SMTP server & sending email...")
        Success, EmailMsg = DS.SendEmailWithLog(ReceiverEmail, LogFilePath, Stats)
        print(f"         Email Delivery Result: {EmailMsg}")
 
        DS.UpdateLogEmailStatus(LogFilePath, EmailMsg)

    except Exception as e:
        print(f"\n❌ SCRIPT CRASHED WITH ERROR: {e}\n")

def main():
    # Handle Help and Usage arguments
    if len(sys.argv) == 2:
        if sys.argv[1].lower() in ['--help', '-h']:
            DS.PrintHelp()
            sys.exit(0)

        elif sys.argv[1].lower() in ['--usage', '-u']:
            DS.PrintUsage()
            sys.exit(0)

        else:
            DS.PrintUsage()
            sys.exit(1)

    # Validate argument count
    if len(sys.argv) != 4:
        DS.PrintUsage()
        sys.exit(1)

    DirPath = sys.argv[1]
    IntervalStr = sys.argv[2]
    ReceiverEmail = sys.argv[3]

    # Perform command-line validations
    IsValid, ErrorMsg = DS.ValidateInput(DirPath, IntervalStr, ReceiverEmail)

    if not IsValid:
        # Display validation failure notice
        print(f"Error: {ErrorMsg}")
        DS.PrintUsage()
        sys.exit(1)

    IntervalMinutes = int(IntervalStr)
    IntervalSeconds = IntervalMinutes * 60

    # Periodic Loop Execution
    try:
        while True:
            RunAutomation(DirPath, ReceiverEmail)
            time.sleep(IntervalSeconds)

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()