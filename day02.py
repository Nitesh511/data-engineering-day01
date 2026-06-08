salaries= [25000, 45000, 60000, 30000, 75000]

average_salary = sum(salaries) / len(salaries)
print(f"Average Salary: {average_salary:.2f}")

data = "data,engineering,is,fun"
fields = data.split(",")
for f in fields:
    print(f)
    
    
    
new_data={"product": "laptop", "price": 80000, "discount": 10}

def calculate_price(product_data):
    return product_data["price"] * (1 - product_data["discount"] / 100)

print(f"Discounted Price: {calculate_price(new_data):.2f}")

people = [
    {"name": "Nitesh", "age": 25},
    {"name": "Ram", "age": 30},
    {"name": "Sita", "age": 22},
]

names = [p["name"] for p in people]
print(names)

numbers = [12, 45, 78, 23, 56, 89, 34]

def new_fun(number):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)
max_num, min_num, avg_num = new_fun(numbers)
print(f"Max: {max_num}, Min: {min_num}, Average: {avg_num:.2f}")