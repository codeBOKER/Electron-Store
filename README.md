# Django Project

This is a Django project named `Electron-Store`.

## Getting Started

To get started with this project, follow these steps:

1. Install Python and Django:
   - Install Python 3.8 from https://www.python.org/downloads/
   - Install Django using pip: `pip install django`

2. Clone the repository:
   - Use Git to clone this repository: `https://github.com/codeBOKER/Electron-Store.git`

3. Set up the environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables:
     ```
     DJANGO_SECRET_KEY=your-secret-key
     DB_NAME=your-database-name
     DB_USER=your-database-user
     DB_PASSWORD=your-database-password
     DB_HOST=your-database-host
     DB_PORT=your-database-port
     ```
     - Generate a secret key using Django's built-in `get_random_secret_key()` function:
       ```python
       from django.core.management.utils import get_random_secret_key

       # Generate a new secret key
       secret_key = get_random_secret_key()

       # Add the secret key to your .env file
       with open('.env', 'a') as f:
           f.write(f'DJANGO_SECRET_KEY={secret_key}\n')
       ```

4. Install project dependencies:
   - Navigate to the project directory: `cd project`
   - Install the required dependencies: `pip install -r requirements.txt`

5. Apply database migrations:
   - Run the following command to apply database migrations: `python manage.py migrate`

6. Create a superuser:
   - Run the following command to create a superuser: `python manage.py createsuperuser`

7. Run the development server:
   - Run the following command to start the development server: `python manage.py runserver`

8. Access the project in your browser:
   - Open your web browser and navigate to http://127.0.0.1:8000/

## Project Structure

The project structure is as follows:
```
Electron-Store/
├── core/
│   ├── templates/
│   │   └── (template files)
│   ├── static/
│   │   └── (static files)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
│   └── (collected static files)
├── media/
│   └── (uploaded media files)
└── .env
```


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.`.

