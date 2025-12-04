Lost and Found Management System

This is a backend system to manage lost and found items. It allows users to report lost or found items, view lists of items, and contact the reporter if needed. The system is built using FastAPI and uses a JSON file as a mock database.

Features

Report lost items with details like item name, location, and description.

Report found items with details and contact information.

View all lost items.

View all found items.

RESTful API endpoints with JSON input/output.

Easy testing with Swagger UI or REST client.

Technologies Used

Python 3.11+

FastAPI

Uvicorn

JSON (for mock database)

Swagger UI for API documentation

Installation and Setup

Clone the repository:
git clone https://github.com/your-username/lost-and-found.git

cd lost-and-found

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows

Install dependencies:
pip install -r requirements.txt

Run the application:
uvicorn main:app --reload

The app will be running at http://127.0.0.1:8000/
.

API Endpoints
Lost Items

GET /lost_items – Get all lost items

POST /lost_items – Add a new lost item

Found Items

GET /found_items – Get all found items

POST /found_items – Add a new found item

Mock Database

The system uses db.json to store data:

{
"lost_items": [
{
"id": 1,
"item_name": "Wallet",
"location_lost": "Library",
"description": "Black leather wallet"
}
],
"found_items": [
{
"id": 1,
"item_name": "Umbrella",
"location_found": "Bus Stop",
"description": "Red umbrella with wooden handle",
"contact_email": "example@mail.com
"
}
]
}

Testing the API

Open Swagger UI at http://127.0.0.1:8000/docs
 to test endpoints visually.

Or use a REST client like the VS Code REST Client to send requests.

Future Improvements

Add user authentication.

Replace JSON with a real database like MySQL or PostgreSQL.

Add search and filter functionality.

Implement notifications for matching lost and found items.

License

This project is open-source and free to use.
