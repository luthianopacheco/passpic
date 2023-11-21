import os
from tkinter import messagebox
import awesometkinter as atk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from  datetime import date

from controller.Controller import *
from util.CadastroUtils import *

global tree
def consulta():
    try:
        # config janela
        interface = tk.Tk()
        interface.resizable(width=False, height=False)
        interface.title("PassPic - Remover Cadastro ")
        interface.wm_iconbitmap('images/passpic.ico')
        interface.geometry("1000x600")
        interface.configure(background="gray")

        #Frame grande de cima
        first_frame = tk.Frame(interface, width=1000, height=420, background='lightgrey', relief='flat')
        first_frame.grid(row=0, column= 0, padx=0, pady=1)
        
        #Topo do primeiro frame
        top_frame = tk.Frame(first_frame, width=1000, height=60, background='lightgrey', relief='flat')
        top_frame.grid(row=0, column= 0)
        main_label = tk.Label(top_frame, text="Cadastros", font=('Ivy 22 bold'), bg='lightgray', fg='black')
        main_label.place(x=420, y=10)

        #Meio do primeiro frame
        middle_frame = tk.Frame(first_frame, width=1000, height=350, background='white', relief='flat')
        middle_frame.grid(row=1, column= 0)

# ---------------------------------------------------- ↓↓↓ TABELA ↓↓↓ ---------------------------------------------------- #
        
        def table():
            global tree
            # Cabeçalho
            columns = ['ID', 'Nome', 'CPF', 'Data de Nascimento', 'Celular']

            # Linhas
            rows = getDataToTable()
            
            # Tabela
            tree = ttk.Treeview(middle_frame, selectmode='extended', columns=columns, show='headings')

            # Scrolls
            vertical_scroll = ttk.Scrollbar(middle_frame, orient=VERTICAL, command=tree.yview)
            # vertical_scroll.pack(side='right', fill='y')
            horizontal_scroll = ttk.Scrollbar(middle_frame, orient=HORIZONTAL, command=tree.xview)
            # horizontal_scroll.pack(side=BOTTOM, fill='y')
            
            tree.configure(yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)

            # Grid
            tree.grid(column=0, row=0, sticky='NSEW')
            vertical_scroll.grid(column=1, row=0, columnspan=2, sticky='NS')
            horizontal_scroll.grid(column=0, row=1, sticky='EW')
            middle_frame.grid_rowconfigure(0, weight=12)

            # Identação do cabeçalho e largura de cada coluna
            hd=['center', 'nw', 'center', 'center', 'center']
            h=[50, 280, 130, 130, 130]
            n=0

            # Setando as colunas/cabeçalho na tabela
            for col in columns:
                tree.heading(col, text=col.title(), anchor=CENTER)
                tree.column(col, width=h[n], anchor=hd[n], stretch=False)
                n+=1

            # Setando as linhas/valores na tabela
            for item in rows:
                tree.insert('','end', values=item)

        table()

