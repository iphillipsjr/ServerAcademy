""" Turn a week of raw sales numbers into a useful report. Given a list of daily sales, 
your program loops through them to compute the total, the number of days, the average, the best day, and how many days beat a target. 
This is the core pattern behind every dashboard and analytics tool: take a list of data and summarize it.

You'll use everything through Section 4: lists, indexing, for loops, range(), while loops, and running totals and counters. 
Also find the worst day
Use a while loop somewhere (e.g. to scan the list) to practice both loop types
"""


print("-------- Sales Report --------")

daily_sales = [100, 200, 300, 400, 500, 600, 700]
total_sales = 0
for sale in daily_sales:
    total_sales += sale
print(f"Total sales: {total_sales}")

number_of_days = len(daily_sales)
print(f"Number of days: {number_of_days}")

average_sales = total_sales / number_of_days
print(f"Average sales: {average_sales}")

best_day = max(daily_sales)
print(f"Best day sales: {best_day}")

worst_day = min(daily_sales)
print(f"Worst day sales: {worst_day}")

target_sales = 400
days_beat_target = 0
for sale in daily_sales:
    if sale > target_sales:
        days_beat_target += 1
print(f"Days that beat the target: {days_beat_target}") 

print("\nDaily sales report:")

while_loop_counter = 0
while while_loop_counter < number_of_days:
    print(f"Day {while_loop_counter + 1} sales: {daily_sales[while_loop_counter]}")
    while_loop_counter += 1
