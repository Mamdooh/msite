# MySite - Django Magic 8-Ball

A simple Django website featuring a homepage and a magic 8-ball predictor.

## Features

- Welcoming homepage with introductory content
- Magic 8-Ball predictor with consistent answers based on question hashing
- Custom CSS with responsive design
- Modern, clean aesthetic suitable for both mobile and PC

## Technology Stack

- Python 3.x
- Django 5.0
- Custom CSS (no frameworks)

## Installation

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Run development server:
   ```bash
   python manage.py runserver
   ```

5. Visit [http://localhost:8000](http://localhost:8000)

## Usage

- **Homepage**: Navigate to `/` for the welcome page with introductory content
- **Magic 8-Ball**: Navigate to `/magic8ball/` to ask questions and receive predictions

## How It Works

The Magic 8-Ball uses a hash-based algorithm to ensure consistency:
- Same question always returns the same answer
- Questions are normalized (case-insensitive, whitespace-trimmed)
- SHA256 hashing provides deterministic results
- 20 classic magic 8-ball responses

## Project Structure

```
msite/
├── manage.py
├── requirements.txt
├── msite/                 # Django project settings
│   ├── settings.py
│   └── urls.py
└── predictor/             # Main Django app
    ├── views.py           # View logic
    ├── urls.py            # URL patterns
    ├── utils.py           # Magic 8-ball logic
    ├── templates/         # HTML templates
    │   ├── base.html
    │   ├── home.html
    │   └── magic8ball.html
    └── static/            # CSS files
        └── predictor/
            └── css/
                ├── base.css
                ├── home.css
                └── magic8ball.css
```

## Development

To create a superuser for the admin interface (optional):
```bash
python manage.py createsuperuser
```

## License

This project is open source and available for educational purposes.
