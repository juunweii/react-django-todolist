# react-django-todolist

## Django Part
```
pip install django-cors-headers djangorestframework

```

In the root directory
#### `python3 manage.py makemigrations`
#### `python3 manage.py migrate`
#### `python3 manage.py runserver`

## React Part

```
cd frontend
```
#### `npm install`
#### `npm start`

## API
Use `http://127.0.0.1:8000/api/todos/` to see the backend todo item in the interface  
`/api/todos/{id}` can see the exact todo item

## Database
Create a admin user to do the CRUD
```
python manage.py createsuperuser
```
`http://localhost:8000/admin` can do the CRUD in Django default interface
