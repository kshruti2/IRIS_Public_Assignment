from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

# Path to your Excel file
EXCEL_FILE = os.path.join(os.path.dirname(__file__), 'Data', 'capbudg.xls')

def get_excel_data():
    try:
        xl = pd.read_excel(EXCEL_FILE, sheet_name=None)
        return xl
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {str(e)}")

@app.get("/list_tables")
def list_tables():
    xl = get_excel_data()
    return {"tables": list(xl.keys())}

@app.get("/get_table_details")
def get_table_details(table_name: str):
    xl = get_excel_data()

    if table_name not in xl:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")

    df = xl[table_name]
    row_names = df.iloc[:, 0].dropna().astype(str).tolist()

    return {
        "table_name": table_name,
        "row_names": row_names
    }

@app.get("/row_sum")
def row_sum(table_name: str, row_name: str):
    xl = get_excel_data()

    if table_name not in xl:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")

    df = xl[table_name]
    row = df[df.iloc[:, 0].astype(str) == row_name]

    if row.empty:
        raise HTTPException(status_code=404, detail=f"Row '{row_name}' not found in table '{table_name}'.")

    # Sum of numeric values in the row (excluding the first column)
    numeric_sum = row.iloc[0, 1:].apply(pd.to_numeric, errors='coerce').sum()

    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": numeric_sum
    }