# ------------------------------------------ ↓↓↓ BOTÕES E FUNCIONALIDADES ↓↓↓ --------------------------------------------- #

        def editar():
            if not tree.focus():
                messagebox.showwarning(title='Erro', message='Você deve selecionar uma linha para editar!')
            else:
                cancel()
                atualizar_cadastro_button.configure(state='normal', cursor="hand2")
                cancelar_button.configure(state='normal', cursor="hand2")
                nome_entry.configure(state='normal')
                cpf_entry.configure(state='normal')
                nascimento_cal.configure(state='normal')
                cep_entry.configure(state='normal')
                logradouro_entry.configure(state='normal')
                num_entry.configure(state='normal')
                complemento_entry.configure(state='normal')
                bairro_entry.configure(state='normal')
                cidade_entry.configure(state='normal')
                UF_entry.configure(state='normal')
                pais_entry.configure(state='normal')
                celular_entry.configure(state='normal')

                # Pegando o ID do item selecionado na tabela
                linha = tree.focus()
                item = tree.item(linha)
                dados = item["values"]
                id = dados[0]
                
                # Buscando os dados do banco de dados passando o id
                user_data, endereco_data = getDataById(id)
                
                # Buscando a imagem pelo diretório
                # image_data:str = user_data[0][5]
                # img = tk.PhotoImage(file= image_data.replace("''","'"))
                # print(image_data)

                # Convertendo a data com o formato do banco de dados para o BR
                nasc = str(user_data[0][3])            
                nascimento = dateConvert(date=nasc)

                # Inserindo as informações nos campos
                nome_entry.insert(0, user_data[0][1])
                cpf_entry.insert(0, user_data[0][2])
                nascimento_cal.insert(0, nascimento)
                celular_entry.insert(0, user_data[0][4])
                cep_entry.insert(0, endereco_data[0][1])
                logradouro_entry.insert(0, endereco_data[0][2])
                num_entry.insert(0, endereco_data[0][3])
                complemento_entry.insert(0, endereco_data[0][4])
                bairro_entry.insert(0, endereco_data[0][5])
                cidade_entry.insert(0, endereco_data[0][6])
                UF_entry.insert(0, endereco_data[0][7])
                pais_entry.insert(0, endereco_data[0][8])
                

                id_entry.configure(state="normal")
                id_entry.delete(0, END)
                id_entry.insert(0, user_data[0][0])
                id_entry.configure(state="disabled")


        def deletar():
            if not tree.focus():
                messagebox.showwarning(title='Erro', message='Você deve selecionar uma linha para deletar!')
            else:
                linha = tree.focus()
                item = tree.item(linha)
                dados = item["values"]
                id = dados[0]
                nome = dados[1]

                # Pega o diretório da imagem salva no banco de dados
                user, endereco = getDataById(id=id)
                image_path = str(user[0][5])
                path = image_path.replace('/','\\')

                # Mostra uma caixa de mensagem para confirmar a exclusão
                delete = messagebox.askokcancel(title='Deletar cadastro', message=f'Tem certeza que deseja deletar "{nome}"?')
                if delete:
                    deleteData(id=id)
                    os.remove(image_path)
                    table()
            

        def atualizarCadastro():
            table()
            messagebox.showinfo(title='Atualizar Cadastro!', message='Cadastro atualizado com sucesso!')
                

        
        #Base do primeiro frame
        bottom_frame = tk.Frame(first_frame, width=1000, height=60, background='lightgrey', relief='flat')
        bottom_frame.grid(row=2, column= 0)
        consult_edit_btn = atk.Button3d(bottom_frame, text='Consultar / Editar', bg='lightgray', fg='black',
                                        cursor='hand2', command=editar, width=16)
        consult_edit_btn.place(x=250, y=20)
        atualizar_tabela_btn = atk.Button3d(bottom_frame, text='Atualizar tabela', bg='lightgray', fg='black',
                                  cursor='hand2', command=table, width=16)
        atualizar_tabela_btn.place(x=450, y=20)
        delete_btn = atk.Button3d(bottom_frame, text='Deletar', bg='lightgray', fg='black',
                                  cursor='hand2', command=deletar, width=16)
        delete_btn.place(x=650, y=20)


        
