import pandas as pd


students = [
    {"id": 1, "name": "  arjun ", "grade": "85",  "subject": "math"},
    {"id": 2, "name": "PRIYA",    "grade": "92",  "subject": "science"},
    {"id": 3, "name": "rohan  ",  "grade": "bad", "subject": "math"},
    {"id": 4, "name": "  anita",  "grade": "78",  "subject": "science"},
    {"id": 5, "name": "bikash",   "grade": None,  "subject": "math"},
    
     {"id": 2, "name": "PRIYA",    "grade": "92",  "subject": "science"},
    {"id": 3, "name": "rohan  ",  "grade": "bad", "subject": "math"},
    {"id": 4, "name": "  anita",  "grade": "78",  "subject": "science"},
    {"id": 5, "name": "bikash",   "grade": None,  "subject": "math"},
]


df=pd.DataFrame(students);


# print(df)

print("\n shape of data \n", df.shape)

print("\n all null values\n", df.isnull().sum())


df["name"]= df["name"].str.strip().str.title();

df["grade"]= pd.to_numeric(df["grade"] ,errors="coerce")

df["pass"]= df["grade"]> 80

clean= df[df["grade"].notnull()]

print(clean)