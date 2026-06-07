# def greet_user(name):
#     return f"Hello, {name}! Welcome to the world of Python functions."


# message = greet_user("Nitesh")
# print(message)

# #function with multiple parameters

# def calculate_pipeline_stats(total_records, failed_records):
#     succesfull_records = total_records - failed_records
#     success_rate = (succesfull_records / total_records) * 100       
#     return succesfull_records, success_rate

# successful, rate = calculate_pipeline_stats(1000, 50)
# print(f"Successful Records: {successful}, Success Rate: {rate:.2f}%")


# # --- THE 3 PIPELINE FUNCTIONS (extract, transform, load) ---
# # This is literally the skeleton of every ETL pipeline you will ever build

def extract():
    raw_data = [
        {"id": 1, "name": "  nitesh ", "salary": "50000", "city": "kathmandu"},
        {"id": 2, "name": "  ram",     "salary": "45000", "city": "pokhara"},
        {"id": 3, "name": "sita  ",    "salary": "bad_value", "city": "lalitpur"},
    ]
    print(f"Extracted {len(raw_data)} records.")
    return raw_data


def transform(data):
    cleaned_data = []
    failed_records = [] # to keep track of records that failed transformation
    for r in data:
        try:
            cleaned_data.append({
                "id": r["id"],
                "name": r["name"].strip().title(),  # clean name
                "salary": int(r["salary"]),         # convert salary to int
                "city": r["city"].strip().title()   # clean city
            })
        except (ValueError, KeyError) as e:
            print(f"Error occurred while transforming record {r['id']}: {e}")
            failed_records.append(r)

    print(f"Transformed {len(cleaned_data)} records.")
    print(f"Failed to transform {len(failed_records)} records.")
    return cleaned_data, failed_records

def load(data):
    print(f"Loading {len(data)} records into the database...")
    # Here you would normally have code to connect to a database and insert the data
    # For this example, we'll just print the cleaned data
    for record in data:
        print(record)

def load_failed(failed_records):
    print(f"Loading {len(failed_records)} failed records into the error log...")
    for record in failed_records:
        print(record)

raw=extract()
cleaned, failed = transform(raw)
load(cleaned)
failed_records = load_failed(failed)