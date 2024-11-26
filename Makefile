
drop.db:
	PGPASSWORD=postgres dropdb --if-exists -h localhost -p 5432 -U postgres drinks-test
	PGPASSWORD=postgres dropdb --if-exists -h localhost -p 5432 -U postgres drinks-dev

create.db:
	PGPASSWORD=postgres createdb -h localhost -p 5432 -U postgres drinks-dev
	PGPASSWORD=postgres createdb -h localhost -p 5432 -U postgres drinks-test

setup-django:
	python3 manage.py makemigrations
	python3 manage.py migrate

make-migrations:
	python3 manage.py makemigrations 

run-migrations:
	python3 manage.py migrate 

create-superuser:
	DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@fiqus.com python3 manage.py createsuperuser --noinput

run-server:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

tests:
	python3 manage.py test
