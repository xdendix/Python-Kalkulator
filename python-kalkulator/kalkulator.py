class Kalkulator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tambah(self):
        return self.a + self.b

    def kurang(self):
        return self.a - self.b

    def kali(self):
        return self.a * self.b

    def bagi(self):
        return self.a / self.b if self.b != 0 else "Error: Tidak bisa dibagi nol!"

    def modulo(self):
        return self.a % self.b if self.b != 0 else "Error: Tidak bisa dibagi nol!"


def main():
    while True:
        print("=" * 10, "Kalkulator", "=" * 10)
        a = float(input("Masukkan angka pertama: "))
        op = input("Masukkan operator (+,-,*,/,%): ")
        b = float(input("Masukkan angka kedua: "))
        k = Kalkulator(a, b)

        if op == "+":
            print(f"Hasil: {k.tambah()}")
        elif op == "-":
            print(f"Hasil {k.kurang()}")
        elif op == "*":
            print(f"Hasil {k.kali()}")
        elif op == "/":
            print(f"Hasil {k.bagi()}")
        elif op == "%":
            print(f"Hasil {k.modulo()}")
        else:
            print("Operator tidak dikenal!")

        if input("Apakah ingin lanjut? (y/n): ").lower() != "y":
            print("Terima Kasih.")
            break


main()
