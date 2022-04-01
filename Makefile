run:
	python ./cmp/manage.py runserver

migrations:
	python ./cmp/manage.py makemigrations cmp_admin

migrate:
	python ./cmp/manage.py migrate