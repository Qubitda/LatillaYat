python -m venv env
env\Scripts\activate.bat

python -m ensurepip --upgrade
python -m pip install --upgrade pip

pip install -r requirements.txt

python -m pip install Django
python -m pip install colorama
pip install django-import-export
pip install psycopg2

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

DATABASES = {'default':
                 {'ENGINE':"django.db.backends.postgresql",
                  "NAME":"budget",
                  "USER":"postgres",
                  "PASSWORD":"1",
                  "HOST":"localhost",
                  "PORT":"5432"}
             }
