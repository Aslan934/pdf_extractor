# Asynchronous pdf extractor API
Asynchronous pdf extractor api with django-rest framework and celery/rabbitmq worker, protected with JWT authentication

When we upload a PDF file to the `/api/v1/create` endpoint, this file is sent to the Celery in the backend and the record id that is linked to the authorized user id is returned and processing starts asynchronously. The file's content is extracted and saved to database. Celery storage is RabbitMQ. Also, you can use `/api/v1/check/:id `endpoint to track the status. If processing has been finalized then it returns the content that was extracted from the document.

List of endpoints:
* /api/v1/auth → JWT authorization
* /api/v1/refresh → JWT token refreshment
* /api/v1/create → as a POST payload this endpoint will receive the .pdf file and document name
* /api/v1/check/:id → get the status of processed file
* /api/v1/search → FULL TEXT search from extracted contents (optional)

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