# ---------------------------------------------- ↑↑↑↑ FRAME DE CIMA ↑↑↑↑ ----------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------↓↓↓ FRAME DE BAIXO ↓↓↓------------------------------------------------------ #



        #Frame grande de baixo
        second_frame = tk.Frame(interface, width=1000, height=260, background='lightgray', relief='flat')
        second_frame.grid(row=1, column= 0, padx=0, pady=1)
        second_frame.place(x=0, y=365)
        

        def save():
            # Apaga os dados e desabilita os campos
            # Atualiza o banco de dados
            updateData(id=id_entry.get(), nome=nome_entry.get(), cpf=cpf_entry.get(), data_nascimento=dateConvert(date=nascimento_cal.get()),
                       celular=celular_entry.get(), cep=cep_entry.get(), logradouro=logradouro_entry.get(), numero=num_entry.get(), 
                       complemento=complemento_entry.get(), bairro=bairro_entry.get(), cidade=cidade_entry.get(), uf=UF_entry.get(), 
                       pais=pais_entry.get())
            print(f'{id_entry.get()}\n{nome_entry.get()}\n{cpf_entry.get()}\n{dateConvert(date=nascimento_cal.get())},\n{celular_entry.get()}\n{cep_entry.get()}\n{logradouro_entry.get()}\n{num_entry.get()},\n{complemento_entry.get()}\n{bairro_entry.get()}\n{cidade_entry.get()}\n{UF_entry.get()},\n{pais_entry.get()}')
            cancel()
            # atualiza a tabela
            atualizarCadastro()


        def cancel():
            # Apaga os dados dos campos
            nome_entry.delete(first=0, last=END)
            cpf_entry.delete(first=0, last=END)
            nascimento_cal.delete(first=0, last=END)
            cep_entry.delete(first=0, last=END)
            logradouro_entry.delete(first=0, last=END)
            num_entry.delete(first=0, last=END)
            complemento_entry.delete(first=0, last=END)
            bairro_entry.delete(first=0, last=END)
            cidade_entry.delete(first=0, last=END)
            UF_entry.delete(first=0, last=END)
            pais_entry.delete(first=0, last=END)
            celular_entry.delete(first=0, last=END)
            id_entry.configure(state="normal")
            id_entry.delete(first=0, last=END)
            id_entry.configure(state="disabled")
            
            # Desabilita os campos e botões
            nome_entry.configure(state='disabled')
            cpf_entry.configure(state='disabled')
            nascimento_cal.configure(state='disabled')
            cep_entry.configure(state='disabled')
            logradouro_entry.configure(state='disabled')
            num_entry.configure(state='disabled')
            complemento_entry.configure(state='disabled')
            bairro_entry.configure(state='disabled')
            cidade_entry.configure(state='disabled')
            UF_entry.configure(state='disabled')
            pais_entry.configure(state='disabled')
            celular_entry.configure(state='disabled')
            atualizar_cadastro_button.configure(state='disabled', cursor="arrow")
            cancelar_button.configure(state='disabled', cursor="arrow")

            

        # Valida os campos
        def check():
            checkFields(nome=nome_entry.get(), interface=second_frame, cep=cep_entry.get(), cpf=cpf_entry.get(), 
                        nascimento=nascimento_cal.get(), celular=celular_entry.get(), save=save)


