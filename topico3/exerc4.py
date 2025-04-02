sal = int(input("Qual o salario"))
roubo= 0

if sal <= 1903.98:
    print("Droga é 0 de imposto")
elif sal > 1903.98 and sal < 2826.65:
    print(f"Vai perder ",sal * 0.075)
elif sal < 3751.05 and sal > 2826.65:
    print(f"Vai perder ",sal * 0.15)
elif sal > 3751.05:
    print(f"Vai perder ",sal * 0.225)
