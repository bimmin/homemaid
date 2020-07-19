FROM python:3.8.4
RUN pip install asgiref==3.2.10 \
    django-extensions==3.0.3 \
    Django==3.0.8 \
    pytz==2020.1 \
    sqlparse==0.3.1 \
    astroid==2.4.2 \
    attrs==19.3.0 \
    django-extensions==3.0.3 \
    isort==4.3.21 \
    lazy-object-proxy==1.4.3 \
    mccabe==0.6.1 \
    more-itertools==8.4.0 \
    packaging==20.4 \
    pluggy==0.13.1 \
    py==1.9.0 \
    pylint==2.5.3 \
    pyparsing==2.4.7 \
    pytest==5.4.3 \
    pytest-django==3.9.0 \
    pytz==2020.1 \
    six==1.15.0 \
    toml==0.10.1 \
    wcwidth==0.2.5 \
    wrapt==1.12.1 \
    uWSGI==2.0.19.1

RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements/local.txt
WORKDIR /app/homemaid/
RUN python manage.py migrate
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]