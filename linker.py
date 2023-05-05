from tkinter import *
import subprocess
import os

def aplicar(janela, text):
    subprocess.call("./linker.sh")

    if (os.path.exists("sucesso.txt")):
        lb4 = Label(janela, text=text)
        lb4.grid(row=5, column=0)

        # Adiciona a cor verde ao texto
        lb4.config(fg="green")        

def main ():
    # Cria os arquivos contendo os nomes dos pendrives
    os.system("./lista_pendrives.sh")

    janela = Tk()
    janela.title("Linker v1.0")

    # Remove o botão de maximizar a janela
    janela.resizable(width=False, height=False)

    # Configura a janela para iniciar no centro da tela
    janela.update_idletasks()
    width = janela.winfo_width()
    height = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (width // 2)
    y = (janela.winfo_screenheight() // 2) - (height // 2)
    janela.geometry('{}x{}+{}+{}'.format(width, height, x-100, y))

    # Carrega os nomes de pendrive do arquivo "pendrives_media.txt" e "pendrives_mnt.txt" e armazena em uma lista
    pendrives = []
    with open("pendrives_media.txt", "r") as f:
        for line in f:
            pendrives.append(line.strip())

    with open("pendrives_mnt.txt", "r") as f:
        for line in f:
            pendrives.append(line.strip())
    
    # Verifica se algum elemento da lista está vazio e remove
    pendrives = list(filter(None, pendrives))

    # Define o tamanho da janela
    janela.geometry("460x150")

    # Cria um texto de introdução
    lb0 = Label(janela, text="Bem vindo ao Linker v1.0")
    lb0.grid(row=0, column=0)

    # Texto para informar o usuário sobre o que faz o programa
    lb1 = Label(janela, text="Esse programa recupera suas configurações e histórico de navegação")
    lb1.grid(row=1, column=0)

    # Cria um menu de seleção
    var = StringVar(janela)
    var.set("CLIQUE AQUI E ESCOLHA SEU PENDRIVE") # default value

    menu = OptionMenu(janela, var, *pendrives)
    menu.config(bg="#a78aff", fg="black")
    menu.grid(row=2, column=0, sticky="w")

    # Cria um botão com uma imagem
    img = PhotoImage(file="refresh.png")

    # Ajusta o tamanho da imagem para 28x28
    img = img.subsample(8, 8)

    bt1 = Button(janela, text="RECARREGAR", bg="#a78aff", fg="black", image=img, compound=RIGHT)
    bt1.grid(row=2, column=0, sticky="e")

    # Ajusta o tamanho do botão
    bt1.config(width=120, height=17)

    lb3 = Label(janela, text=" ")
    lb3.grid(row=3, column=0)

    text="Configurações e histórico de navegação recuperados com sucesso!"
    
    # Cria o botão "aplicar" de cor verde
    bt2 = Button(janela, text="APLICAR", bg="green", fg="white", font="bold", command=aplicar(janela, text))
    bt2.grid(row=4, column=0, columnspan=3)
    
    # Ajusta o tamanho do botão
    bt2.config(width=43)

    janela.mainloop()
    
if __name__ == '__main__':
    main()