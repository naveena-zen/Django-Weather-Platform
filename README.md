# API-Driven Real-Time Weather Dashboard

A production-style Django web application that integrates the OpenWeatherMap REST API to fetch, process, and dynamically render real-time weather data. The system leverages Django’s Model-View-Template (MVT) architecture to ensure modular design, scalability, and maintainability.

## Project Overview

The application enables users to retrieve live weather information for any city worldwide. Upon user input, the backend performs an API request, parses the JSON payload, extracts relevant meteorological parameters, and renders the data through dynamic templates.
This project demonstrates practical implementation of:

- RESTful API integration
- JSON data parsing and transformation
- Server-side validation and exception handling
- Dynamic template rendering
- Responsive frontend design
  
## Architecture

- Framework: Django (Python)
- Architecture Pattern: Model-View-Template (MVT)
- API Communication: HTTP requests using `requests` library
- Data Format: JSON
- Frontend: HTML5, CSS3 (Responsive UI)

## Core Features

- Real-time weather data retrieval
- Dynamic city-based search functionality
- JSON response parsing and structured data extraction
- User-friendly error handling for invalid inputs
- Default city fallback mechanism
- Clean, modular project structure

## Application Workflow

1. User submits a city name.
2. Backend validates input.
3. System sends request to OpenWeatherMap API.
4. JSON response is received and parsed.
5. Relevant weather attributes are extracted.
6. Processed data is passed to template context.
7. Dashboard dynamically renders updated weather information.

## Installation & Setup

### 1️⃣ Clone Repository
```
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
```

Activate:
- Windows:
```
venv\Scripts\activate
```
- Mac/Linux:
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure API Key
Replace the placeholder API key in:
```
dashboard/views.py
```
with your OpenWeatherMap API key.

### 5️⃣ Run Development Server
```
python manage.py runserver
```

Access application at:
```
http://127.0.0.1:8000/
```

## Future Enhancements

- Multi-city comparison module
- Extended forecast integration
- Asynchronous API requests
- Caching layer for optimized performance
- Containerized deployment using Docker
- Production deployment with Gunicorn & Nginx

## Project Structure

```
weather-dashboard/
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│
├── dashboard/
│   ├── templates/dashboard/home.html
│   ├── views.py
│   ├── urls.py
│
├── manage.py

```

## Technical Highlights

- Clean separation of concerns via MVT architecture
- Robust JSON response handling
- Structured context passing to templates
- Lightweight and scalable backend design
- API-driven dynamic data rendering
  
## License

This project is intended for educational and portfolio demonstration purposes.
