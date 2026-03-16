import math

# Assign data to variables
principal = 172000
boe_rate = 2.25
rate_over_boe = 1.49

# Total annual interest rate
total_rate = boe_rate + rate_over_boe

# Monthly interest payment
interest = principal * (total_rate / 100) / 12

print(interest)

## test ##
assert math.isclose(interest, 536.0666666666667)
