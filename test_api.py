#!/usr/bin/env python3
"""
Simple test script for the Student Information System API
Run this script to test the basic functionality of the API endpoints
"""

import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, method="GET", data=None):
    """Test a single endpoint"""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        elif method == "PUT":
            response = requests.put(url, json=data, headers={'Content-Type': 'application/json'})
        elif method == "DELETE":
            response = requests.delete(url)
        
        print(f"{method} {endpoint}")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200 or response.status_code == 201:
            try:
                result = response.json()
                if isinstance(result, list):
                    print(f"Response: {len(result)} items returned")
                    if result:
                        print(f"First item: {json.dumps(result[0], indent=2)}")
                else:
                    print(f"Response: {json.dumps(result, indent=2)}")
            except:
                print(f"Response: {response.text}")
        else:
            print(f"Error: {response.text}")
        
        print("-" * 50)
        return response.status_code == 200 or response.status_code == 201
        
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Could not connect to {url}")
        print("Make sure the Flask application is running on localhost:5000")
        print("-" * 50)
        return False
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("-" * 50)
        return False

def main():
    """Run all tests"""
    print("Student Information System API Test")
    print("=" * 50)
    
    # Test College endpoints
    print("\nTesting College Endpoints:")
    test_endpoint("/college/")
    test_endpoint("/college/CCS")
    
    # Test Program endpoints
    print("\nTesting Program Endpoints:")
    test_endpoint("/program/")
    test_endpoint("/program/BSCS")
    test_endpoint("/program/college/CCS")
    
    # Test Student endpoints
    print("\nTesting Student Endpoints:")
    test_endpoint("/student/")
    test_endpoint("/student/2021-0036")
    test_endpoint("/student/program/BSCS")
    test_endpoint("/student/year/3")
    
    print("\nTest completed!")

if __name__ == "__main__":
    main() 