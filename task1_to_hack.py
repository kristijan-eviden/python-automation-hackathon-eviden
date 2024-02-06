""" TASK 1: 10 points
    In this task you will try to automate the work you do in browsers. You will be using playwright codegen library to solve this task. We want to automate filling out forms, so you will be asked to write a code that will fill out one form 20 times.
    When you start playwright following steps listed below, two windows will be opened. One of your browser and other one of playwright editor. Every click you do on windowed browser will be recorded and written in code for you in playwright editor.
    That means if you just copy and run form link, fill it out and then click stop recording, you will already have the necessary code to automaticly fill out forms. After that you will just have to edit that code to in order to fill out diffrent values.
    To start the process you need to complete a couple of steps: 
    1. run: pip install playwright
    2. run: playwright install 
    3. run: playwright codegen """

""" NOTES: After you have recorded everything, try to run it once to see if it is working as intended. If the code fails at some point consider using page.wait_for_load_state('networkidle') or time.sleep()"""

""" Link to the form: https://forms.office.com/e/wkNh9uHP50 """

""" SUBTASK 1 (2 points): all forms should have their dates set to todays date """

""" SUBTASK 2 (2 points): all forms should have your full name """

""" SUBTASK 3 (2 points): all forms should have your department """

""" SUBTASK 4 (2 points): there should be at least 5 diffrent date for 'Wann benötigt' field """

""" SUBTASK 5 (2 points): there should be at least 1 form for each possible option in 'Welche Art von Anforderung übermitteln Sie heute?' (Write something funny in 'Sonstiges') """

import time