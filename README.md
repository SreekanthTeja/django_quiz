# Project running into local machine
```ssh
    $ git clone https://github.com/SreekanthTeja/django_quiz.git
    $ virtualenv -p python3.7 env
    $ source env/bin/activate 
    $ pip install -r <project_name>/req.txt 
    $ cd <project_name>
    $ python manage.py runserver
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
```