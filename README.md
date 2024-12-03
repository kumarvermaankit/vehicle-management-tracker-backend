# Vehicle Repair System Backend

## Installation
1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Create and apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

The backend should now be running at `http://127.0.0.1:8000/`. You can access the Django admin at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.
