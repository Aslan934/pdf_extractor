# Asynchronous pdf extractor api
Asynchronous pdf extractor api with django-rest framework and celery worker, protected with JWT authentication

# Usage

Install dependencies
```
pip install -r requirements.txt
```

Set database
```
python manage.py makemigrations
python manage.py migrate
```
Note: I used MySql in this projects, you can change back to default Sqlite db in settings.py file before migrating

Create SuperUser
```
python manage.py createsuperuser
```

Run celery worker
```
celery -A pdfextract worker -l info --pool=solo 
```
Note: This command should be different depending on your operating system

Run Django server
```
python manage.py runserver
```


