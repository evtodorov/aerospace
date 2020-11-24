capitalStart = int(input("Capital: ")*100.)/100.
rate =input("Rate (in percent): ")/100.
time = float(input("Time (in years): "))

capitalEnd = capitalStart*(rate+1)**time

print int(capitalEnd*100)/100.
