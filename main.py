def computepay(h, r):
    if h > 40:
        return r*(40 + 1.5*(h-40))
    else:
        return r*h

hrs = input("Enter Hours:")
dig_hrs = float(hrs)
rate = input("Enter Rate:")
dig_rate = float(rate)
p = computepay(dig_hrs, dig_rate)
print("Pay", p)
