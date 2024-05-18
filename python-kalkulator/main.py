print(17 * "=")
print("Python Kalkulator")
print(17 * "=")

angka_1 = float(input("Masukkan Angka 1: "))
operator = input("Masukkan Operator (+, -, x, :): ")
angka_2 = float(input("Masukkan Angka 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == ":" or operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Hanya masukkan angka!")