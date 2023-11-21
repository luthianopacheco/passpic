import os
import cv2
import tkinter as tk
import awesometkinter as atk
from tkinter import *
from tkcalendar import DateEntry
from datetime import date

from controller.Controller import insertData
from util.CadastroUtils import *

# Tela de inserção de dados - Cadastro 
def register():
    try:
        # config janela
        register_interface = tk.Tk()
        register_interface.resizable(width=False, height=False)
        register_interface.title("PassPic - Cadastro")
        register_interface.wm_iconbitmap('images/passpic.ico')
        register_interface.geometry("770x250")
        register_interface.configure(background="lightgrey")

        # Abre a câmera passando os dados e fecha a janela
        def save():
            new_image(name=nome_entry.get(), cpf=cpf_entry.get(), data_nascimento=dateConvert(date=nascimento_cal.get()), 
                      celular=celular_entry.get(), cep=cep_entry.get(), logradouro=logradouro_entry.get(), numero=num_entry.get(),
                      complemento=complemento_entry.get(), bairro=bairro_entry.get(), cidade=cidade_entry.get(), uf=UF_entry.get(),
                      pais=pais_entry.get(), interface=register_interface)

        # Fecha a janela
        def cancel():
            register_interface.destroy()

        # Faz a validação dos campos
        def check():
            checkFields(nome=nome_entry.get(), interface=register_interface, cep=cep_entry.get(), cpf=cpf_entry.get(),
                        nascimento=nascimento_cal.get(), celular=celular_entry.get(), save=save)
        
# ---------------------------------------------------- ↓↓↓ COMPONENTES ↓↓↓ ---------------------------------------------------- #
        
        #Criação de componentes e posicionamento na tela
        # Nome
        nome_label = tk.Label(register_interface, text="* Nome:", font=("Arial", 10, "bold"), bg="lightgrey")
        nome_entry = tk.Entry(register_interface, width=55)
        nome_entry.focus()
        nome_label.place(x=15, y=15)
        nome_entry.place(x=15, y=37)

        # CPF
        cpf_label = tk.Label(register_interface, text="* CPF:", font=("Arial", 10, "bold"), bg="lightgrey")
        cpf_entry = tk.Entry(register_interface, width=20)
        cpf_label.place(x=380, y=15)
        cpf_entry.place(x=380, y=37)

        # Data de Nascimento
        nascimento_label = tk.Label(register_interface, text="Data Nascimento:", font=("Arial", 10, "bold"),
                                    bg="lightgrey")
        nascimento_cal = DateEntry(register_interface, width=20, background='darkblue', foreground='white', 
                                 borderwidth=2, locale='pt_BR', date_pattern='dd/MM/yyyy',
                                 mindate=date(1900,1,1), maxdate=date.today())
        nascimento_cal.delete(0, END)
        nascimento_cal.insert(0, '01/01/2000')
        nascimento_label.place(x=540, y=15)
        nascimento_cal.place(x=540, y=37)
        
        # CEP
        cep_label = tk.Label(register_interface, text="CEP:", font=("Arial", 10, "bold"), bg="lightgrey")
        cep_entry = tk.Entry(register_interface, width=15)
        cep_label.place(x=15,y=70)
        cep_entry.place(x=15, y=92)

        # Logradouro - nome da rua
        logradouro_label = tk.Label(register_interface, text="Logradouro:", font=("Arial", 10, "bold"), bg="lightgrey")
        logradouro_entry = tk.Entry(register_interface, width=55)
        logradouro_label.place(x=145, y=70)
        logradouro_entry.place(x=145, y=92)

        # Número da casa
        num_label = tk.Label(register_interface, text="Nº:", font=("Arial", 10, "bold"), bg="lightgrey")
        num_entry = tk.Entry(register_interface, width=8)
        num_label.place(x=515, y=70)
        num_entry.place(x=515, y=92)

        # Complemento
        complemento_label = tk.Label(register_interface, text="Complemento:", font=("Arial", 10, "bold"), bg="lightgrey")
        complemento_entry = tk.Entry(register_interface, width=21)
        complemento_label.place(x=600, y=70)
        complemento_entry.place(x=600, y=92)

        # Bairro
        bairro_label = tk.Label(register_interface, text="Bairro:", font=("Arial", 10, "bold"), bg="lightgrey")
        bairro_entry = tk.Entry(register_interface, width=30)
        bairro_label.place (x= 15, y=125)
        bairro_entry.place(x=15, y=147)

        # Cidade
        cidade_label = tk.Label(register_interface, text="Cidade:", font=("Arial", 10, "bold"), bg="lightgrey")
        cidade_entry = tk.Entry(register_interface, width=30)
        cidade_label.place(x=235, y=125)
        cidade_entry.place(x=235, y=147)

        # UF - Estado
        UF_label = tk.Label(register_interface, text="UF:", font=("Arial", 10, "bold"), bg="lightgrey")
        UF_entry = tk.Entry(register_interface,insertwidth=2, width=8)
        UF_label.place(x=450, y=125)
        UF_entry.place(x=450, y=147)

        # País
        pais_label = tk.Label(register_interface, text="País:", font=("Arial", 10, "bold"), bg="lightgrey")
        pais_entry = tk.Entry(register_interface, width=8)
        pais_label.place(x=535, y=125)
        pais_entry.place(x=535, y=147)

        # Celular
        celular_label = tk.Label(register_interface, text="Celular:", font=("Arial", 10, "bold"), bg="lightgrey")
        celular_entry = tk.Entry(register_interface, width=18)
        celular_label.place(x=619, y=125)
        celular_entry.place(x=619, y=147)

        # Botão de Cancelar
        cancelar_button = atk.Button3d(register_interface, text="Cancelar", bg="lightgrey", fg="black", cursor="hand2",
                                       command=cancel)
        cancelar_button.place(x=540, y=200)
                
        # Botão de Confirmar/Capturar imagem
        atualizar_cadastro_button = atk.Button3d(register_interface, text="Capturar imagem", bg="lightgray", fg="black", cursor="hand2",
                                    command=check)
        atualizar_cadastro_button.place(x=650, y=200)

