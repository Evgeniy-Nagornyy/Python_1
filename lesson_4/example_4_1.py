from sys import argv

script_name, hours, h_money, premium = argv

print("Employee salary = ", int(hours) * int(h_money) + int(premium))
