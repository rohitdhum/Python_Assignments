# Duplicate File Removal Automation

## 1. Project Title
**Duplicate File Removal Automation**

## 2. Project Description
This Python automation system periodically scans a specified directory and its subdirectories to detect duplicate files based on content checksums (MD5) rather than file names. Upon finding duplicate copies, it retains the primary file, deletes all remaining duplicate files, generates a comprehensive timestamped log file, and automatically transmits an email with operation statistics and the attached log file to a specified recipient address.

## 3. Features
* **Recursive Directory Scanning**: Discovers files across all subdirectories.
* **Checksum-based Detection**: Uses MD5 hashing to safely verify identical file contents.
* **Automatic Deletion**: Retains the original instance and deletes duplicate entries.
* **Timestamped Logging**: Creates structured log files named after the execution time.
* **Periodic Scheduled Execution**: Automates tasks to run continuously at specified intervals.
* **Email Notification & Attachments**: Automatically sends operational summaries and attachments via SMTP.
* **Rigorous Input & File Validations**: Validates paths, formats, access rights, and inputs before execution.
* **Robust Exception Handling**: Prevents crashes from broken paths, read/write permission errors, or network issues.
* **Modular Codebase**: Keeps helper actions and main logic distinctly separated.

## 4. Requirements
* **Python Version**: Python 3.6 or higher
* **Required Standard Libraries**: `os`, `sys`, `re`, `time`, `hashlib`, `smtplib`, `datetime`, `email`
* **Network**: Active internet connection for email transmission
* **SMTP Credentials**: Standard email login or App Password enabled for Gmail

## 5. Project Structure
```text
.
├── DuplicateFileRemoval.py   # Main entry point; handles CLI arguments, scheduling, and loop control.
├── DuplicateServices.py      # Core service module containing scan logic, emailer, and validation functions.
└── README.md                 # System overview and operational instructions.


6. Command-Line Options:
The main script accepts three positional command-line arguments:
DirectoryPath (String): Absolute path to the directory you want to scan.
IntervalInMinutes (Integer): Scanning frequency interval (must be greater than 0).
ReceiverEmail (String): Valid email address where log reports will be delivered.

7. Execution Command:
python DuplicateFileRemoval.py C:\Users\SAWARIYA SETH\Desktop\Python37\Assignments\Demo 50
rohit45dhumal@gmail.com

8. Help Command:
python DuplicateFileRemoval.py --help

9. Usage Command:
python DuplicateFileRemoval.py --usage

10. Log-File Information: 
Storage Location: Log files are generated inside a dedicated directory named Marvellous/ located in the current working directory.
Filename Generation: The log filename is dynamically generated using the system timestamp at the start of execution:
Filename Pattern: DuplicateRemovalLog <DD> <MM> <YYYY> <HH> <MM> <SS>.log
Example: Marvellous/DuplicateRemovalLog 24 07 2026 23 30 15.log

11. Email Configuration:
Secure Credential Handling:
Sender credentials should never be committed to version control systems or hard-coded into public code repositories.
Use Environment Variables or secure configuration files to load credentials at runtime.
For Gmail accounts, generate and use an App Password under Google Security Settings instead of your primary account password.

(Place DuplicateFileRemoval.py and DuplicateServices.py in the same working directory.
Open DuplicateServices.py and update the email variables:
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password")

12. Important Notes:
Irreversible Deletion: Deleted duplicate files are permanently removed and may not be recoverable from the Recycle Bin/Trash.
Perform Initial Tests: Always test the automation on a sample or backup directory prior to processing critical files.
Avoid Hardcoded Secrets: Do not hardcode raw email passwords directly inside source files.
Preserve Original File: The system preserves the first file encountered from each duplicate group during traversal and deletes subsequent copies.
Strict Duplicate Definition: Files are considered duplicates only when their MD5 checksums are completely identical, regardless of filename or extension differences.