# ---------------------------------------------------- ↑↑↑ COMPONENTES ↑↑↑ ---------------------------------------------------- #

        # Loop da janela
        register_interface.mainloop()

    # Caso ocorra algum erro, exibe uma mensagem de erro
    except Exception as e:
        def close():
            error.destroy()
            exit()

        print("Ocorreu um erro 'code-2'\n"+str(e))
        register_interface.destroy()
        error = tk.Tk()
        error.resizable(width=False, height=False)
        error.title("Erro código 2")
        error.wm_iconbitmap('images/passpic.ico')
        error.geometry("520x240")
        error.configure(background="red")

        error_label = tk.Label(error, text="Erro cod 2: Janela de Cadastro", font=(
            "Arial", 24), bg="red", fg="black")
        button = atk.Button3d(error, text="OK", bg="red", fg="red", cursor="hand2", command=close)
        tip_label = tk.Label(error, text="Erro em criar a Janela de Cadastro", font=(
            "Arial", 12), bg="red", fg="black")
        tip2_label = tk.Label(error, text=e, font=(
            "Arial", 12), bg="red", fg="black")
        report_problem_label = tk.Label(error, text="Reportar problema: teste@teste.com", font=(
            "Arial", 10), bg="red", fg="black")

        error_label.place(x=40, y=20)
        tip_label.place(x=130, y=70)
        tip2_label.place(x=150, y=100)
        button.place(x=220, y=145)
        report_problem_label.place(x=290, y=210)

        error.mainloop()


# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------------------------------------------#

# Tela de captura de imagem - Cadastro

