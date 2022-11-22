# Twitter API Backend

# To do, steps below are for testing on local database we need to have a online database, but for now this is testing
```
Steps

-pip install -r requirements.txt
-mkvirtualenv twitterbackend
-pipenv shell
-pip install django
-psql -d postgres
-CREATE DATABASE twitterbackend;
-CREATE USER twitterbackenduser WITH PASSWORD 'password';
-GRANT ALL PRIVILEGES ON DATABASE twitterbackenduser TO twitterbackenduser;
-pip install psycopg2-binary
-twitterbackend;
-pip install djangorestframework
```

##### Links

```
Admin: http://localhost:8000/admin/

API Root: http://localhost:8000/

Get Users: http://localhost:8000/user/

Get Users By ID: http://localhost:8000/user/ID

Get Posts: http://localhost:8000/post/

Get Posts By ID : http://localhost:8000/post/id

Get Comments: http://localhost:8000/post/

Get Comments By ID: http://localhost:8000/post/id

fetch Object by diff params coming soon...
```
