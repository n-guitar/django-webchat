# django-webchat

## setup

```bash
$ python -V
Python 3.9.1
$ python -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

## create project

```bash
$ django-admin startproject config .
$ django-admin startapp webchat
$ python manage.py runserver
```

# branch

| branch name                                                                      | overview                                       |
| -------------------------------------------------------------------------------- | ---------------------------------------------- |
| [simple-webchat](https://github.com/n-guitar/django-webchat/tree/simple-webchat) | webchat サンプル room 毎にブロードキャストする |
