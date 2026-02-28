# Intermost Backend

## Production-ready Django REST API with MongoDB Atlas

### Quick Start

1. **Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Environment**
```bash
copy .env.example .env
# Edit .env with your MongoDB Atlas connection string
```

4. **Setup MongoDB Atlas (Free)**
   - Go to https://www.mongodb.com/cloud/atlas
   - Create a free account
   - Create a new cluster (M0 Free Tier)
   - Create a database user
   - Whitelist your IP (or 0.0.0.0/0 for development)
   - Get your connection string and add to .env

5. **Run Migrations (Django auth)**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Seed Database**
```bash
python scripts/seed_data.py
```

7. **Run Development Server**
```bash
python manage.py runserver
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/health/` | GET | Health check |
| `/api/v1/auth/login/` | POST | JWT Login |
| `/api/v1/auth/register/` | POST | Register user |
| `/api/v1/countries/` | GET, POST | List/Create countries |
| `/api/v1/countries/<id>/` | GET, PUT, DELETE | Country detail |
| `/api/v1/colleges/` | GET, POST | List/Create colleges |
| `/api/v1/colleges/country/<slug>/` | GET | Colleges by country |
| `/api/v1/testimonials/` | GET, POST | Testimonials |
| `/api/v1/blogs/` | GET, POST | Blog posts |
| `/api/v1/inquiries/` | GET, POST | Lead inquiries |
| `/api/v1/news/` | GET, POST | News updates |
| `/api/v1/team/` | GET, POST | Team members |
| `/api/docs/` | GET | Swagger API docs |

### Production Deployment

```bash
# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Cloudinary Setup (Free Image Hosting)
1. Sign up at https://cloudinary.com/
2. Get your Cloud Name, API Key, and API Secret
3. Add to .env file
# Intermost-Backend