def new_image(name:str, cpf:str, data_nascimento:str, celular:str, 
            cep:str, logradouro:str, numero:str, complemento:str, 
            bairro:str, cidade:str, uf:str, pais:str, interface:tk.Tk):
    try:
        # Define o nome da pasta onde as fotos serão salvas
        folder_name = "Fotos Data 'PassPic'"

        # Define o caminho completo da pasta na área de trabalho
        desktop_path = os.path.join(os.path.join(
            os.path.expanduser('~')), 'Desktop')
        folder_path = os.path.join(desktop_path, folder_name)

        # Verifica se a pasta já existe, caso contrário, cria a pasta
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Captura a imagem da câmera
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Aguarda o usuário apertar qualquer tecla para tirar a sua foto
        while True:
            ret, frame = cap.read()
            cv2.imshow("PassPic - Capturar Foto - 'Aperte Qualquer Tecla Para Capturar Imagem'", frame)
            if cv2.waitKey(1) != -1:
                break

        file_path = os.path.join(folder_path,name)

        

        
        # Verifica se o nome do arquivo já existe e acrescenta um número ao final se for true
        if os.path.isfile(file_path+'.jpg'):
            for i in range(1,11):
                if os.path.isfile(file_path+'.jpg'):
                    file_path = file_path+' ('+str(i)+')'+'.jpg'
                    name = name+' ('+str(i)+')'
        else:
            file_path = file_path+'.jpg'

        # Salva a imagem capturada na pasta criada
        cv2.imwrite(file_path, frame)

        # Salva no banco de dados
        insertData(nome=name, cpf=cpf, data_nascimento=data_nascimento, celular=celular, 
                       user_image=file_path.replace('\\','/'), cep=cep, logradouro=logradouro, numero=numero, 
                       complemento=complemento, bairro=bairro, cidade=cidade, uf=uf, pais=pais)


        # Tela de informação do nome salvo - Cadastro
        def nameinfo(message:str):
            def close():
                name_info.destroy()
                

            cap.release()
            cv2.destroyAllWindows()
            interface.destroy()
            name_info = tk.Tk()
            name_info.resizable(width=False, height=False)
            name_info.title("PassPic - Cadastro")
            name_info.wm_iconbitmap('images/passpic.ico')
            name_info.geometry("450x120")
            name_info.configure(background="lightgray")

            nameinfo_label = tk.Label(name_info, text=message,
                                      font=("Arial", 12, 'bold'), bg="lightgrey", fg="black")
            nameinfo_button = atk.Button3d(name_info, text="OK", bg="black", fg="white", cursor="hand2", command=close)

            nameinfo_label.place(x=12, y=30)
            nameinfo_button.place(x=350, y=80)
            name_info.mainloop()

        if os.path.isfile(file_path):
            nameinfo(str(name)+" cadastrado com sucesso!")
        else:
            nameinfo('Não foi possível efetuar o cadastro, tente novamente!')
            

    # Caso ocorra algum erro, exibe uma mensagem de erro
    except Exception as e:
        def close():
            error.destroy()
            exit()
            

        print("Ocorreu um erro 'code-3'" + str(e))
        error = tk.Tk()
        error.resizable(width=False, height=False)
        error.title("Erro código 3")
        error.wm_iconbitmap('images/passpic.ico')
        error.geometry("520x240")
        error.configure(background="red")

        error_label = tk.Label(error, text="Erro cod 3: Janela de Escanear", font=(
            "Arial", 24), bg="red", fg="black")
        button = atk.Button3d(error, text="OK", bg="red", fg="red", cursor="hand2", command=close)
        tip_label = tk.Label(error, text="Erro ao escanear", font=(
            "Arial", 12), bg="red", fg="black")
        tip2_label = tk.Label(error, text=e, font=(
            "Arial", 12), bg="red", fg="black")
        report_problem_label = tk.Label(error, text="Reportar problema: teste@teste.com", font=(
            "Arial", 10), bg="red", fg="black")

        error_label.place(x=35, y=20)
        tip_label.place(x=195, y=70)
        tip2_label.place(x=15, y=100)
        button.place(x=220, y=145)
        report_problem_label.place(x=290, y=210)
        error.mainloop()