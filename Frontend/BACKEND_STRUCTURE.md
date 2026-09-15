# Backend Directory Structure Documentation

This document provides a complete overview of the backend folder structure for the Boarding Finder application.

## Project Root: Backend/

```
Backend/
├── manage.py                 # Django management script for running commands
├── config/                   # Main Django configuration directory
│   ├── __init__.py
│   ├── settings.py          # Django settings and configuration
│   ├── urls.py              # Root URL configuration
│   ├── asgi.py              # ASGI configuration for deployment
│   ├── wsgi.py              # WSGI configuration for deployment
│   └── __pycache__/
└── apps/                     # Django applications directory
    ├── __init__.py
    ├── accounts/            # User authentication and profile management
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration for accounts
    │   ├── apps.py          # App configuration
    │   ├── forms.py         # User forms (registration, login, profile)
    │   ├── managers.py      # Custom model managers
    │   ├── models.py        # User and profile models
    │   ├── tests.py         # Unit tests for accounts app
    │   ├── urls.py          # URL routing for accounts
    │   ├── views.py         # View handlers for authentication
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   ├── 0001_initial.py    # Initial migration
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── boarding/            # Boarding/Accommodation listings
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Boarding and accommodation models
    │   ├── tests.py         # Unit tests for boarding app
    │   ├── urls.py          # URL routing for boarding listings
    │   ├── views.py         # View handlers for boarding operations
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── bookings/            # Booking management
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Booking models
    │   ├── tests.py         # Unit tests for bookings
    │   ├── views.py         # View handlers for booking operations
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── chat/                # Messaging and communication
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Chat and message models
    │   ├── tests.py         # Unit tests for chat
    │   ├── views.py         # View handlers for messaging
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── dashboard/           # User dashboard and statistics
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Dashboard-related models
    │   ├── tests.py         # Unit tests for dashboard
    │   ├── views.py         # View handlers for dashboard
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── notifications/       # System notifications
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Notification models
    │   ├── tests.py         # Unit tests for notifications
    │   ├── views.py         # View handlers for notifications
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    ├── reviews/             # Ratings and reviews
    │   ├── __init__.py
    │   ├── admin.py         # Django admin configuration
    │   ├── apps.py          # App configuration
    │   ├── models.py        # Review and rating models
    │   ├── tests.py         # Unit tests for reviews
    │   ├── views.py         # View handlers for review operations
    │   ├── migrations/      # Database migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   └── __pycache__/
    │
    └── __pycache__/
```

## Module Descriptions

### Core Configuration (config/)

| File | Purpose |
|------|---------|
| `settings.py` | Main Django configuration including database, installed apps, middleware, templates, and static files |
| `urls.py` | Root URL router that includes URLs from all installed apps |
| `wsgi.py` | WSGI application entry point for web servers (Gunicorn, uWSGI) |
| `asgi.py` | ASGI application entry point for async web servers |

### Applications (apps/)

#### 1. **Accounts App** (User Management)
Handles user authentication, registration, and profile management.

| File | Responsibility |
|------|-----------------|
| `models.py` | User profile, custom user model, authentication fields |
| `views.py` | Login, registration, profile update, password reset views |
| `forms.py` | User registration forms, login forms, profile forms |
| `urls.py` | Routes for /accounts/login, /accounts/register, /accounts/profile, etc. |
| `managers.py` | Custom user manager for creating users and superusers |
| `admin.py` | Admin interface configuration for user management |
| `tests.py` | Unit tests for authentication and user operations |
| `migrations/` | Database schema changes for user-related tables |

#### 2. **Boarding App** (Accommodation Listings)
Manages boarding house listings, amenities, and property information.

| File | Responsibility |
|------|-----------------|
| `models.py` | Boarding/Property model, amenities, images, location data |
| `views.py` | List all boardings, boarding details, search/filter functionality |
| `urls.py` | Routes for /boarding/list, /boarding/<id>/details, /boarding/search |
| `admin.py` | Admin interface for property management |
| `tests.py` | Unit tests for boarding operations |
| `migrations/` | Database schema for boarding and properties |

