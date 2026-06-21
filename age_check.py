print("Напиши свой возраст:")
age = float(input())
if age < 18:
    print("Ты несовершеннолетний")
elif 18<=age<=65:
    print("Ты взрослый")
else:
    print("Ты пенсионер")
