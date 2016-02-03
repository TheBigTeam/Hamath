***

# Prerequisites

**First things first, make sure you have [pip](https://github.com/TheBigTeam/hamath-workspace/wiki/pip-installation), [python](https://github.com/TheBigTeam/hamath-workspace/wiki/python-installation), and [github](https://github.com/TheBigTeam/hamath-workspace/wiki/github-setup) installed and working properly. If not, don't sweat it, check out the [**wiki's**](https://github.com/TheBigTeam/hamath-workspace/wiki) for installation instructions**


***

## Virtual Environment Setup

Make a new virtualenv in desired location: ```virtualenv yourprojectname-workspace```

The ```yourprojectname-workspace``` directory isolates our libraries and contains the local github repository.

**How To Use:**

Activate the virtualenv: ```source /bin/activate```

The virtualenv can be deactivated: ```deactivate```

## Setup Local Repository

Now, from inside our activated virtual enviroment (*yourprojectname-workspace*), pull down code from github with the following terminal commands:
```
git init
git remote add origin https://github.com/TheBigTeam/yourprojectname-workspace
git pull origin master
```
You will get two projects: 
* **hamath**: is the class project
* **mysite-example**: is a django sample website described [**here**](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)

or create your own django project with ```django-admin startproject mysite```

## Project Setup

Install Requirements: ```pip install -r requirements.txt```

Navigate to: ```/yourprojectname-workspace/yourprojectname/yourprojectname```

Run the server: ```python manage.py runserver```

Open website in browser at http://localhost:8000 or admin at http://localhost:8000/admin (admin:admin)



