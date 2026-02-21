import tkinter as tk

def somar():
    n1 = float(num1.get())
    n2 = float(num2.get())
    resultado.set(n1 + n2)

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x300")

num1 = tk.Entry(janela)
num1.pack(pady=10)

num2 = tk.Entry(janela)
num2.pack(pady=10)

resultado = tk.StringVar()

tk.Button(janela, text="Somar", command=somar).pack(pady=10)

tk.Label(janela, textvariable=resultado).pack(pady=10)

janela.mainloop()