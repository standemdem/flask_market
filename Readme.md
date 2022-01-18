# Welcome to FlaskMarket App!

This is a project made following the youtube guide [Flask Lesson - Created by JimShappedCodding](https://www.youtube.com/watch?v=Qr4QMBUPxWo)

You can find the online version I deployed with Heroku at
[https://flask-market-place.herokuapp.com/](https://flask-market-place.herokuapp.com/)

## How to run the project locally ?

The projects comes with a requirements.txt file

- Open a terminal
- Clone project
- `cd market` (get into flaskmarket folder)
- `python -m venv . ` (creates a new virtual environment)
- `venv source/bin/activate` (activate the virtual env)
- `pip install requirements.txt` (install all the required packages and more, since I did a poor job of cleaning the file ... )
- `flask run`

That'is it !

## What is this project about ?
The objective was to learn several things:
- Flask 
	- Jinja syntax
	- Forms
	- Flash messages
	- Login / logout / register
- SQLAlchemy
	- Creatign a db
	- Creating tables
	- writting to a table
	- deleting info from a table
	- updating info from a table 
- Deploying an app on HEROKU (Procfile at the root of project)

## Things I still need to fix in this project

The tutorial didn't take in consideration the one to many relationship between a product and the owners.
**Here, one item can only be owned by one owner**

Since I tweeked the author's code to still display the full list of items even when one item has been bought, it leads to some errors. Be aware of that if you want to visit the website
