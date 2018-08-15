cm = float(input("chieu cao cua ban: "))
kg = float(input("can nang cua ban: "))
m = cm / 100
BMI = kg / (m * m)

if BMI < 16:
    print("giam can nang")
elif BMI < 18.5:
    print("thieu can")
elif BMI < 25:
    print("binh thuong")
elif BMI < 30:
    print("thua can")
else:
    print("beo phi")
