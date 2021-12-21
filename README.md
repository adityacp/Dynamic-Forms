Dynamic-Form
============


Introduction
^^^^^^^^^^^^

This is a project to create dynamic forms using a CSV file

Requirements
^^^^^^^^^^^^

This project requires mongodb as the database backend.

- Python 3.8.10
- Django 4.0
- djongo 1.3.6

Installation
^^^^^^^^^^^^
  
-  Clone the repository

   ::

     git clone https://github.com/adityacp/DJRTSHARE.git

-  Go to the project directory

   ::

     cd DJRTSHARE


- Installing project packages

  ::

     pip install -r requirements.txt


- Run migrations
  
  ::
     
     python manage.py makemigrations 
     python manage.py migrate


- Run server Locally
      
  ::

     python manage.py runserver


API Endpoints
^^^^^^^^^^^^^

- Form Creation Post API

  ::
  
     http://127.0.0.1:8000/api/form
     
     Request data: {"form_name": <Form name>, "csv_file": <CSV File>}
     Response data: 
- Form Update Post API
- Form deletion Delete API
- Form Response Get API
- Form Repsonse Post API
