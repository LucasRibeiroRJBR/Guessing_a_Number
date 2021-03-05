from random import randint
import tkinter as tk

def adivinhar():
    pass

root = tk.Tk()
root.title('Jogo de Adivinhação')
root.config(background='#24293A')

c_erros = 0

# IMAGENS


# LABELS
lb_letreiro = tk.Label(root,
                    text='Jogo de Adivinhação',
                    font=('Arial', 24, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')
lb_tentativas = tk.Label(root,
                    text=str(c_erros),
                    font=('Arial', 14, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')
lb_n = tk.Label(root,
                    text='Digite um número: ',
                    font=('Arial', 14, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')

# ENTRIES
varN = tk.StringVar()
input_n = tk.Entry(root, textvariable=varN)

# BUTTON
bt_verificar = tk.Button(root, text = 'Enter The Text', command = adivinhar)

# Grid
lb_letreiro.grid(row=0,columnspan=2)
lb_tentativas.grid(row=1, column=0, sticky='w')
lb_n.grid(row=2, column=0)
input_n.grid(row=2, column=1, sticky='w')
bt_verificar.grid(row = 3, column = 1)

root.mainloop()
