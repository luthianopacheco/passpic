import re
import tkinter as tk

#-------------------------------------------------------------------------------------------------------------------------#

# Regexp para data de nascimento
def dateRegex(date):
    regex = re.compile("(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)")
    if re.fullmatch(regex, date):
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------------------------#    

# Regexp para CEP
def cepRegex(cep):
    regex = re.compile("\\d{5}-\\d{3}")
    if re.fullmatch(regex, cep):
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------------------------#    

# Converte o formato de data dd/mm/aaaa para o formato do banco de dados aaaa/mm/dd e vice-versa
def dateConvert(date):
    if '-' in date:
        split = date.split(sep="-")
        data_nascimento = split[2]+'/'+split[1]+'/'+split[0]
    elif '/' in date:
        split = date.split(sep="/")
        data_nascimento = split[2]+'-'+split[1]+'-'+split[0]
    else:
        data_nascimento = ''

    return data_nascimento

#----------------------------------------------------------------------------------------------------------------------------------------------#

# Verifica os campos obrigatórios e passa para a próxima tela
def checkFields(interface:tk, nome:str, cpf:str, celular:str, nascimento:str, cep:str, save):
    if len(nome) >= 3 and len(cpf) == 11 and len(celular) == 11 and (nascimento == '' or dateRegex(nascimento)) and (cep == '' or cepRegex(cep)):
        name_blank_container = tk.Frame(interface, bg="lightgrey", width=400, height=20)  
        name_blank_container.place(x=15, y=56)
        cpf_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
        cpf_blank_container.place(x=380, y=56)
        phone_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
        phone_blank_container.place(x=619, y=166)
        cep_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
        cep_blank_container.place(x=10, y=111)

        save()
    else:
        # Validando nome
        if len(nome) < 3:
            name_required_label = tk.Label(interface, text="O nome é obrigatório e deve conter ao menos 3 caracteres!", 
                                           font=("Arial", 8), foreground="red", bg="lightgrey")
            name_required_label.place(x=15, y=56)
        else:
            name_blank_container = tk.Frame(interface, bg="lightgrey", width=400, height=20)  
            name_blank_container.place(x=15, y=56)

        # Validando CPF
        if not cpf or cpf == '':
            cpf_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)   
            cpf_required_label = tk.Label(cpf_blank_container, text="O CPF é obrigatório!", font=("Arial", 8), 
                                          foreground="red", bg="lightgrey")
            cpf_required_label.place(x=0, y=0)
            cpf_blank_container.place(x=380, y=56)
        elif len(cpf) != 11:
            cpf_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            cpf_len_label = tk.Label(cpf_blank_container, text="O CPF deve ter 11 digitos!", font=("Arial", 8), 
                                     foreground="red", bg="lightgrey")
            cpf_len_label.place(x=0, y=0)
            cpf_blank_container.place(x=380, y=56)
        else:
            cpf_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20) 
            cpf_blank_container.place(x=380, y=56)

        # Validando Celular
        if not celular or celular == '':
            phone_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            phone_required_label = tk.Label(phone_blank_container, text="O Celular é obrigatório!", font=("Arial", 8), 
                                            foreground="red", bg="lightgrey")
            phone_required_label.place(x=0, y=0)
            phone_blank_container.place(x=619, y=166)
        elif len(celular) != 11:
            phone_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            phone_required_label = tk.Label(phone_blank_container, text="O Celular deve ter 11 digitos!", font=("Arial", 8), 
                                            foreground="red", bg="lightgrey")
            phone_required_label.place(x=0, y=0)
            phone_blank_container.place(x=619, y=166)
        else:
            phone_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            phone_blank_container.place(x=619, y=166)

        # Validando data de nascimento
        if nascimento:
            if dateRegex(nascimento):
                date_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
                date_blank_container.place(x=540, y=56)
            else:
                date_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
                date_format_label = tk.Label(date_blank_container, text="O formato deve ser dd/mm/aaaa", font=("Arial", 8),
                                              foreground="red", bg="lightgrey")
                date_format_label.place(x=0, y=0)
                date_blank_container.place(x=540, y=56)
        else:
            date_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            date_blank_container.place(x=540, y=56)

        # Validando cep
        if cep:
            if cepRegex(cep):
                cep_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
                cep_blank_container.place(x=10, y=111)
            else:
                cep_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
                cep_format_label = tk.Label(cep_blank_container, text="O formato deve ser 00000-000", font=("Arial", 7), 
                                            foreground="red", bg="lightgrey")
                cep_format_label.place(x=0, y=0)
                cep_blank_container.place(x=10, y=111)
        else:
            date_blank_container = tk.Frame(interface, bg="lightgrey", width=200, height=20)
            date_blank_container.place(x=10, y=111)

#-------------------------------------------------------------------------------------------------------------------------#
    