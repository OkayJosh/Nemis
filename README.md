## Welcome to NEMIS

Better Education Service Delivery [editor on GitHub]# Django setup
> Make sure you have django install on your system else else [django](https://django.org).

```bash
#This is the compulsory
pip3 install django

```
> Make sure you install djangorestframework

```bash
#This enable us to use django as a backend to power our application
pip3 install djagorestframework

```
> Then you run migrations like so:

```bash
# making migrations
python3 manage.py makemigrations

python3 manage.py migrate

```
> Creating a super user and follow the prompt

```bash
#creating a super user to login from 127.0.0.1:8000/admin
python3 manage.py createsuperuser

```
> Running the application

```bash 
#running the server at port 8000
python3 manage.py runserver

```



# Vue for Frontend

> Make sure you have vue-cli installed [Vue](https://vuejs.org/)

## Setup

``` bash
changing directory
cd frontend 
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run serve

```
## Finally
> Both servers must be running 

## Built with
- [Vue](https://vuejs.org/) - A progressive JavaScript framework
- [django](https://django.org/) - The python webframework for developers with a deadline