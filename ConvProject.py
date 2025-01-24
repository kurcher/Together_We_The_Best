import json
from urllib.request import urlopen
from tkinter import Tk, Label, Entry, Button, messagebox, StringVar, Radiobutton


def get_usd_to_uah_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
            for currency in data:
                if currency['cc'] == 'USD':
                    return currency['rate']
    except Exception as e:
        messagebox.showerror("Error", f"Fetching exchange rate: {e}")
        return None


def conv_to_uah(rate, count_of_usd):
    conv_from_usd_to_uah = int(float(count_of_usd) * rate)
    rounded_1 = round(conv_from_usd_to_uah, 2)
    return rounded_1


def conv_to_usd(rate, count_of_uah):
    conv_from_uah_to_usd = (float(count_of_uah) / rate)
    rounded_2 = round(conv_from_uah_to_usd, 2)
    return rounded_2


def interface():
    def convert():

        rate = get_usd_to_uah_rate()
        if rate is None:
            return


        amount = entry.get()
        conversion = conversion_type.get()

        if conversion == "to_uah":
            result = conv_to_uah(rate, amount)
            if result is not None:
                messagebox.showinfo("Result", f"{amount} USD = {result} UAH")
        elif conversion == "to_usd":
            result = conv_to_usd(rate, amount)
            if result is not None:
                messagebox.showinfo("Result", f"{amount} UAH = {result} USD")
        else:
            messagebox.showinfo("Choose", "Choose a conversion type!")


    root = Tk()
    root.title("CURRENCY CONVERTOR")
    root.configure(bg="#FFFFFF")
    root.geometry("400x250")

    Label(root, bg="#d5e3df", text="Enter:", font="Arial").pack(pady=10)
    entry = Entry(root, width=20)
    entry.pack(pady=5)

    conversion_type = StringVar(value="to_uah")
    Radiobutton(root, text="USD → UAH", font="Arial", variable=conversion_type, value="to_uah").pack(anchor="w", padx=50)
    Radiobutton(root, text="UAH → USD", font="Arial", variable=conversion_type, value="to_usd").pack(anchor="w", padx=50)

    Button(root, bg="#95baae",text="Convert", font="Arial", command=convert).pack(pady=20)

    root.mainloop()

interface()
