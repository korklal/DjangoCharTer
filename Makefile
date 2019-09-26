run:
	python manage.py runserver 8000
make-su:
	python manage.py createsuperuser
migrate:
	python manage.py migrate
migrate-m:
	python manage.py makemigrations
