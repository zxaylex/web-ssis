# Simple Student Information System

A Flask-based REST API for managing student, program, and college information in an educational institution.

## Features

- **Student Management**: CRUD operations for student records
- **Program Management**: CRUD operations for academic programs
- **College Management**: CRUD operations for colleges
- **Relationship Queries**: Get students by program, programs by college, etc.
- **RESTful API**: JSON-based API with standard HTTP methods
- **Database Integration**: MySQL database with proper relationships

## System Architecture

The system follows a three-tier architecture:

1. **Routes Layer** (`app/routes/`): Handles HTTP requests and responses
2. **Models Layer** (`app/models/`): Business logic and database operations
3. **Database Layer**: MySQL database with proper relationships

### Database Schema

- **College** (code, name)
- **Program** (code, name, college) - Foreign key to College
- **Student** (id_number, profile_url, first_name, last_name, program, year_level, gender) - Foreign key to Program

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd web-ssis
   ```

2. **Install dependencies**:
   ```bash
   pipenv install
   ```

3. **Set up the database**:
   - Create a MySQL database named `student_system`
   - Import the `student_system.sql` file into your MySQL database
   - Update the database configuration in `app/config.py` or create a `.env` file

4. **Configure database connection**:
   
   **Option A: Update config.py directly**
   ```python
   # In app/config.py
   MYSQL_DATABASE_HOST = "localhost"
   MYSQL_DATABASE_USER = "your_username"
   MYSQL_DATABASE_PASSWORD = "your_password"
   MYSQL_DATABASE_PORT = 3306
   MYSQL_DATABASE_DB = "student_system"
   ```
   
   **Option B: Create .env file**
   ```bash
   # Create .env file in the root directory
   MYSQL_DATABASE_HOST=localhost
   MYSQL_DATABASE_USER=your_username
   MYSQL_DATABASE_PASSWORD=your_password
   MYSQL_DATABASE_PORT=3306
   MYSQL_DATABASE_DB=student_system
   SECRET_KEY=your-secret-key-here
   CSRF_SESSION_KEY=your-csrf-secret-key-here
   ```

5. **Test database connection**:
   ```bash
   python test_db_connection.py
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## API Endpoints

### Students
- `GET /student/` - Get all students
- `GET /student/{id}` - Get student by ID
- `POST /student/create` - Create new student
- `PUT /student/{id}` - Update student
- `DELETE /student/{id}` - Delete student
- `GET /student/program/{code}` - Get students by program
- `GET /student/year/{level}` - Get students by year level

### Programs
- `GET /program/` - Get all programs
- `GET /program/{code}` - Get program by code
- `POST /program/create` - Create new program
- `PUT /program/{code}` - Update program
- `DELETE /program/{code}` - Delete program
- `GET /program/college/{code}` - Get programs by college

### Colleges
- `GET /college/` - Get all colleges
- `GET /college/{code}` - Get college by code
- `POST /college/create` - Create new college
- `PUT /college/{code}` - Update college
- `DELETE /college/{code}` - Delete college

## Usage Examples

### Get all students
```bash
curl -X GET http://localhost:5000/student/
```

### Get a specific student
```bash
curl -X GET http://localhost:5000/student/2021-0036
```

### Create a new student
```bash
curl -X POST http://localhost:5000/student/create \
  -H "Content-Type: application/json" \
  -d '{
    "id_number": "2024-9999",
    "first_name": "John",
    "last_name": "Doe",
    "program": "BSCS",
    "year_level": "1",
    "gender": "male"
  }'
```

### Get all programs in a college
```bash
curl -X GET http://localhost:5000/program/college/CCS
```

## Testing

Run the test script to verify the API functionality:

```bash
python test_api.py
```

Make sure the Flask application is running before executing the test script.

## Project Structure

```
web-ssis/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration settings
│   ├── service.py           # Database and CSRF services
│   ├── models/              # Data models
│   │   ├── student.py       # Student model
│   │   ├── program.py       # Program model
│   │   └── college.py       # College model
│   ├── routes/              # API routes
│   │   ├── student.py       # Student endpoints
│   │   ├── program.py       # Program endpoints
│   │   └── college.py       # College endpoints
│   ├── templates/           # HTML templates (if needed)
│   └── static/              # Static files (if needed)
├── main.py                  # Application entry point
├── student_system.sql       # Database schema and sample data
├── test_api.py              # API test script
├── API_DOCUMENTATION.md     # Detailed API documentation
├── Pipfile                  # Python dependencies
└── README.md               # This file
```

## Data Models

### Student Model
The Student model represents individual students with the following attributes:
- `id_number`: Unique student identifier
- `profile_url`: URL to student's profile picture
- `first_name`: Student's first name
- `last_name`: Student's last name
- `program`: Program code the student is enrolled in
- `year_level`: Student's year level (1, 2, 3, 4)
- `gender`: Student's gender (male, female)

### Program Model
The Program model represents academic programs with:
- `code`: Unique program code
- `name`: Program name
- `college`: College code the program belongs to

### College Model
The College model represents colleges with:
- `code`: Unique college code
- `name`: College name

## Database Relationships

- **Students** belong to **Programs** (many-to-one)
- **Programs** belong to **Colleges** (many-to-one)
- **Colleges** have many **Programs** (one-to-many)
- **Programs** have many **Students** (one-to-many)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For detailed API documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

For issues and questions, please create an issue in the repository.