# Employee_django
Deployment of Employee based project using Django, SQLite and HTML (no CSS)

This is my first ever project made using Django!!!
It consists of an employee table which was done using SQLite.
It allows adding new employees and their details such as their name, branch, email-id and salary.
I'll add one more feature of removing the data of an employee/employees.

There is no front-end in this yet, I have to work on it.
But we can add CSS on this using tailwind, it would be quick and better for fast deployment.

I'm listing the commands that I used for this project:

mkdir employee_project
cd employee_project
python -m venv venv

To activate the virtual environment(FOR MAC):
source venv/bin/activate     

pip install django

To install SQL server:
pip install pyodbc
pip install django-mssql-backend

To create Django project and App:
django-admin startproject mysite .
python manage.py startapp employee

After this edit mysite/settings.py and employee/models.py

To make migrations and to migrate:
python manage.py makemigrations
python manage.py migrate

Edit employee/views.py
Add urls to employee/urls.py and mysite/urls.py

Create this folder: employee/templates/employee/ and edit list.html, add.html

To run the server:
python manage.py runserver
