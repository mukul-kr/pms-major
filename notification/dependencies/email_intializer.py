import json

# import OS
import os

CreateUserEmail = json.load(
    open(os.path.join("templates", "create-user-mail.json"))
)

EventNotTriggered = json.load(
    open(os.path.join("templates", "event-not-triggered-mail.json"))
)

DataWarning = json.load(
    open(os.path.join("templates", "high-severity-warning.json"))
)
