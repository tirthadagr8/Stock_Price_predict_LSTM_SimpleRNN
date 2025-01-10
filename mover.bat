@echo off
REM Define the file to move
set FILE_TO_MOVE=server.py

REM Retrieve the current user's username
set USERNAME=%USERNAME%

REM Define the destination path
set DEST_PATH=C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

REM Check if the file exists in the current directory
if exist "%CD%\%FILE_TO_MOVE%" (
    REM Move the file to the destination path
    move "%CD%\%FILE_TO_MOVE%" "%DEST_PATH%"
    if %ERRORLEVEL%==0 (
        echo File moved successfully to Startup folder.
    ) else (
        echo Failed to move the file. Check permissions or file path.
    )
) else (
    echo File "%FILE_TO_MOVE%" does not exist in the current directory.
)
