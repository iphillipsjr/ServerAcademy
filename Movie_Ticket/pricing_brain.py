#Build the pricing brain of a movie theater. Given a customer's age and whether it's a discounted day (like
#Tuesday), your program decides the correct ticket price and prints the decision. This is exactly how real systems
#apply rules: compare some inputs, branch on the result, and act.
#
#You'll use everything through Section 3: comparisons, booleans, if / elif / else, and at least one nested conditional.
#
#Add a 'matinee' boolean for an extra $1 off before 5pm
#Print a friendly error message if age is negative
#Print something like: Adult ticket on discount day: $11

customer_age = 10
discounted_day = "yes"  # Change this to "no" for a regular day
time_of_day = 16  # Change this to a time before 5pm for a matinee showing

if customer_age < 0:
    print("Error: Age cannot be negative.")
elif customer_age < 13:
    customer_type = "Child"
elif customer_age < 65:
    customer_type = "Adult"
else:
    customer_type = "Senior"


if time_of_day < 17:
    matinee = True  # Change this to False for a regular showing
else:
    matinee = False

if customer_age < 0:
    print("Error: Age cannot be negative.")
elif discounted_day == "yes":
    if customer_type == "Child":
        ticket_price = 5.00  # Child price on discounted day
    elif customer_type == "Adult":
        ticket_price = 7.00  # Adult price on discounted day
    else:
        ticket_price = 6.00  # Senior price on discounted day
else:
    if customer_type == "Child":
        ticket_price = 8.00  # Child price on regular day
    elif customer_type == "Adult":
        ticket_price = 10.00  # Adult price on regular day
    else:
        ticket_price = 9.00  # Senior price on regular day
        customer_type = "Senior"
if matinee:
    ticket_price -= 1.00  # Apply matinee discount

print(customer_type + " ticket on " + ("discounted day" if discounted_day == "yes" else "regular day") +
       (" (Matinee discount applied)" if matinee else "") + ": $" + str(ticket_price))