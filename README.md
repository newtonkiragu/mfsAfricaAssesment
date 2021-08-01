# MFS Africa Assessment

## Description
An application interface that receives a string of comma separated points and calculates the closest points.

#### Link to deployed site
http://pasteb1n.herokuapp.com/

## Table of content
1. [Description](#description)
2. [API endpoints](#endpoints)
3. [Setup and installations](#setup-and-installations)
4. [Testing](#testing)
7. [Contact me](#support-and-contact-details)
8. [Licensing](#license)

## endpoints
API Endpoint | Description | Request
---- | :---- | :----- |
http://mfsafrica-karanu.herokuapp.com/points/ | Display a JSON object containing all comma separated points | GET
http://mfsafrica-karanu.herokuapp.com/points/ | Create a new list of points | POST
http://mfsafrica-karanu.herokuapp.com/points/<id>/ | Display a JSON object of a specific point containing the calculation of the closest point | GET
http://mfsafrica-karanu.herokuapp.com/points/<id>/ | Edit a comma separated point | PUT
http://mfsafrica-karanu.herokuapp.com/points/<id>/ | Delete a comma separated point | DELETE

## Setup and installations

#### Prerequisites
1. [Python3.9](https://www.python.org/downloads/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
5. [Django](https://www.djangoproject.com/download/)
5. [Django Rest Framework](http://www.django-rest-framework.org/#installation)

#### Technologies used
    - Python 3.9
    - Heroku
    - SQLite
    - Django, Django Rest Framework

#### Clone the Repo and checkout into the project folder.
```shell
git clone git@github.com:newtonkiragu/mfsAfricaAssesment.git && cd mfsAfricaAssesment
```

#### Create and activate the virtual environment
```shell
python3.9 -m virtualenv virtual
```

```shell
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
DEBUG=True
DISABLE_COLLECTSTATIC=1
```

#### Install dependencies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`


#### Run migrations
```shell
python3.9 manage.py migrate
```

#### Run the app
```shell
python3.9 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Testing
To run the tests, run
```shell
python3.9 manage.py test
```

## Support and contact details
Contact [Newton Karanu](karanunewton4@gmail.com) for further help/support

### License
MIT

Copyright (c) 2021 **Newton Karanu**
