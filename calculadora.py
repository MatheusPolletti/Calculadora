from tkinter import *

def botao_apertado(num):
    global equation_text

    equation_text = equation_text + str(num)
    if '**' in equation_text:
        equation_label.set(equation_text.replace('**', '^'))
    else:
        equation_label.set(equation_text)

    print(equation_text)


def igual():
    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Erro! Divisão por zero!')
    except SyntaxError:
        equation_label.set('Erro de sintaxe!')


def limpar():
    global equation_text

    equation_label.set('')
    equation_text = ''


janela = Tk()

icone = PhotoImage(file='calculadora.png')
janela.iconphoto(True, icone)

janela.title('Calculadora Polletti')

janela.geometry('436x615')

janela.config(bg='#a9a9a9')

equation_text = ''
equation_label = StringVar()

label = Label(janela, textvariable=equation_label, font=('Arial', 20), bg='#2B2B2B', fg='#FDFDF6', width=27, height=2)
label.pack()

frame = Frame(janela)
frame.pack()

botao1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda:botao_apertado(1), bg='#484848', fg='#FDFDFD')
botao1.grid(row=0, column=0)

botao2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda:botao_apertado(2), bg='#484848', fg='#FDFDFD')
botao2.grid(row=0, column=1)

botao3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda:botao_apertado(3), bg='#484848', fg='#FDFDFD')
botao3.grid(row=0, column=2)

botao4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda:botao_apertado(4), bg='#484848', fg='#FDFDFD')
botao4.grid(row=1, column=0)

botao5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda:botao_apertado(5), bg='#484848', fg='#FDFDFD')
botao5.grid(row=1, column=1)

botao6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda:botao_apertado(6), bg='#484848', fg='#FDFDFD')
botao6.grid(row=1, column=2)

botao7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda:botao_apertado(7), bg='#484848', fg='#FDFDFD')
botao7.grid(row=2, column=0)

botao8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda:botao_apertado(8), bg='#484848', fg='#FDFDFD')
botao8.grid(row=2, column=1)

botao9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda:botao_apertado(9), bg='#484848', fg='#FDFDFD')
botao9.grid(row=2, column=2)

botao0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda:botao_apertado(0), bg='#484848', fg='#FDFDFD')
botao0.grid(row=3, column=0)

mais = Button(frame, text='+', height=4, width=9, font=35, command=lambda:botao_apertado('+'), bg='#DC8C00', fg='#FDFDFD')
mais.grid(row=0, column=3)

menos = Button(frame, text='-', height=4, width=9, font=35, command=lambda:botao_apertado('-'), bg='#DC8C00', fg='#FDFDFD')
menos.grid(row=1, column=3)

multiplicacao = Button(frame, text='*', height=4, width=9, font=35, command=lambda:botao_apertado('*'), bg='#DC8C00', fg='#FDFDFD')
multiplicacao.grid(row=2, column=3)

divisao = Button(frame, text='/', height=4, width=9, font=35, command=lambda:botao_apertado('/'), bg='#DC8C00', fg='#FDFDFD')
divisao.grid(row=3, column=3)

apagar = Button(frame, text='C', height=4, width=9, font=35, command=limpar, bg='#484848', fg='#FDFDFD',)
apagar.grid(row=4, column=3)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda:botao_apertado('.'), bg='#484848', fg='#FDFDFD')
decimal.grid(row=3, column=1)

barra_esquerda = Button(frame, text='(', height=4, width=9, font=35, command=lambda:botao_apertado('('), bg='#131313', fg='#FDFDFD')
barra_esquerda.grid(row=4, column=0)

barra_direita = Button(frame, text=')', height=4, width=9, font=35, command=lambda:botao_apertado(')'), bg='#131313', fg='#FDFDFD')
barra_direita.grid(row=4, column=1)

elevado = Button(frame, text='^', height=4, width=9, font=35, command=lambda:botao_apertado('**'), bg='#484848', fg='#FDFDFD')
elevado.grid(row=3, column=2)

igual = Button(frame, text='=', height=4, width=9, font=35, command=igual, bg='#DC8C00', fg='#FDFDFD')
igual.grid(row=4, column=2)

janela.mainloop()
