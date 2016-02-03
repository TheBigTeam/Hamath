# Mac Setup

####

**first things first, make sure you have pip and github installed and working**

## Virtual Enviroment Setup
http://docs.python-guide.org/en/latest/dev/virtualenvs/

Install virtualenv: ```pip install virtualenv```

####

the modify your .bash_profile with ```cd ~/.bash_profile``` 

and add the following line to it: ```export PIP_REQUIRE_VIRTUALENV=true```

**pip should now only run if there is a virtualenv currently activated**

####

Make a new virtualenv in desired location: ```virtualenv hamath-workspace```

Activate the virtualenv: ```source /bin/activate```

The virtualenv can be deactivated: ```deactivate```

## Setup Local Repository

Now, from inside our activated virtual enviroment (*hamath-workspace*), pull down code from github with the following terminal commands:
```
git init
git remote add origin https://github.com/TheBigTeam/hamath-workspace
git pull origin master
```
You will get two projects: 
* *hamath*: is the class project
* *mysite-example*: is django sample website described here: https://docs.djangoproject.com/en/1.9/intro/tutorial01/

## Project Setup

Install Requirements: ```pip install -r requirements.txt```

Navigate to: ```/hammath-workspace/hamath/hamath```

Run the server: ```python manage.py runserver```

Open website in browser at http://localhost:8000 or admin at http://localhost:8000/admin (admin:admin)



# Windows Setup

####

You're on your own



