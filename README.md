# A collection of basic Django web applications for beginners.


## Applications
- Blog
- Polls
- Feedbacks/Contact Us
- Custom user profile
- ChatGPT

## Requirements
- Python 3.10.8 or later
- PostgreSQL database (version 11 or later)
- Django 4.0 or later
- Your preferred web browser
- Git

## Installation
1. Clone reporsitory.

```bash
$ git clone https://github.com/kitimi88/dj-hyperbeam.git
```

2. Setup virtual environment.

```bash
$ py -m venv .venv
$ .venv\scripts\activate
```

3. Install required dependecies.

```bash
$ py -m pip install -r requirements.txt
```
4. Setup database and apply migration.

```bash
$ py manage.py makemigrations
$ py manage.py migrate
```

5. Start development server.

```bash
$ py manage.py runserver
```
---
### Note
_Define your preferred configuration in the ```env.example.txt``` and save it as ```.env```. Learn more about [python-dotenv](https://pypi.org/project/python-dotenv) and [django-environ](https://pypi.org/project/django-environ/)._

_Should you need a new SECRET_KEY, run ```gen_secret_key.py```._

---

### References and documentations

* [Django](https://docs.djangoproject.com/en/4.1/)
* [Bootstrap](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Git for Windows](https://gitforwindows.org/)
* [Openai (API Reference)](https://platform.openai.com/docs/api-reference)
* [Django with PostgreSQL in Azure](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows&pivots=deploy-portal)

---
## Contributions
_Pending contribution guide._
***
## License
_Pending_

