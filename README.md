# IRIS Public Assignment

# 📌 Project Overview

This project is a FastAPI-based backend application designed to process Excel sheets and expose RESTful APIs to retrieve and perform computations on their data. It was developed as part of the IRIS Public Assignment to demonstrate proficiency in Python backend development, API design, and data handling using Pandas.

The API processes an Excel file (capbudg.xls) containing multiple tables (sheets). Users can:

📂 List all tables

📋 View details of rows in a specific table

➕ Calculate the sum of numerical values for a selected row

It includes an interactive Swagger documentation and a Postman collection for easy testing.

# ✅ Features

 Reads complex Excel files with multiple sheets

 Provides API endpoints to interact with the data

 Calculates row-wise numeric sums

 Includes Postman Collection for testing

 Simple, clean, well-documented code

# ⚙️ Tech Stack

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| **FastAPI**  | Web framework for API building  |
| **Pandas**   | Reading & processing Excel data |
| **Uvicorn**  | ASGI server for running FastAPI |
| **OpenPyXL** | Excel support for Pandas        |

 # 📡 API Endpoints

| Method | Endpoint                                     | Description                              |
| ------ | -------------------------------------------- | ---------------------------------------- |
| GET    | `/list_tables`                               | Lists all table (sheet) names in Excel   |
| GET    | `/get_table_details?table_name=<sheet>`      | Lists first-column values of the sheet   |
| GET    | `/row_sum?table_name=<sheet>&row_name=<row>` | Returns numeric sum of the specified row |

# 💡 Potential Improvements

✅ Add authentication to secure API endpoints

✅ Allow uploading different Excel files dynamically

✅ Add frontend UI for seamless interaction

✅ Handle edge cases like empty sheets or invalid formats gracefully

# ⚠️ Known Edge Cases

| Scenario                  | Current Handling                    |
| ------------------------- | ----------------------------------- |
| Excel file missing        | Returns HTTP 500 with error message |
| Sheet name not present    | Returns HTTP 404                    |
| Row name not present      | Returns HTTP 404                    |
| Non-numeric values in row | Ignored during summation            |

# 📊  My Insights

🔧 Potential Improvements

✅ Dynamic File Upload: Allow users to upload Excel files via API instead of using a fixed file.

✅ Advanced Operations: Support for averages, medians, or filtering specific rows/columns.

✅ Authentication: Add API key/token-based access for security.

✅ UI Integration: Develop a creative, user-friendly frontend interface (React or Streamlit).

✅ Deployment: Dockerize for smooth deployment on cloud platforms like Heroku or AWS.

# 📦 Installation Instructions

1️⃣ Clone the Repository : git clone https://github.com/your-username/IRIS_Public_Assignment.git
cd IRIS_Public_Assignment

2️⃣ Install Python Dependencies : pip install -r requirements.txt

3️⃣ Run the FastAPI Application : uvicorn main:app --reload --port 9090

4️⃣ Access API Docs : http://localhost:9090/docs 

# Postman Collection Usage

📁 Postman Collection File Location: postman_collection/IRIS_Assignment.postman_collection.json

📥 Importing into Postman

1️⃣ Open Postman

2️⃣ Click Import → File

3️⃣ Choose: IRIS_Public_Assignment/postman_collection/IRIS_Assignment.postman_collection.json

