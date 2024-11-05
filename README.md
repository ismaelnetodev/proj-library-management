# Digital Library System 📚

This is a Digital Library System project developed with Django and PostgreSQL, designed to facilitate the management and access to a library's collection. Key features include user registration, book loans, and book search functionality.

## Main Features

- **User Registration and Authentication**
- **Book Catalog Management**
- **Book Loans and Reservations**
- **Inventory and Availability Control**

## Environment Setup

### Prerequisites

- **Python** (version 3.8 or higher)
- **PostgreSQL**
- **Git** (optional, for cloning the repository)

### 1. Cloning the Repository

First, clone the repository to your machine:

```bash
git clone <repository-URL>
cd repository-name
```

### 2. Installing Dependencies
It's recommended to use a virtual environment to manage the project dependencies. Run the following commands to create and activate a virtual environment and install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setting Up the Database
This project uses PostgreSQL as its database. Create a database in PostgreSQL with the desired name, for example:
```sql
CREATE DATABASE digital_library;
```

### 4. Configuring the .env File
To keep your database connection information secure, use a .env file in the project root with environment variables. Create a .env file and add the following database configuration:
```plaintext
# Database Configuration
DB_NAME=digital_library
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
Important: Ensure the .env file is listed in .gitignore so it is not versioned.

### 5. Applying Migrations
After setting up the database and .env file, run the migrations to create the required tables:
```bash
python manage.py migrate
```

### 6. Running the Local Server
With the environment set up, start the local server with:
```bash
python manage.py runserver
```
The project will be available at http://localhost:8000.
