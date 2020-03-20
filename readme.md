# Install Python3, pip and Django
https://docs.djangoproject.com/en/3.0/topics/install/#installing-official-release
## Install crispyforms for bootstrap integration
`pip install django-crispy-forms`
## Create migration files for the database
Open the folder corona_survival and you see some files and one that is named `manage.py`
Now u can open a terminal and enter: `python manage.py makemigrations`
Then type: `python manage.py migrate` and the database gets created
## Create superuser for our page
Enter: `python manage.py createsuperuser` to create an admin for our page and enter the credentials u like.
## Start the server
`python manage.py runserver`