#### 3. **Bookings App** (Reservation Management)
Handles booking/reservation functionality for boarding spaces.

| File | Responsibility |
|------|-----------------|
| `models.py` | Booking model, reservation dates, booking status |
| `views.py` | Create booking, view bookings, cancel booking, booking confirmation |
| `urls.py` | Routes for /bookings/create, /bookings/list, /bookings/<id>/cancel |
| `admin.py` | Admin interface for booking management |
| `tests.py` | Unit tests for booking operations |
| `migrations/` | Database schema for bookings |

#### 4. **Chat App** (Messaging System)
Manages user-to-user messaging and communication.

| File | Responsibility |
|------|-----------------|
| `models.py` | Message model, conversation/thread model, participants |
| `views.py` | Send message, retrieve messages, create conversation |
| `urls.py` | Routes for /chat/conversations, /chat/messages, /chat/send |
| `admin.py` | Admin interface for message moderation |
| `tests.py` | Unit tests for messaging |
| `migrations/` | Database schema for chat/messages |

#### 5. **Dashboard App** (User Analytics)
Provides user dashboards and analytics.

| File | Responsibility |
|------|-----------------|
| `models.py` | Dashboard data models, statistics, user metrics |
| `views.py` | Dashboard view, statistics aggregation, analytics data |
| `urls.py` | Routes for /dashboard, /dashboard/analytics |
| `admin.py` | Admin configuration |
| `tests.py` | Unit tests for dashboard |
| `migrations/` | Database schema for dashboard data |

#### 6. **Notifications App** (System Notifications)
Handles system notifications and alerts to users.

| File | Responsibility |
|------|-----------------|
| `models.py` | Notification model, notification types, read/unread status |
| `views.py` | Retrieve notifications, mark as read, delete notifications |
| `urls.py` | Routes for /notifications/list, /notifications/mark-read |
| `admin.py` | Admin interface for notification management |
| `tests.py` | Unit tests for notifications |
| `migrations/` | Database schema for notifications |

#### 7. **Reviews App** (Ratings & Reviews)
Manages user reviews and ratings for boarding places.

| File | Responsibility |
|------|-----------------|
| `models.py` | Review model, rating model, review content and metadata |
| `views.py` | Create review, list reviews, update/delete review |
| `urls.py` | Routes for /reviews/create, /reviews/<id>/edit, /reviews/<id>/delete |
| `admin.py` | Admin interface for review moderation |
| `tests.py` | Unit tests for review operations |
| `migrations/` | Database schema for reviews |

## File Type Descriptions

### Python Files (*.py)

- **`__init__.py`**: Marks directory as Python package, can contain package initialization code
- **`admin.py`**: Django admin site configuration and model registration
- **`apps.py`**: Django app configuration and metadata
- **`models.py`**: SQLAlchemy/ORM models defining database tables
- **`views.py`**: Request handlers and business logic (or use in REST APIs)
- **`forms.py`**: Django form classes for data validation and rendering
- **`urls.py`**: URL routing configuration and endpoint mappings
- **`tests.py`**: Unit tests and integration tests
- **`managers.py`**: Custom model managers for database queries
- **`settings.py`**: Global configuration, database, middleware, secrets
- **`manage.py`**: Command-line utility for Django management tasks

### Directories

- **`migrations/`**: Database schema versioning and evolution scripts
- **`__pycache__/`**: Python bytecode cache (can be ignored in version control)

## Architecture Overview

This is a **Django REST Framework** backend following the **MTV (Model-Template-View)** pattern:

1. **Models** define the database schema
2. **Views** handle business logic and HTTP requests
3. **URLs** map endpoints to views
4. **Forms** handle data validation
5. **Admin** provides management interface
6. **Migrations** track database changes

Each app is modular and can be independently developed, tested, and deployed.

---

**Last Updated:** Documentation automatically generated from backend structure
