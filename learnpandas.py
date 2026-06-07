import pandas as pd

students = [
    {"id": 1, "name": "  arjun ", "grade": "85",  "subject": "math"},
    {"id": 2, "name": "PRIYA",    "grade": "92",  "subject": "science"},
    {"id": 3, "name": "rohan  ",  "grade": "bad", "subject": "math"},
    {"id": 4, "name": "  anita",  "grade": "78",  "subject": "science"},
    {"id": 5, "name": "bikash",   "grade": None,  "subject": "math"},
]

# #loading data into a pandas dataframe

df=pd.DataFrame(students)
# print(df)
# print("\nDataFrame Info:",df.shape)

# print(df.isnull().sum()) # check for missing values

# math= df[df["subject"]=="math"] # filter math students
# print("\nMath Students:\n", math)

# valid= df[df["grade"].notnull() & (df["grade"] != "bad")] # filter valid grades
# print("\nValid Grades:\n", valid)


df["name"]= df["name"].str.strip().str.title() # clean name column

df["grade"]=pd.to_numeric(df["grade"], errors="coerce") # convert grade to numeric, invalid parsing will be set as NaN

df["pass"]=df["grade"] >= 50 # create pass column based on grade

clean= df[df["grade"].notnull()] # filter out records with valid grades
failed= df[df["grade"].isnull()] # filter out records with invalid grades

print("\nCleaned Data:\n", clean)
print("\nFailed Records:\n", failed)

print(clean.groupby("subject")["grade"].mean()) # average grade by subject

print("\n=== HIGHEST GRADE ===")
print(clean["grade"].max())

print("\n=== STUDENT WITH HIGHEST GRADE ===")
print(clean[clean["grade"] == clean["grade"].max()])