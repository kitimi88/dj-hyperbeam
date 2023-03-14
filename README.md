# Django Hyperbeam


### A collection of basic Django web applications for beginners.

> ### Features
* Blog
* Polls
* Feedbacks/Contact Us
* Custom user profile
* Azure deployment ready

>### Important

By default, I'm using PostgreSQL however, you can edit the DATABASES configuration in the ```settings.py``` according to your preference.

Create ```.env``` file in your main directory with the ff. configs:

* ```APP_SECRET_KEY=[Your_App_Secret_Key]```
* ```DBNAME=[Your_Database_Name]```
* ```DBHOST=[Your_Database_HostName]```
* ```DBUSER=[Your_Database_Username]```
* ```DBPASS=[Your_Database_Password]```

SECRET KEYS should be kept SECRET. For best practices, create a new secret key using the ff. script:

`` from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())``


Keep in mind that development and production settings are configured separately but can be defined in the ```.env``` file.

>### Usage
Some words
>### Installation
Some instructions
