import tkinter as tk
import awesometkinter as atk

from view.Cadastro import register
from view.Consulta import consulta
from view.Reconhecimendo import ReconhecimentoFacial


# Janela principal
def main():
    try:
        # Cria a janela
        main_interface = tk.Tk()

        # Bloqueia o redimensionamento da janela
        main_interface.resizable(width=False, height=False)

        # Define o título na barra superior da janela
        main_interface.title("PassPic")

        # Define o icone da barra superior da janela
        main_interface.wm_iconbitmap('images/passpic.ico')

        # Define o tamanho da janela
        main_interface.geometry("1100x720")

        # Define a cor de fundo da janela
        main_interface.configure(background="lightgrey")

        # Armazenando e manipulando o logo em uma variável
        logo = tk.PhotoImage(file="images/passpic.png")
        logo = logo.subsample(1, 1)

        # Cria os componentes da main_interface
        txt_welcome = tk.Label(main_interface, text="Bem-vindo ao PassPic!", font=(
            "Arial", 22, "bold"), bg="lightgray", fg="black")
        
        main_image_logo = tk.Label(image=logo, bg='lightgray')

        register_button = atk.Button3d(main_interface, text="Cadastrar", bg="lightgrey", fg="black", cursor="hand2",
                                       command=register, width=16)
        delete_button = atk.Button3d(main_interface, text="Consultar", bg="lightgrey", fg='black', cursor="hand2",
                                     command=consulta, width=16)
        scan_button = atk.Button3d(main_interface, text="Escanear", bg="lightgrey", fg="black", cursor="hand2",
                                   command=ReconhecimentoFacial.reconhecer, width=16)
        dev_label = tk.Label(main_interface, text="Desenvolvido por: Anelle Arias e Luthiano Pacheco", font=(
            "arial", 8, "bold"), bg="lightgray", fg="black", cursor="hand2")

        # Posiciona os componentes na main_interface
        txt_welcome.place(x=400, y=50)
        main_image_logo.place(x=390, y=120)
        register_button.place(x=380, y=500)
        delete_button.place(x=502, y=580)
        scan_button.place(x=620, y=500)
        dev_label.place(x=780, y=680)

        # Loop da main_interface
        main_interface.mainloop()

    # Caso ocorra algum erro, exibe uma mensagem de erro
    except Exception as e:
        def close():
            error.destroy()
            exit()


        print("Ocorreu um erro 'code-1'\n"+str(e))
        error = tk.Tk()
        error.resizable(width=False, height=False)
        error.title("Erro código 1")
        error.wm_iconbitmap('images/passpic.ico')
        error.geometry("480x200")
        error.configure(background="red")

        error_label = tk.Label(error, text="Erro cod 1: Janela Principal ", font=(
            "Arial", 24), bg="red", fg="black")
        button = atk.Button3d(error, text="OK", bg="red", fg="red", cursor="hand2", command=close)
        tip_label = tk.Label(error, text=f"Erro em criar a Janela Principal\n{e}", font=(
            "Arial", 12), bg="red", fg="black")
        report_problem_label = tk.Label(error, text="Reportar problema: teste@teste.com", font=("Arial", 10), bg="red",
                                        fg="black")

        error_label.place(x=40, y=20)
        tip_label.place(x=140, y=70)
        button.place(x=210, y=120)
        report_problem_label.place(x=260, y=170)
        error.mainloop()

main()
