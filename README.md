# Encyclopedia
> In this project I designed a Wikipedia-like online encyclopedia.
## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
The purpose of this project is to implement an online encyclopedia that consists of entries written in markup language.

## Screenshots
![Screenshot1](https://user-images.githubusercontent.com/61382735/98668871-c9819280-2350-11eb-9b7d-b62e7b3c0007.png)
![Screenshot2](https://user-images.githubusercontent.com/61382735/98668957-eae27e80-2350-11eb-804d-3ccc753f96ae.png)
![Screenshot3](https://user-images.githubusercontent.com/61382735/98669017-09487a00-2351-11eb-8d9e-43af6744fa71.png)

## Technologies
* Python - version 3.6
* Django - version 3.1
* Markdown2
* Bootstrap4

## Setup
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

Create .env file such as: 
```
DJANGO_OLD_SECRET_KEY=<your_old_django_secret_key>
DJANGO_SECRET_KEY=<your_django_secret_key>
```

```
python manage.py runserver

```
See your website at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Features
* Create, edit, view entries in the encyclopedia
* Search encyclopedia for a particular entry
* Render a random entry

To-do list:
* improve design 
* improve functionality, in particular put the entries into the database.

## Status
Project is paused, because it fullfills the requirements of the course, but some changes to be done to improve functionality and design.

## Inspiration
This project is part of the Harvard course I am taking, in particular CS50’s Web Programming with Python and JavaScript, project 1 - wiki.

## Contact
Created by [Lena Struts](https://www.linkedin.com/in/lena-yeliena-struts-5aa96292/) - feel free to contact me!