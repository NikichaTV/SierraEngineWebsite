#!/usr/bin/env python3

import os
import datetime

CURRENT_DIRECTORY: str = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
ROOT_DIRECTORY: str = CURRENT_DIRECTORY + '../'

def Main() -> None:
    UpdateReadMe()

def UpdateReadMe() -> None:
    SOURCE_FILE_EXTENSIONS: [str] = ['.cpp', '.h', '.mm', '.cs', '.py', '.cmake', '.glsl', '.vert', '.frag', 'comp', '.geom', '.tesc', '.tese', '.sh', '.bat']

    # Define initial line count
    linesOfCode: int = 0

    # Loop through all project files and check if the current file is a source file
    for subdirectory in ['src/', 'templates/', 'static/', 'scripts/']:
        for root, dirs, files in os.walk(ROOT_DIRECTORY + subdirectory):
            for file in files:
                for extension in SOURCE_FILE_EXTENSIONS:
                    if str(file).endswith(extension):
                        with open(os.path.join(root, file), 'r') as file:
                            for count, line in enumerate(file):
                                pass
                            linesOfCode += count + 1
                            file.close()

    with open(ROOT_DIRECTORY + 'README.md', 'r+') as file:
        # Count README.md's lines as well (gotta look like there's a lot of code, innit :D) and write total count & date
        for count, line in enumerate(file):
            pass
        linesOfCode += count + 1
        file.seek(0)

        # Get old README.md file data
        readMeData: str = file.read()

        index: int = readMeData.index('<p align="center" id="LineCounter">')
        readMeData = readMeData[0:index]

        # Get current date
        now = datetime.datetime.now()
        updated: str = f'{now.day:02}/{now.month:02}/{now.year:02}'

        # Apply date and line count changes
        linesOfCodeString: str = f'{linesOfCode:,}'
        linesOfCodeLine: str = f'<p align="center" id="LineCounter">Total lines of code: { linesOfCodeString }</p>\n'
        lastUpdatedLine: str = f'<p align="center" id="LastUpdated">Last updated: { updated } </p>\n'

        # Get new data and write to README.md file
        newReadMeData = readMeData + linesOfCodeLine + lastUpdatedLine + '\n' + ('-' * 171)
        file.seek(0)
        file.write(newReadMeData)
        file.close()

# We use a try here, as this script is called from a CMake file, which we do not want the build to crash together with this script
try:
    Main()
except Exception as e:
    print("UpdateProject.py failed: " + str(e))