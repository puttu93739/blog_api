# blog_api
Blogging Platform API
https://roadmap.sh/projects/blogging-platform-api


## 🚀 Features

- Create new blog posts
- Retrieve a single blog post by ID
- Retrieve all blog posts
- Filter blog posts by a search term (title, content, or category)
- Update existing blog posts
- Delete blog posts
- Follows RESTful principles
- Asynchronous and high-performance

---

## 📦 Tech Stack

- **FastAPI** – For building the API
- **MongoDB** – As the database
- **Motor** – Async MongoDB driver for Python
- **Pydantic** – For data validation
- **Uvicorn** – ASGI server to run the FastAPI app

---

## 🛠️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/blogging-platform-api.git
   cd blogging-platform-api
   
Create a virtual environment and activate it
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install the dependencies
pip install -r requirements.txt

Start MongoDB locally or use MongoDB Atlas and update your MongoDB URI in .env or in db.py.

Run the server
uvicorn main:app --reload
