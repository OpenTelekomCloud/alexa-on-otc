# __init__.py - Starting of our application

from flask import Flask
from flask_ask import Ask, statement, question
from otc_api import vm_count

# Initialize Flask
app = Flask(__name__)

# Initialize Flask Ask and assign URL
ask = Ask(app, "/control_center")

# Set a useful response for the root 
@app.route('/')
def homepage():
    return "Open Telekom Cloud Alexa Skill"

# Set a welcome message when the skill is started    
@ask.launch
def start_skill():
    welcome_message = 'o. t. c. Control Center is online'
    return question(welcome_message)

# Define our intent and query the backend 
@ask.intent("VMCountIntent")
def share_count():
    count = vm_count()
    count_msg = 'The total number of virtual machines in your tenant is {}, at the moment {} are running and {} are stopped'.format(count[0],count[1], count[2])
    return question(count_msg)

# Define shutdown message

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'o. t. c. Control Center Shutting Down'
    return statement(bye_text)

# Main function    
if __name__ == '__main__':
    app.run(debug=True)

