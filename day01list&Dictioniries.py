pipeline_lists=["extract","transform","load"]

print("Pipeline Steps:",pipeline_lists)

print("pipeline step first step:", pipeline_lists[0]) # indexing starts from 0
print("pipeline step last step:", pipeline_lists[-1]) # negative indexing starts from -1 and goes backwards

pipeline_lists.append("validate") # adding a new step to the list
print("Pipeline Steps after adding validate:",pipeline_lists) #it add in the end of the list

#Dictionaries are like JSON in Python. They are used to store data in key-value pairs. They are unordered, mutable and indexed.

employee={"name":"Nitesh", "age": 25, "designation": "Data Scientist", "skills"
          : ["Python", "Data Science", "Machine Learning"]}



print("\nEmployee Details:", employee["name"]) # accessing value using key

employee["experience"] = 3 # adding a new key-value pair to the dictionary
print("Employee Details after adding experience:", employee)


for key, value in employee.items(): # iterating through the dictionary
    print(f"{key}: {value}")

