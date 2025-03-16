# Imperial Gems 💎

## 🛒 E-commerce Jewelry Store
This project is an elegant e-commerce platform built with **Django**, designed for showcasing and selling exquisite jewelry. The project offers a smooth user experience with features like product catalog browsing, shopping cart functionality, and order checkout.

---

## 📋 Features
✅ User registration and authentication (login/logout)  
✅ Product catalog with categories  
✅ Detailed product page with description and price  
✅ Shopping cart with dynamic item quantity updates  
✅ Order checkout with user details form  
✅ "Thank you" page after successful purchase  
✅ Admin panel for managing products, categories, and orders  
✅ Custom user model with extended fields (phone, address)  
✅ Secure environment variables using `.env`  
✅ Optimized `.gitignore` for better project management  

---

## 🚀 Installation and Setup
1. **Clone the repository:**
```bash
git clone https://github.com/username/imperial-gems.git
```

2. **Navigate to the project folder:**
```bash
cd imperial-gems
```

3. **Create a virtual environment and activate it:**
```bash
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate   # On Windows
```

4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

5. **Create a `.env` file in the root directory and add the following:**
```
SECRET_KEY=your-very-secure-secret-key
DEBUG=True
DATABASE_NAME=store_db
DATABASE_USER=store_admin
DATABASE_PASSWORD=strongpassword123
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

6. **Run database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create a superuser for accessing the admin panel:**
```bash
python manage.py createsuperuser
```

8. **Start the development server:**
```bash
python manage.py runserver
```

9. **Visit the app in your browser:**  
🔗 **[localhost:8000](http://localhost:8000)**

---

## 📂 Project Structure
```
/imperial-gems/
├── manage.py
├── .env
├── .gitignore
├── requirements.txt
├── /jewelry/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   ├── static/
└── /store/
    ├── settings.py
    ├── urls.py
```

---

## 🏆 Credits
**Imperial Gems** was created with love for craftsmanship and an appreciation for the art of jewelry. 💎