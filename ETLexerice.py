

def extract():
    students = [
    {"id": 1, "name": "  arjun ", "grade": "85",  "subject": "math"},
    {"id": 2, "name": "PRIYA",    "grade": "92",  "subject": "science"},
    {"id": 3, "name": "rohan  ",  "grade": "bad", "subject": "math"},
    {"id": 4, "name": "  anita",  "grade": "78",  "subject": "science"},
    {"id": 5, "name": "bikash",   "grade": None,  "subject": "math"},
]
    
    print(f"extracted {len(students)} student records.")
    return students

def transform(data):
    clean_data=[];
    failed_data=[];
    for i in data:
        try:
            clean_data.append({
                 "id":i["id"],
                 "name":i["name"].strip().title(),
                 "grade":int(i["grade"]),
                 "pass": int(i["grade"]) >= 50,
                 "subject":i["subject"].strip().title()
             })
        except (ValueError, KeyError, TypeError) as e:
            print(f"Error occurred while transforming record {i['id']}: {e}")
            failed_data.append(i)
    return clean_data, failed_data

def load(data):
    print(f"Loading {len(data)} student records into the database...")
    for record in data:
        print(record)

def load_failed(failed_data):
    print(f"Loading {len(failed_data)} failed student records into the error log...")
    for record in failed_data:
        print(record)
        
        
        
students=extract()
cleaned_students, failed_students = transform(students)
load(cleaned_students)
load_failed(failed_students)