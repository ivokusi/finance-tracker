from datetime import datetime
import pandas as pd
import csv 
import os

class CSV:

    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        
        if os.path.exists(cls.CSV_FILE):

            pd.read_csv(cls.CSV_FILE)

        else:
            
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):

        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        
        print("New entry added succesfully")
        
CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")
