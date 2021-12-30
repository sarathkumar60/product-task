# product-task
#A step by step list of commands / guide that informs how to install this project.

# create a virtual environment
$ virtualenv project-env
$ source project-env/bin/activate

git clone https://github.com/sarathkumar60/product-task

cd product-task/product-task

# install requirements
$pip install -r requirements.txt

# run the migrations to create sqllite database
$ python manage.py migrate

#Starting the webserver
$ python manage.py runserver

#Running tests
$ ./manage.py test


# Screenshots


