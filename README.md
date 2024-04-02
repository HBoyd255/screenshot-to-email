# Screenshot to Email

This is just a simple script that takes a screenshot and sends it as an email.
The purpose of the script is to quickly add a screenshot to my Todoist inbox.

## Implementation

The original plan was to use the Todoist API, but this was to hard to upload a
file as a comment. So I decided to send the file as an email to my Todoist
inbox.

The plan was then to use `pyinstaller` to create an executable that could be
called from a hotkey. This worked, but the program took 8.5 seconds from the
hotkey being pressed to the screenshot being captured.

In the end I decided to use a VBS script to call a batch file that would call
the program. This reduced the time to 2 seconds.
