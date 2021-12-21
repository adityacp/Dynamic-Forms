Dynamic-Form
============


## Introduction


This is a project to create dynamic forms using a CSV file

## Requirements


This project requires mongodb as the database backend.

- Python 3.8.10
- Django 4.0
- djongo 1.3.6


## Installation

  
-  Clone the repository

     git clone https://github.com/adityacp/Dynamic-Forms.git

-  Go to the project directory

     cd Dynamic-Forms

- Installing project packages

     pip install -r requirements.txt

- Run migrations

     python manage.py makemigrations
     
     python manage.py migrate

- Run server Locally
     
     cd dynamic_form
     
     python manage.py runserver


## API Endpoints

- Form Creation Get API
  
  POST http://127.0.0.1:8000/api/form/(form_id)

  Response data: {"status": (success or failed), "form_data": {"form_id": (form_id), "form_name": (form_name), "fields": (form_fields)}}

- Form Creation Post API
  
  POST http://127.0.0.1:8000/api/form
     
  Request data: {"form_name": (Form name), "csv_file": (CSV File)}
  
  Response data: {"status": (success or failed), "form_data": {"form_id": (form_id), "form_name": (form_name), "fields": (form_fields)}}

- Form Update Post API
  
  POST http://127.0.0.1:8000/api/form/(form_id)
     
  Request data: {"form_name": (Form name), "csv_file": (CSV File)}
  
  Response data: {"status": (success or failed), "form_data": {"form_id": (form_id), "form_name": (form_name), "fields": (form_fields)}}
  
- Form deletion Delete API
  
  DELETE http://127.0.0.1:8000/api/form/(form_id)
  
  Request data: No data
  
  Response data: {"status": "success"}
  
- Form Response Get API

  GET http://127.0.0.1:8000/api/get/form/response/(response_id)
  
  Response data: {"message": (success or failed), "response": {"response_id": (response_id), "form_id": (form_id), "answers": (form_answers), "fields": (form_fields)}}
  
- Form Repsonse Post API

  POST http://127.0.0.1:8000/api/form/response/(form_id)
  
  Request data: {"answers": (answer_dict)}
  
  Response data: {"message": (success or failed), "response": {"response_id": (response_id), "form_id": (form_id), "answers": (form_answers)}}
  
  