# ---------------------------------------------------- ↓↓↓ COMPONENTES ↓↓↓ ---------------------------------------------------- #

        #Criação de componentes e posicionamento na tela
        # Nome
        nome_label = tk.Label(second_frame, text="* Nome:", font=("Arial", 10, "bold"), bg="lightgrey")
        nome_entry = tk.Entry(second_frame, width=55)
        nome_label.place(x=15, y=15)
        nome_entry.place(x=15, y=37)

        # CPF
        cpf_label = tk.Label(second_frame, text="* CPF:", font=("Arial", 10, "bold"), bg="lightgrey")
        cpf_entry = tk.Entry(second_frame, width=20)
        cpf_label.place(x=380, y=15)
        cpf_entry.place(x=380, y=37)

        # Data de Nascimento
        nascimento_label = tk.Label(second_frame, text="Data Nascimento:", font=("Arial", 10, "bold"),
                                    bg="lightgrey")
        nascimento_cal = DateEntry(second_frame, width=20, background='darkblue', foreground='white', 
                                 borderwidth=2, year=2023, locale='pt_BR', date_pattern='dd/MM/yyyy',
                                 mindate=date(1900,1,1), maxdate=date.today())
        nascimento_label.place(x=540, y=15)
        nascimento_cal.place(x=540, y=37)
        
        # CEP
        cep_label = tk.Label(second_frame, text="CEP:", font=("Arial", 10, "bold"), bg="lightgrey")
        cep_entry = tk.Entry(second_frame, width=15)
        cep_label.place(x=15,y=70)
        cep_entry.place(x=15, y=92)

        # Logradouro - nome da rua
        logradouro_label = tk.Label(second_frame, text="Logradouro:", font=("Arial", 10, "bold"), bg="lightgrey")
        logradouro_entry = tk.Entry(second_frame, width=55)
        logradouro_label.place(x=145, y=70)
        logradouro_entry.place(x=145, y=92)

        # Número da casa
        num_label = tk.Label(second_frame, text="Nº:", font=("Arial", 10, "bold"), bg="lightgrey")
        num_entry = tk.Entry(second_frame, width=8)
        num_label.place(x=515, y=70)
        num_entry.place(x=515, y=92)

        # Complemento
        complemento_label = tk.Label(second_frame, text="Complemento:", font=("Arial", 10, "bold"), bg="lightgrey")
        complemento_entry = tk.Entry(second_frame, width=21)
        complemento_label.place(x=600, y=70)
        complemento_entry.place(x=600, y=92)

        # Bairro
        bairro_label = tk.Label(second_frame, text="Bairro:", font=("Arial", 10, "bold"), bg="lightgrey")
        bairro_entry = tk.Entry(second_frame, width=30)
        bairro_label.place (x= 15, y=125)
        bairro_entry.place(x=15, y=147)

        # Cidade
        cidade_label = tk.Label(second_frame, text="Cidade:", font=("Arial", 10, "bold"), bg="lightgrey")
        cidade_entry = tk.Entry(second_frame, width=30)
        cidade_label.place(x=235, y=125)
        cidade_entry.place(x=235, y=147)

        # UF - Estado
        UF_label = tk.Label(second_frame, text="UF:", font=("Arial", 10, "bold"), bg="lightgrey")
        UF_entry = tk.Entry(second_frame,insertwidth=2, width=8)
        UF_label.place(x=450, y=125)
        UF_entry.place(x=450, y=147)

        # País
        pais_label = tk.Label(second_frame, text="País:", font=("Arial", 10, "bold"), bg="lightgrey")
        pais_entry = tk.Entry(second_frame, width=8)
        pais_label.place(x=535, y=125)
        pais_entry.place(x=535, y=147)

        # Celular
        celular_label = tk.Label(second_frame, text="Celular:", font=("Arial", 10, "bold"), bg="lightgrey")
        celular_entry = tk.Entry(second_frame, width=18)
        celular_label.place(x=619, y=125)
        celular_entry.place(x=619, y=147)

        # ID do usuário
        id_label = tk.Label(second_frame, text="ID:", font=("Arial", 10, "bold"), bg="lightgrey")
        id_entry = tk.Entry(second_frame, width=8)
        id_entry.configure(state="disabled")
        id_label.place(x= 15, y= 178)
        id_entry.place(x= 15, y= 200)

        # Botão de Cancelar
        cancelar_button = atk.Button3d(second_frame, text="Cancelar", bg="lightgrey", fg="black", cursor="hand2",
                                       command=cancel)
        cancelar_button.place(x=540, y=200)
                
        # Botão de Atualizar cadastro
        atualizar_cadastro_button = atk.Button3d(second_frame, text="Atualizar", bg="lightgray", fg="black",
                                    command=check)
        # atualizar_cadastro_button.configure(state='disabled')
        atualizar_cadastro_button.place(x=650, y=200)

        

        

        cancel()


# ---------------------------------------------------- ↑↑↑ COMPONENTES ↑↑↑ ---------------------------------------------------- #
        
        
        
    except Exception as e:
        print(e)