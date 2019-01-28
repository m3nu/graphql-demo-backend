# GraphQL Demo App

A minimal Django app that implements the example from [How to GraphQL](https://www.howtographql.com/basics/2-core-concepts/).

## Install

1. Install required packages (in virtualenv)
```
$ pip install -r requirements.txt
```

2. Set up database (sqlite)
```
$ python manage.py migrate
```

## Run
```
$ python manage.py runserver
```

The GraphqiQL web interface should now be available from [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
