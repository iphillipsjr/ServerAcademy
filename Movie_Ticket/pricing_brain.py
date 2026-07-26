#Build the pricing brain of a movie theater. Given a customer's age and whether it's a discounted day (like
#Tuesday), your program decides the correct ticket price and prints the decision. This is exactly how real systems
#apply rules: compare some inputs, branch on the result, and act.
#
#You'll use everything through Section 3: comparisons, booleans, if / elif / else, and at least one nested conditional.

customer_age = 40
discounted_day = "yes"  # Change this to "no" for a regular day

if discounted_day == "yes":
    if customer_age < 13:
        ticket_price = 5.00  # Child price on discounted day
    elif customer_age < 65:
        ticket_price = 7.00  # Adult price on discounted day
    else:
        ticket_price = 6.00  # Senior price on discounted day
else:
    if customer_age < 13:
        ticket_price = 8.00  # Child price on regular day
    elif customer_age < 65:
        ticket_price = 10.00  # Adult price on regular day
    else:
        ticket_price = 9.00  # Senior price on regular day  

print(f"The ticket price is: ${ticket_price:.2f}")
