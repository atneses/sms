# Sending Verification Algorithm
You can find a little diagram in the root directory called `Diagram.pdf`

### Requirements
* Python 3.6
* virtualenv

**How to install virtualenv**

`sudo pip3 install virtualenv`

**Create an virtual environment**

`virtualenv venv`

*Python Libraries*
* django==2.2
* djangorestframework==3.11.0
* PyYAML==5.2
* coreapi==2.3.3
* Pygments==2.5.2

**Install requirements**

pip3 install -r requirements.txt`

## How to run

### Run migration to create database

The application needs a database to save the verification codes sent it to the users.

`python manage.py migrate`

### Run the project
To run the development server of the application use the next command:

`python manage.py runserver`

This will run the developtment sever in the host: **localhost:8000** or **127.0.0.0:8000**

### Create superuser for access Django Admin (OPTIONAL)
Run the next command and follow the steps to create a superuser
`python manage.py create superuser`

To access django admin use the next URL: **localhost:8000/admin** or **127.0.0.0:8000/admin**


## Auto generated API documentation
Using Django Rest Framework the application generate automatically it's own API documentation,
to access to the documentation use the next URL: ****localhost:8000/api/docs** or **127.0.0.0:8000/api/docs****
