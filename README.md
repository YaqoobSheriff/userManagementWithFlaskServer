# userManagementWithFlaskServer

This repo consists of a flask server which invokes the PowerShell scripts for user creation, user deletion, user password reset, book a user slot and remove a user slot..
Based on the API request made.

Before you run the Flask server install the following modules.
pip install flask
pip install requests

This script can be used for bulk user creation at a very faster pace.
It is observed that 1000 users can be created within a minute.

API POST request cab be made as follows,

POST: http://localhost:8006/create

JSON Data:

{
    "users": [
        {
            "employeeUsername": "user1",
            "employeePassword": "password@1",
            "domainName": "test.com"
        },
        {
            "employeeUsername": "user2",
            "employeePassword": "password@1",
            "domainName": "test.com"
        }
    ]
}
