# Report Extraction Script

This script is designed to automate the process of migrating report directories from one location to another within a structured file system. It is particularly useful for organizing and transferring reports from an external source to a centralized destination.

Overview
The script performs the following steps:

1. Source Path Setup: Defines the path to the source directory where subject folders and their corresponding reports are located.
Destination Path Setup: Defines the path to the destination root directory where the reports will be copied.

2. Subject Path Identification: Identifies and constructs paths for each subject folder in the source directory.

3. Report Directory Copy: For each subject, it locates the report directory and copies its contents to the corresponding destination directory, creating any necessary folders along the way.

Prerequisites
- Python 3.x
- os and shutil modules (included in the standard library)

Usage
1. Set the path variable to the root directory containing subject folders with reports.

2. Set the destination_root variable to the target root directory where reports will be copied.

3. Run the script. It will automatically create the necessary directories and copy the report files.
