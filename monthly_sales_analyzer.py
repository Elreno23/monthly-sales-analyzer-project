# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for product in data:
        total += product[product_key]
    return total


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total = 0
    for product in data:
        total += product[product_key]
    average = total / len(data)
    return average

def best_selling_day(data):
    """Finds the day with the highest total sales."""
    highest_sales = float("-inf")
    best_day = None
    for days in data:
        total = 0
        for key, value in days.items():
            if key != 'day':
                total += value
                print(f"SUMA DE LAS VENTAS DE PRODUCTOS: {total}")
        if total > highest_sales:
            highest_sales = total
            best_day = days["day"]
    return best_day

def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    count = 0
    for day in data:
        if day[product_key] > threshold:
            count += 1
    return f"ESTA ES LA CANTIDAD DE DIAS QUE SUPERARON EL UMBRAL {count}"


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    products = {"product_a":0,"product_b":0,"product_c":0}
    for day in data:
        products["product_a"] += day["product_a"]
        products["product_b"] += day["product_b"]
        products["product_c"] += day["product_c"]

    top_product = float("-inf")
    for product,value in products.items():
        if value > top_product:
            top_product = value
    
    return product, top_product
            
def worst_selling_day(data):
    lower_sales = float("inf")
    worst_day_sale = 0 

    for day in data:
        total = 0
        for key,value in day.items():
            if key != "day":
                total += value
        if total < lower_sales:
            lower_sales = total
            worst_day_sale = day["day"]
    return worst_day_sale

def top_three_total_sales(data):
    total_sales = []
    for day in data:
        days = 0 
        total = 0
        for key, value in day.items():
            if key != "day":
              total += value
            else:
                days = value
        total_sales.append([days,total])
    total_sales.sort(key=lambda x: x[1], reverse=True)
    print(total_sales)
    top1=total_sales[0][0]
    top2=total_sales[1][0]
    top3=total_sales[2][0]
    
    return top1,top2,top3

def sales_range(data, product_key):
    highest_sale = float("-inf")#200
    smallest_sale = float("inf")#100
    for day in data:
        if day[product_key] > highest_sale:
            highest_sale = day[product_key]
        elif day[product_key] < smallest_sale:
            smallest_sale = day[product_key]
    print(highest_sale)
    print(smallest_sale)
    return highest_sale - smallest_sale
          
# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("the day with the worst sales:", worst_selling_day(sales_data))
print("top three days by total sales:", top_three_total_sales(sales_data))
print("range of a product's sales:", sales_range(sales_data,"product_a"))