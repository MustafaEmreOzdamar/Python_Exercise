import tkinter as tk
from tkinter import messagebox

# Roma rakamlarını tam sayıya çevirme fonksiyonu
def roman_to_int(roman_number: str) -> int:
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    int_value = 0

    for i in range(len(roman_number)):
        if roman_number[i] in roman_numbers:
            if i + 1 < len(roman_number) and roman_numbers[roman_number[i]] < roman_numbers[roman_number[i + 1]]:
                int_value -= roman_numbers[roman_number[i]]
            else:
                int_value += roman_numbers[roman_number[i]]
        else:
            return None

    return int_value

# Çevirme işlemindeki kontrolü sağlayan fonksiyon
def convert():
    roman_number = entry.get().upper()
    integer_value = roman_to_int(roman_number)

    if integer_value is None:
        messagebox.showerror("Hata", "Geçersiz Roma rakamı girdiniz!")
    elif integer_value > 4999 or integer_value < 1:
        messagebox.showerror("Hata", "Sayı 1 ile 4999 arasında olmalı!")
    else:
        result_label.config(text=f"Sonuç: {integer_value}")

root = tk.Tk()
root.title("Roma Rakamı Çevirici")

entry_label = tk.Label(root, text="Roma Rakamı:")
entry_label.pack(pady=15)

entry = tk.Entry(root)
entry.pack(pady=15)

convert_button = tk.Button(root, text="Çevir", command=convert)
convert_button.pack(pady=30)

result_label = tk.Label(root, text="Sonuç: ")
result_label.pack(pady=15)

root.mainloop()
