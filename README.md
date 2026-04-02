# Finance Dashboard API 

A production-ready FastAPI backend designed for small businesses and personal finance management. This system features **Role-Based Access Control (RBAC)**, secure **JWT Authentication**, and automated **Financial Analytics**.

---

##  Live API Documentation
**Swagger UI:** https://finance-backend-assignment-production.up.railway.app/docs  


---

##  Key Features
- **Secure Authentication:** User registration and login using `bcrypt` password hashing (Direct implementation for Python 3.13 compatibility).
- **JWT Authorization:** Protected routes requiring a Bearer Token for access.
- **Role-Based Access Control (RBAC):**
  - **Admin:** Can create financial records and view the dashboard summary.
  - **Analyst:** Can view existing records and the dashboard summary (Read-only).
  - **Viewer:** Can only view the list of records (Restricted from Dashboard).
- **Financial Analytics:** Real-time calculation of Total Income, Total Expense, Net Balance, and Category-specific totals.
- **Database:** SQLite (local) / PostgreSQL (production-ready) using SQLAlchemy ORM.

---

##  Technical Stack
- **Language:** Python 3.13
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Security:** `python-jose` (JWT), `bcrypt`
- **Validation:** Pydantic v2

---

##  Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kotigopinedi/finance-backend-assignment.git](https://github.com/kotigopinedi/finance-backend-assignment.git)
   cd finance-backend-assignment



2. **Create a Virtual Environment:**
   python -m venv venv
   .\venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Run the Application:**
   uvicorn main:app --reload --port 8080

   Open your browser to: http://localhost:8080/docs

   ## Testing Guide
   1. **Register a User**
      
      Use the POST /register endpoint.
      {
         "email": "admin@example.com",
         "password": "password123",
         "role": "Admin"
      }

    2. **Login & Authorize**
       Use POST /login to get your access_token.
      Click the Authorize button at the top of Swagger UI and paste the token.

    3. **Add Data (Admin Only)**
       Use POST /records to add transactions:

         Income: {"amount": 5000, "type": "Income", "category": "Freelance"}

         Expense: {"amount": 1500, "type": "Expense", "category": "Software"}


     4. **View Dashboard**
        Access GET /dashboard/summary to see the calculated totals and category-wise breakdown.

     ## Project Structure

     main.py: API Route definitions and App entry point.

     models.py: SQLAlchemy Database models (Users, Records).

     schemas.py: Pydantic models for request/response validation.

     auth.py: JWT Logic, Password Hashing, and Role Dependencies.

     crud.py: Database Create/Read logic and Analytics calculations.

     database.py: Session management and Engine setup.

  
  
