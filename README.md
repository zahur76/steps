# DJANGO FILTERS TUTORIAL

## TABLE OF CONTENT 
* [Introduction](#introduction)    
* [Technologies used](#technologies-used)
* [Environmental Variables](#environmental-variables)
* [Django Filters](#django-filters)
* [References](#references)


## INTRODUCTION

Tutorial on how to implement django filters in DRF with the aim of using it on other projects.
Also implements openAPI documentation

## TECHNOLOGIES USED

* python 3.6.9
* Django 3.2.16
* django-rest-framework=0.1.0
* drf-spectacular==0.25.1
* django-filter==21.1

## Environmental Variables

* Set secret key in home/bashrc file: ``` export SECRET_KEY= **** ``` or use env.py
* activate with source ~/.bashrc


## DJANGO FILTERS

* ``` pip install django-filters  ```
* add ``` django-filters ``` to app in settings.py
* update setting REST_FRAMEWORK to include ``` 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'] ```
* create filter classes
* add filter class to view


## References

* https://django-filter.readthedocs.io/en/latest/index.html




