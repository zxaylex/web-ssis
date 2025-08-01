# Student Information System API Documentation

This document describes the REST API endpoints for the Simple Student Information System.

## Base URL
All endpoints are relative to the base URL of your Flask application.

## Authentication
Currently, no authentication is required for the API endpoints.

## Data Models

### Student
- `id_number` (string): Unique student identifier
- `profile_url` (string): URL to student's profile picture
- `first_name` (string): Student's first name
- `last_name` (string): Student's last name
- `program` (string): Program code the student is enrolled in
- `year_level` (string): Student's year level (1, 2, 3, 4)
- `gender` (string): Student's gender (male, female)

### Program
- `code` (string): Unique program code
- `name` (string): Program name
- `college` (string): College code the program belongs to

### College
- `code` (string): Unique college code
- `name` (string): College name

## Student Endpoints

### Get All Students
```
GET /student/
```
Returns a list of all students in the system.

**Response:**
```json
[
  {
    "id_number": "2021-0036",
    "profile_url": null,
    "first_name": "Andre",
    "last_name": "Hancock",
    "program": "BSEd-Bio",
    "year_level": "3",
    "gender": "female"
  }
]
```

### Get Student by ID
```
GET /student/{student_id}
```
Returns details of a specific student.

**Parameters:**
- `student_id` (string): The student's ID number

**Response:**
```json
{
  "id_number": "2021-0036",
  "profile_url": null,
  "first_name": "Andre",
  "last_name": "Hancock",
  "program": "BSEd-Bio",
  "year_level": "3",
  "gender": "female"
}
```

### Create New Student
```
POST /student/create
```
Creates a new student record.

**Request Body:**
```json
{
  "id_number": "2024-9999",
  "profile_url": "https://example.com/profile.jpg",
  "first_name": "John",
  "last_name": "Doe",
  "program": "BSCS",
  "year_level": "1",
  "gender": "male"
}
```

**Response:**
```json
{
  "message": "Student created successfully",
  "student": {
    "id_number": "2024-9999",
    "profile_url": "https://example.com/profile.jpg",
    "first_name": "John",
    "last_name": "Doe",
    "program": "BSCS",
    "year_level": "1",
    "gender": "male"
  }
}
```

### Update Student
```
PUT /student/{student_id}
```
Updates an existing student record.

**Parameters:**
- `student_id` (string): The student's ID number

**Request Body:**
```json
{
  "first_name": "Jane",
  "year_level": "2"
}
```

**Response:**
```json
{
  "message": "Student updated successfully"
}
```

### Delete Student
```
DELETE /student/{student_id}
```
Deletes a student record.

**Parameters:**
- `student_id` (string): The student's ID number

**Response:**
```json
{
  "message": "Student deleted successfully"
}
```

### Get Students by Program
```
GET /student/program/{program_code}
```
Returns all students enrolled in a specific program.

**Parameters:**
- `program_code` (string): The program code

**Response:**
```json
[
  {
    "id_number": "2021-0036",
    "profile_url": null,
    "first_name": "Andre",
    "last_name": "Hancock",
    "program": "BSEd-Bio",
    "year_level": "3",
    "gender": "female"
  }
]
```

### Get Students by Year Level
```
GET /student/year/{year_level}
```
Returns all students in a specific year level.

**Parameters:**
- `year_level` (string): The year level (1, 2, 3, 4)

**Response:**
```json
[
  {
    "id_number": "2021-0036",
    "profile_url": null,
    "first_name": "Andre",
    "last_name": "Hancock",
    "program": "BSEd-Bio",
    "year_level": "3",
    "gender": "female"
  }
]
```

## Program Endpoints

### Get All Programs
```
GET /program/
```
Returns a list of all programs in the system.

**Response:**
```json
[
  {
    "code": "BSCS",
    "name": "BS in Computer Science",
    "college": "CCS"
  }
]
```

### Get Program by Code
```
GET /program/{program_code}
```
Returns details of a specific program.

**Parameters:**
- `program_code` (string): The program code

**Response:**
```json
{
  "code": "BSCS",
  "name": "BS in Computer Science",
  "college": "CCS"
}
```

### Create New Program
```
POST /program/create
```
Creates a new program record.

**Request Body:**
```json
{
  "code": "BSIT",
  "name": "BS in Information Technology",
  "college": "CCS"
}
```

**Response:**
```json
{
  "message": "Program created successfully",
  "program": {
    "code": "BSIT",
    "name": "BS in Information Technology",
    "college": "CCS"
  }
}
```

### Update Program
```
PUT /program/{program_code}
```
Updates an existing program record.

**Parameters:**
- `program_code` (string): The program code

**Request Body:**
```json
{
  "name": "Updated Program Name"
}
```

**Response:**
```json
{
  "message": "Program updated successfully"
}
```

### Delete Program
```
DELETE /program/{program_code}
```
Deletes a program record.

**Parameters:**
- `program_code` (string): The program code

**Response:**
```json
{
  "message": "Program deleted successfully"
}
```

### Get Programs by College
```
GET /program/college/{college_code}
```
Returns all programs in a specific college.

**Parameters:**
- `college_code` (string): The college code

**Response:**
```json
[
  {
    "code": "BSCS",
    "name": "BS in Computer Science",
    "college": "CCS"
  }
]
```

## College Endpoints

### Get All Colleges
```
GET /college/
```
Returns a list of all colleges in the system.

**Response:**
```json
[
  {
    "code": "CCS",
    "name": "College of Computer Studies"
  }
]
```

### Get College by Code
```
GET /college/{college_code}
```
Returns details of a specific college.

**Parameters:**
- `college_code` (string): The college code

**Response:**
```json
{
  "code": "CCS",
  "name": "College of Computer Studies"
}
```

### Create New College
```
POST /college/create
```
Creates a new college record.

**Request Body:**
```json
{
  "code": "NEW",
  "name": "New College"
}
```

**Response:**
```json
{
  "message": "College created successfully",
  "college": {
    "code": "NEW",
    "name": "New College"
  }
}
```

### Update College
```
PUT /college/{college_code}
```
Updates an existing college record.

**Parameters:**
- `college_code` (string): The college code

**Request Body:**
```json
{
  "name": "Updated College Name"
}
```

**Response:**
```json
{
  "message": "College updated successfully"
}
```

### Delete College
```
DELETE /college/{college_code}
```
Deletes a college record.

**Parameters:**
- `college_code` (string): The college code

**Response:**
```json
{
  "message": "College deleted successfully"
}
```

## Error Responses

All endpoints may return the following error responses:

### 404 Not Found
```json
{
  "error": "Student not found"
}
```

### 400 Bad Request
```json
{
  "error": "Error message describing the issue"
}
```

## Example Usage

### Using curl to get all students:
```bash
curl -X GET http://localhost:5000/student/
```

### Using curl to create a new student:
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

### Using curl to get students by program:
```bash
curl -X GET http://localhost:5000/student/program/BSCS
```

## Database Relationships

- **Students** belong to **Programs** (many-to-one)
- **Programs** belong to **Colleges** (many-to-one)
- **Colleges** have many **Programs** (one-to-many)
- **Programs** have many **Students** (one-to-many)

When querying related data, you can:
1. Get all students in a program: `/student/program/{program_code}`
2. Get all programs in a college: `/program/college/{college_code}`
3. Get all students in a college by first getting programs, then students for each program 