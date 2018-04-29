# shortcrux

## Requirements
Django 1.11
You can install all the dependencies using :

`pip install -r requirements.txt`

## Setup

1. Download the repositary
```
git clone https://github.com/kurianbenoy/Ibeto-project.git
```

2. Install the requirements
```
cd Ibeto-project
sudo apt-get install python3-pip
pip3 install pipenv
pipenv --python 3
pipenv install -r requirements.txt
```

3. Run the project
```
pipenv shell
python3 manage.py makemigrations && python3 manage.py migrate
python3 manage.py runserver
```

