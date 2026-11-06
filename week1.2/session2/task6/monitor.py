# Week 1.2, Session 2: Task 6

temperature = int(input("Machine temperature in Celsius: "))
pressure = int(input("Machine pressure in PSI: "))
status = int(input("Machine status (1 = operating, 0 = stopped): "))

if temperature > 80:
    print("The temperature is too high, shut the machine down")
elif temperature >= 50:
    print("The temperature is safe")
else:
    print("The temperature is low, nothing to do")

if pressure > 100:
    print("The pressure is too high, maintenance is needed")
elif pressure >= 70:
    print("The pressure is stable")
else:
    print("The pressure is low, everything is normal")

if status == 1:
    if temperature > 80 or pressure > 100:
        print("The machine is running unsafe, shut it down")
    else:
        print("The machine is running normally")
else:
    print("The machine is stopped, nothing to do")
