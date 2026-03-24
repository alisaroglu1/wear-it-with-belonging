# Wear It With Belonging 🛍️

A modern, full-featured e-commerce web application built with Django. Designed for clothing retail with a clean, minimal aesthetic.

## ✨ Features

### Customer Side
- 🏠 Product listing with category filtering and search
- 🔍 Product detail pages
- 🛒 Shopping cart (add, remove, update quantity)
- 💳 Checkout with delivery address and simulated payment
- 📦 Order confirmation and tracking
- 👤 User profile with address management
- 📋 Order history with status tracking
- 🔐 Authentication via django-allauth (register, login, logout)

### Admin Dashboard
- 📊 Sales overview (total revenue, orders, products)
- 📦 Order management (view, update status, delete)
- 🛍️ Product management (add, edit, delete)
- 🗂️ Category management (add, delete)
- ⚠️ Low stock alerts

## 🛠️ Tech Stack

- **Backend:** Django 6.x
- **Authentication:** django-allauth
- **Database:** SQLite (development)
- **Frontend:** HTML, CSS (custom design system)
- **Fonts:** Cormorant Garamond + DM Sans
- **Image handling:** Pillow

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/alisaroglu1/wear-it-with-belonging.git
cd wear-it-with-belonging
```

2. **Create a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the `wearity/` root directory
```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create a superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/store/` to see the app.
Visit `http://127.0.0.1:8000/dashboard/` for the admin dashboard (staff only).

## 📁 Project Structure

```
wearity/
├── wearity/          # Project settings & URLs
├── store/            # Main e-commerce app
│   ├── models.py     # Product, Cart, Order models
│   ├── views.py      # All store views
│   ├── urls.py       # Store URL routes
│   └── templates/    # Store templates
├── dashboard/        # Admin dashboard app
│   ├── views.py      # Dashboard views
│   ├── urls.py       # Dashboard URL routes
│   └── templates/    # Dashboard templates
├── templates/        # Base templates
│   ├── base.html
│   └── account/      # Allauth templates
└── static/           # CSS and static files
```

## 🎨 Design System

Custom CSS design system with:
- **Colors:** Warm beige background, dark ink, terracotta accent, sage green
- **Typography:** Cormorant Garamond (headings) + DM Sans (body)
- **Fully responsive** — mobile-first design

## 🔮 Roadmap

- [ ] Stripe payment integration
- [ ] Email notifications for order status changes
- [ ] Power BI analytics dashboard
- [ ] Deployment to Railway/Render

## 👨‍💻 Author

**Ali Saroğlu** — YBS Student  
Built as a learning project to master Django and web development.

<img width="1919" height="870" alt="Ekran görüntüsü 2026-03-24 101517" src="https://github.com/user-attachments/assets/8ece2c19-e586-40e9-8b23-44dcce6cab6a" />

<img width="1894" height="833" alt="Ekran görüntüsü 2026-03-24 101528" src="https://github.com/user-attachments/assets/7cbc74f1-374e-4444-9955-a00eeece7661" />
<img width="1881" height="862" alt="Ekran görüntüsü 2026-03-24 101539" src="https://github.com/user-attachments/assets/b41bdf42-1cfb-4093-b494-66a2a27aa241" />

<img width="1885" height="848" alt="Ekran görüntüsü 2026-03-24 101547" src="https://github.com/user-attachments/assets/945563bc-afb5-45db-bee6-783b2d9402fa" />


<img width="1896" height="858" alt="Ekran görüntüsü 2026-03-24 101624" src="https://github.com/user-attachments/assets/f57a18e8-5dd5-4dcf-a975-9764b8ae132f" />


---

*This project is for educational purposes.*
