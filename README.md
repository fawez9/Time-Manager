# Time-Manager
Manage Time on your Calendar by adding it directly from ur terminal and commiting it to a database later

GUIDE:

1) visit "console.cloud.google.com/" and create a project

2) go to apis and services and enable it also search for google calendar api and enable it

3) go to ouath consent screen and follow the instructions , add all google calendar scopes

4) add yourself as a user for the application by adding your email in the "test users"

5) go to credentials and create credentials choose oauth client id and then choose desktop app , create and download credentials.json


6) move that file to the same folder where the TimeManager.py 

7) you need to fill the spots marked on the TimeManager.py file by your time zone and calendar id (you can get that from your calendar)


8) you'll need to run CreateTable.py once to generate the hours.db file (all your commits will be found there)


9) install requirements: pip install -r requirements.txt (make sure you have python updated first)


10) now you can execute the TimeManager.py script and add or commit your time spent : example(python TimeManager.py  add 2 "Coding") <--- python TimeManager.py add hours and "description" or python TimeManager.py commit


11)you can also add the credentials.json to your root folder and make the TimeManager.py  executable , add an alias to it on your "bashrc" file so that you can run the commands above from your terminal directly 


