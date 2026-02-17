# Name: Neelima Hansdah
# Roll No: IITP_AIMLH_2602218 
# Assignment: Python Loops & Automation - Subjective Question


print("===== Task 1: Find Maximum and Minimum =====")
temperatures= [28,32,35,29,31,27,30]
highest_temp = temperatures[0]
lowest_temp = temperatures[0]
count = 0
day_counter = 1
"""  """
for temp in temperatures:
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp

print("Highest Temperature:", highest_temp) 
print("Lowest Temperature:", lowest_temp)   


print("\n===== Task 2: Count Hot Days =====")
for temp in temperatures:
    
    if temp > 30:
        count=count+1
    continue
print("Hot days >30°C :", count) 

print("\n===== Task 3: Alert System =====") 

temperatures1= [28, 32, 35, 38, 40, 31, 33, 30]
for temp in temperatures1:
    if temp >= 40:
        print(f"Alert: Day {day_counter} has a high temperature of {temp}°C!")
        break
    day_counter += 1 

count = 0
for temp in temperatures1[:day_counter-1]:
    if temp >= 30:
        count  += 1
    
print(f"Hot Days before alert: {count}")

    

