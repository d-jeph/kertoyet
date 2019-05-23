# dsc
A Flask application skeleton with the boilerplate code.

## What's included? The following functionalities are included out of the box

* [Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/)
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) templating
* User accounts and permissions management
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) for databases
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for forms
* [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/) for asset management and SCSS compilation
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/) for sending emails
* Redis Queue for handling asynchronous tasks
* ZXCVBN password strength checker
* CKEditor for editing pages

## Setting up

##### Clone the repo

```
$ git clone https://github.com/d-jeph/kertoyet.git
$ cd kertoyet
```

##### Install and run [pipenv](https://docs.pipenv.org/en/latest/basics/) to create virtualenv and install dependencies

```
$ pip install pipenv
$ pipenv install
```

##### Activate the pipenv virtualenv
```
$ pipenv shell

```

##### Add Environment Variables
Flask requires the FLASK_APP environment variable to be set before running the app.
In linux run the command:

```
export FLASK_APP=manage.py
export FLASK_DEBUG=1
```

If you're on windows us:
```
set FLASK_APP=manage.py
set FLASK_DEBUG=1
```



**Other environment variables**

For the other environment variables create a file called `.env` that contains environment variables in the following syntax: `ENVIRONMENT_VARIABLE=value`.
For example, the mailing environment variables and secret key can be set as the following.
```
MAIL_USERNAME=SendgridUsername
MAIL_PASSWORD=SendgridPassword
SECRET_KEY=SuperRandomStringToBeUsedForEncryption
```

Other Key value pairs:

* `ADMIN_EMAIL`: set to the default email for the first admin account (default is `flask-base-admin@example.com`)
* `ADMIN_PASSWORD`: set to the default password for your first admin account (default is `password`)
* `DATABASE_URL`: set to a postgresql database url (default is `data-dev.sqlite`)
* `REDISTOGO_URL`: set to Redis To Go URL or any redis server url (default is `http://localhost:6379`)
* `FLASK_CONFIG`: can be `development`, `production`, `default`, `heroku`, `unix`, or `testing`. Most of the time you will use `development` or `production`.


**Note: do not include the `.env` file in any commits. This should remain private.**

##### Create the database

create a file at the root of the application named app.db then run the command:

```
$ python manage.py recreate_db
```

##### Other setup (e.g. creating roles in database)

```
$ python manage.py setup_dev
```

Note that this will create an admin user with email and password specified by the `ADMIN_EMAIL` and `ADMIN_PASSWORD` config variables. If not specified, they are both `flask-base-admin@example.com` and `password` respectively.

##### [Optional] Add fake data to the database

```
$ python manage.py add_fake_data
```

## Running the app

```
$ flask run

```
