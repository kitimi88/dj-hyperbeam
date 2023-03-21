# Django Hyperbeam


### A collection of basic Django web applications for beginners.

>Features
* Blog
* Polls
* Feedbacks/Contact Us
* Custom user profile
* ChatGPT

>Important

By default, I'm using PostgreSQL for this project. However, you can manually configure the DATABASES ```settings.py```.

By default, I'm using PostgretSQL for this project. Most configurations including secrets keys, API reference, etc., are defined and set as enviroment variables in the ```.env```. 

Feel free to  edit the ```env.example.txt``` and save it as ```.env``` together with your preferred configuration. Know more about [python-dotenv.](https://pypi.org/project/python-dotenv/)

SECRET KEYS should be kept SECRET. It is considered best-practice to create large random value and by NOT relying to the system-generated even in development environment. Know more about [Django SECRET KEYS](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/#secret-key) or you may run the ```gen_secret_key.py``` 



Keep in mind that development and production settings are configured separately but can be defined in the ```.env``` file.


*** 

### Usage

>Installation

```bash
$ git clone https://github.com/kitimi88/dj-hyperbeam.git
```
>Setup virtual environment

```bash
$ py -m venv .venv
$ .venv\scripts\activate
$ py -m pip install -r requirements.txt
```
>Setup database

```bash
$ py manage.py makemigrations
$ py manage.py migrate
```
***
### References and documentations

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/download/)
* [Openai (API Reference)](https://platform.openai.com/docs/api-reference)
* [Django with PostgreSQL in Azure](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows&pivots=deploy-portal)

***

