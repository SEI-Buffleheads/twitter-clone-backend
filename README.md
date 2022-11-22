# Twitter API Backend

# To do, steps below are for testing on local database
# we need to have a online database, but for now this is testing
-mkvirtualenv twitterbackend
-pip install django
-django-admin startproject twitterapi
-psql -d postgres
-CREATE DATABASE twitterbackend;
-CREATE USER twitterbackenduser WITH PASSWORD 'password';
-GRANT ALL PRIVILEGES ON DATABASE twitterbackenduser TO 
-pip install psycopg2-binary
-twitterbackend;
-django-admin startapp twitterapi
-pip install djangorestframework

# Now go to shell

-pipenv shell

# setting configurations
-add to database settings, this needs to be altered later,
-create superuser locally, then login
```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twitterbackend',
        'USER': 'twitterbackenduser',
        'PASSWORD': 'password',
        'HOST': 'localhost'
    }
```



### Admin

```
http://localhost:8000/admin/

```

##### Get Requests

```
API Root: http://localhost:8000/

Get Users: http://localhost:8000/user/

Get Users By ID: http://localhost:8000/user/ID

Get Posts: http://localhost:8000/post/

Get Posts By ID : http://localhost:8000/post/id

Get Comments: http://localhost:8000/post/

Get Comments By ID: http://localhost:8000/post/id

fetch Object by diff params coming soon...
```
