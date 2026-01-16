# Job Finder API

A Django REST API that fetches real-time job listings from the [Adzuna Job Search API](https://developer.adzuna.com/). This backend powers the Job Finder frontend by providing job data based on keyword and location queries.

## ✨ Features
- Search jobs by keyword (e.g., "developer", "designer")
- Filter by location (e.g., "New York", "United States")
- Returns structured job data: title, company, location, salary, and apply link
- Securely handles API keys via environment variables
- CORS-enabled for frontend integration

## 🛠️ Tech Stack
- Python 3.12
- Django 6.0
- Django REST Framework (DRF)
- `python-decouple` for environment management
- `requests` for external API calls

## 🚀 Local Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/mcrolins/job-finder-API.git
   cd job-finder-API

2.Create virtual environment
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  # venv\Scripts\activate  # Windows

3.Install dependencies
 pip install -r requirements.txt

4.Set up environment variables 
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_API_KEY=your_adzuna_api_key
SECRET_KEY=your_django_secret_key

5.Run the server
python manage.py runserver

6.Test the API
http://localhost:8000/api/jobs/?q=developer&l=United%20States
