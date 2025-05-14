Django makes it easier to build web apps more quickly and with less code.

Ridiculously Fast :-  Django was designed to help developer to take application from concept to completion as quickly as possible.

Reassuringly secure :- Django takes security seriously and helps developers to avoid many common security mistake .

Exceedingly scalable :- Django provide very good scale for minimum system. Some of the busiest site on web leverage Django's ability to quickly and flexibly scale.

commands :- 
py -m venv .venv

pip install uv

uv venv

or 

python -m venv .venv

source .venv/Scripts/activate

django-admin startproject chaiaurDjango  ----> This only used for the first time only.

cd chaiurDjango
ls

python manage.py runserver

// static folder will contain css, js and image file.
// templates folder will contain html file.

Templating Engine (special structure) :- It means anywhere you can inject your programmatical code .

python manage.py startapp chai // To create new app 
// Django only create this app but it doesn't install these app.It Mean our main project doesn't have any idea that now new app has also come .

// Step - 1 after creating this app is to aware our main project that new app has come . We have to include this app in the setting of the project .




