# Django Geo Chile 🇨🇱

Models and management command to load Chile's Administrative Geographical data from official source.

## Getting Started 

### 1) Download package

Using poetry

    poetry add django_geo_chile

Using pipenv

    pipenv install django_geo_chile

Using pip
    
    pip install django_geo_chile


### 2) Add to settings

In `settings.py` add `geo_chile` to `INSTALLED_APPS`


    INSTALLED_APPS = [
        ...
        "geo_chile",
    ]

### 3) Create database tables

In terminal run:

    python manage.py migrate



### 4) Load data

In terminal run:

    python manage.py load_geo_chile_data


### 5) Drink Wine 🍷 
