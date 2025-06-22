class Kalkulator():
    def __init__(self, angka_pertama, angka_kedua):
        self.angka_pertama = angka_pertama
        self.angka_kedua = angka_kedua

    def pertambahan(self):
        return self.angka_pertama + self.angka_kedua

    def pengurangan(self):
        return self.angka_pertama - self.angka_kedua

    def perkalian(self):
        return self.angka_pertama * self.angka_kedua

    def pembagian(self):
        if self.angka_kedua != 0:
            return self.angka_pertama / self.angka_kedua
        else:
            return "Error: Tidak bisa dibagi nol!"

    def modulo(self):
        if self.angka_kedua != 0:
            return self.angka_pertama % self.angka_kedua
        else:
            return "Error: Tidak bisa dibagi nol!"


def main():
    while True:
        print(10 * "=", "Kakulator", 10 * "=")
        angka_pertama = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+,-,*,/,%): ")
        angka_kedua = float(input("Masukkan angka kedua: "))
        kalkulator = Kalkulator(angka_pertama, angka_kedua)

        if operator == "+":
            print(f"Hasil: {kalkulator.pertambahan()}")
        elif operator == "-":
            print(f"Hasil {kalkulator.pengurangan()}")
        elif operator == "*":
            print(f"Hasil {kalkulator.perkalian()}")

        elif operator == "/":
            print(f"Hasil {kalkulator.pembagian()}")
        elif operator == "%":
            print(f"Hasil {kalkulator.modulo()}")
        else:
            print("Operator tidak dikenal!")

        pilihan = str(input("Apakah ingin lanjut? (y/n): "))
        if pilihan.lower() != "y":
            print("Terima Kasih.")
            break


main()
