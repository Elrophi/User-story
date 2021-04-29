An app that allows users to pitch a topic and get votes on them and feeback.
>## Author: [El-rophi Skwaila](https://github.com/Elrophi/User-story)


---

>## Description
### THis is a simple app to pich a topic and vote on it. Users have the ability to create as many, login and save their work
---

## Technology Used: 
>Bootstrap

>Python

>Flask

---
>## Installation and setup locally
## Pre-requisites
- Python3
- Virtual environment
- bootstrap
- flask


---
>## Cloning and opening on compiler
#### On your terminal run

    $ git clone https://github.com/Elrophi/User-story.git
    $ cd user-story
    $ code .


##  Setting up the virtual environment and activating it
    $ python -m venv <name of virtual environment>
    $ source <name of virtual environment>/bin/activate

##  Install flask and modules needed
       $ python3 -m pip install flask
       $ python3 -m install flask-bootstrap
       $python3 -m install flask-script

## Creating the start.sh file to tun the app
 - Create a file and name it start.sh
 - in the file add this

       export SECRET_KEY=<you api key>
       python3 manage.py server


## Run the app now
On your terminal run

        $ chmod +x start.sh
        $ ./start.sh

## Test the application

        $ python3 manage.py test        
heroku addons:create heroku-postgresql