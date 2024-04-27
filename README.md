# Time Management on Google Calendar

Manage time on your calendar by adding events directly from your terminal and committing them to a database later.

## Guide

Follow these steps to set up and manage time on your calendar:

1. **Create a Google Cloud Project:** Visit [console.cloud.google.com](https://console.cloud.google.com/) and create a new project.
2. **Enable Google Calendar API:** Navigate to APIs and Services and enable the Google Calendar API.
3. **Configure OAuth Consent Screen:** Go to OAuth consent screen and follow the instructions. Add all Google Calendar scopes.
4. **Add Test Users:** Add yourself as a user for the application by adding your email in the "test users" section.
5. **Create OAuth Credentials:** Go to Credentials and create credentials. Choose OAuth client ID and then choose desktop app. Create and download credentials.json.
6. **Move Credentials:** Move the credentials.json file to the same folder where the TimeManager.py script is located.

## Configuration

Configure the TimeManager.py script by following these steps:

1. Fill the spots marked on the TimeManager.py file with your time zone and calendar id (you can get that from your calendar).

## Database Setup

To set up the database, follow these steps:

1. Run CreateTable.py once to generate the hours.db file (all your commits will be found there).

## Execution

Follow these steps to execute the TimeManager.py script:

### 1. Install requirements:

Make sure you have Python updated first.

```bash
pip install -r requirements.txt
```

### 2.Execute the TimeManager.py script :

python TimeManager.py add hours and " Enter Description" 

**Example:**

```bash
python TimeManager.py add 2 "Coding"
```

### 3.Commit your time spent to a Database:

```bash
python TimeManager.py commit
```

### Optional Configuration

For added convenience, you can follow these optional steps:

1. Add the credentials.json to your root folder.
2. Make the TimeManager.py executable.
3. Add an alias to it on your "bashrc" file so that you can run the commands above from your terminal directly.

**We welcome contributions from the community! Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvement.**






