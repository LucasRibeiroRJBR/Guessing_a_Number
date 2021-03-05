from random import randint
import tkinter as tk
import pyglet

pyglet.font.add_file('font/HYWenHei.ttf')

def adivinhar():
    global c_erros
    
    if int(varN.get()) < comp:
        lb_status.config(image=img_up)
        c_erros += 1
        lb_tentativas['text'] = c_erros
    elif int(varN.get()) > comp:
        lb_status.config(image=img_down)
        c_erros += 1
        lb_tentativas['text'] = c_erros
    elif int(varN.get()) == comp:
        lb_status.config(image=img_trophy)
        bt_resetar.grid(row = 3, column = 0, sticky='w')
    
    input_n.delete(0, 'end')
    input_n.insert(0, '')

def resetar():
    global comp
    global c_erros

    comp = randint(1, 100)
    c_erros = 0

    lb_tentativas['text'] = c_erros
    lb_status['image'] = img_initial

    bt_resetar.grid_forget()

root = tk.Tk()
root.title('Jogo de Adivinhação')
root.config(background='#24293A')

comp = randint(1, 100)
c_erros = 0

# IMAGENS
img_up = tk.PhotoImage(file='img/up.png')
img_down = tk.PhotoImage(file='img/down.png')
img_initial = tk.PhotoImage(file='img/initial.png')
img_check = tk.PhotoImage(file='img/check.png')
img_trophy = tk.PhotoImage(file='img/trophy.png')
img_reset = tk.PhotoImage(file='img/reset.png')


# LABELS
lb_letreiro = tk.Label(root,
                    text='Jogo de Adivinhação',
                    font=('HYWenHei-85W', 24, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')
lb_tentativas = tk.Label(root,
                    text=str(c_erros),
                    font=('HYWenHei-85W', 32, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')
lb_n = tk.Label(root,
                    text='Digite um número: ',
                    font=('HYWenHei-85W', 14, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')
lb_status = tk.Label(root,
                    image=img_initial,
                    font=('HYWenHei-85W', 14, 'bold'),
                    foreground='#7B8DC7',
                    background='#24293A')

# ENTRIES
varN = tk.StringVar()
input_n = tk.Entry(root,
                    textvariable=varN,
                    font=('HYWenHei-85W', 14, 'bold'),
                    background='#2C3347',
                    foreground='#7B8DC7',
                    width=12)

# BUTTON
bt_resetar = tk.Button(root,
                        image=img_reset,
                        command = resetar,
                        borderwidth=0,
                        activebackground='#2C3347',
                        background='#24293A')

bt_verificar = tk.Button(root,
                        image=img_check,
                        command = adivinhar,
                        borderwidth=0,
                        activebackground='#2C3347',
                        background='#24293A')

# Grid
lb_letreiro.grid(row=0,columnspan=2)
lb_tentativas.grid(row=1, column=0)
lb_status.grid(row=1, column=1)
lb_n.grid(row=2, column=0)
input_n.grid(row=2, column=1, sticky='w', padx=15)
bt_resetar.grid(row = 3, column = 0, sticky='w')
bt_verificar.grid(row = 3, column = 1, sticky='e')

bt_resetar.grid_forget()

root.mainloop()
