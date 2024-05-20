# Car Inventory Django Application

This Django application allows users to input new car data including the name, manufacturer, price, model year, and engine used. The data is stored in a database and can be managed through the Django admin interface.

## Features

- Add new car information
- View existing car information
- Edit car details
- Delete car entries
- Admin interface for managing car data

## Technologies Used

- Django (Python Web Framework)
- SQLite
- HTML/CSS for front-end

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.12
- Django 4.0 or later

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/car-site.git
   cd mysite
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://127.0.0.1:8000/`

## Usage

- To add a new car, navigate to the appropriate form and fill in the details.
- To view existing cars, go to the list view.
- Use the admin interface at `http://127.0.0.1:8000/admin/` to manage the car entries.

## Project Structure

```plaintext
car-inventory/
├── car_inventory/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cars/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
