🧾 e-Auction Platform
An online e-Auction web application built using Django with a modern frontend (HTML, CSS, Bootstrap, JavaScript). It allows users to register, list items for auction, place bids, and manage auction listings — all integrated with Django's powerful admin panel.

🛠️ Technologies Used
💻 Frontend: HTML5, CSS3, Bootstrap 5, JavaScript (vanilla)

🧠 Backend: Python, Django

📦 Database: SQLite (default Django DB)

🔐 Authentication: Django built-in user system

🛠️ Admin Panel: Fully configured Django admin

🔑 Key Features
🧍 User Registration & Login system

📦 List items for auction with price & description

⏰ Timer-based auction management

🛒 Place bids on active items

🧑‍💼 Admin panel to manage users, items, and bids

📩 Contact page or inquiry system

📊 Order summary or total bid count feature

⚙️ How to Run Locally
Clone the repository:

git clone https://github.com/yourusername/e-auction.git
cd e-auction
Create a virtual environment and activate:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

pip install -r requirements.txt
Apply migrations:

python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Start the development server:

python manage.py runserver
Visit:

Frontend: http://localhost:8000/

Admin Panel: http://localhost:8000/admin/

💡 Future Improvements
Real-time bidding using Django Channels & WebSocket

Email notifications for winners

Image gallery & video previews

Mobile responsive enhancements

Payment integration (Stripe, Razorpay, etc.)

