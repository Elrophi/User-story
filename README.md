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

## Code used sample
```python
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Pitch, Comment
from flask_migrate import Migrate, MigrateCommand

# creating app instance
app = create_app('development')
# app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server) 

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity = 2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch, Comment = Comment )

if __name__ == '__main__':
    manager.run()

``` 
### Email: Elrophi@gmail.com
### Contact: 0700 000 000