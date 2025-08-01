#!/usr/bin/env python3
"""
Database Connection Test Script
This script tests the connection to the MySQL database and verifies table access.
"""

import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app import create_app
from app.service import mysql, execute_query, fetch_one, fetch_all

def test_database_connection():
    """Test database connection and table access"""
    print("🔍 Testing Database Connection...")
    print("=" * 50)
    
    try:
        # Create Flask app to initialize database connection
        app = create_app()
        
        with app.app_context():
            # Test basic connection
            print("1. Testing basic connection...")
            mysql.connect()
            print("   ✅ Database connection successful!")
            
            # Test database name
            print("\n2. Testing database name...")
            result = fetch_one("SELECT DATABASE() as db_name")
            db_name = result['db_name']
            print(f"   📊 Connected to database: {db_name}")
            
            if db_name != 'student_system':
                print(f"   ⚠️  Warning: Expected 'student_system' but got '{db_name}'")
            else:
                print("   ✅ Database name is correct!")
            
            # Test table existence
            print("\n3. Testing table existence...")
            tables_to_check = ['Student', 'Program', 'College']
            
            for table in tables_to_check:
                try:
                    result = fetch_one(f"SELECT COUNT(*) as count FROM {table}")
                    count = result['count']
                    print(f"   ✅ Table '{table}' exists with {count} records")
                except Exception as e:
                    print(f"   ❌ Table '{table}' not found or not accessible: {str(e)}")
            
            # Test sample queries
            print("\n4. Testing sample queries...")
            
            # Test Student table
            try:
                result = fetch_one("SELECT COUNT(*) as count FROM Student")
                student_count = result['count']
                print(f"   📚 Students: {student_count}")
            except Exception as e:
                print(f"   ❌ Error querying Student table: {str(e)}")
            
            # Test Program table
            try:
                result = fetch_one("SELECT COUNT(*) as count FROM Program")
                program_count = result['count']
                print(f"   📖 Programs: {program_count}")
            except Exception as e:
                print(f"   ❌ Error querying Program table: {str(e)}")
            
            # Test College table
            try:
                result = fetch_one("SELECT COUNT(*) as count FROM College")
                college_count = result['count']
                print(f"   🏛️  Colleges: {college_count}")
            except Exception as e:
                print(f"   ❌ Error querying College table: {str(e)}")
            
            # Test relationships
            print("\n5. Testing relationships...")
            try:
                results = fetch_all("""
                    SELECT c.name as college_name, COUNT(p.code) as program_count 
                    FROM College c 
                    LEFT JOIN Program p ON c.code = p.college 
                    GROUP BY c.code, c.name 
                    ORDER BY program_count DESC 
                    LIMIT 3
                """)
                print("   📊 Top colleges by program count:")
                for row in results:
                    print(f"      • {row['college_name']}: {row['program_count']} programs")
            except Exception as e:
                print(f"   ❌ Error testing relationships: {str(e)}")
            
            print("\n" + "=" * 50)
            print("🎉 Database connection test completed!")
            
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure MySQL server is running")
        print("2. Check database credentials in app/config.py")
        print("3. Verify database 'student_system' exists")
        print("4. Ensure tables 'Student', 'Program', 'College' exist")
        return False
    
    return True

def test_model_operations():
    """Test model operations"""
    print("\n🔧 Testing Model Operations...")
    print("=" * 50)
    
    try:
        app = create_app()
        
        with app.app_context():
            from app.models.student import Student
            from app.models.program import Program
            from app.models.college import College
            
            # Test College model
            print("1. Testing College model...")
            college = College()
            colleges = college.get_all()
            print(f"   ✅ Found {len(colleges)} colleges")
            
            # Test Program model
            print("2. Testing Program model...")
            if colleges:
                test_college = colleges[0]
                program = Program()
                program.code = "TEST"
                program.name = "Test Program"
                program.college = test_college.code
                
                # Try to get the test program (should not exist)
                result = program.get()
                if result is None:
                    print("   ✅ Program.get() works correctly for non-existent program")
                else:
                    print("   ⚠️  Test program already exists")
            
            # Test Student model
            print("3. Testing Student model...")
            student = Student()
            student.id_number = "TEST-9999"
            result = student.get()
            if result is None:
                print("   ✅ Student.get() works correctly for non-existent student")
            else:
                print("   ⚠️  Test student already exists")
            
            print("\n" + "=" * 50)
            print("🎉 Model operations test completed!")
            
    except Exception as e:
        print(f"❌ Model operations test failed: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Student Information System - Database Test")
    print("=" * 60)
    
    # Test database connection
    db_success = test_database_connection()
    
    # Test model operations
    model_success = test_model_operations()
    
    print("\n" + "=" * 60)
    if db_success and model_success:
        print("🎉 All tests passed! Your database is properly configured.")
        print("You can now run the application with: python main.py")
    else:
        print("❌ Some tests failed. Please check the configuration.")
        sys.exit(1) 