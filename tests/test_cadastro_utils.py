from util.cadastro_utils import *

# ------------------------------------ dateRegEx ----------------------------------------- #

# data padrão BR separado por '/' - TRUE
def test_date_regex_true():
    assert dateRegex(date= "27/04/1994") == True

# data padrão BR separado por '-' - FALSE
def test_date_regex_false_1():
    assert dateRegex(date= "27-04-1994") == False

# data padrão BR separado por '.' - FALSE
def test_date_regex_false_2():
    assert dateRegex(date= "27.04.1994") == False

# data sem separador - FALSE    
def test_date_regex_false_3():
    assert dateRegex(date= "27041994") == False

# data com formato dd/MM/aa - FALSE    
def test_date_regex_false_4():
    assert dateRegex(date= "27/04/94") == False


# ------------------------------------ cepRegEx ----------------------------------------- #

# cep padrão br - TRUE
def test_cep_regex_true():
    assert cepRegex('91010-000') == True

# cep padrão br com '.' - False
def test_cep_regex_false_1():
    assert cepRegex('91.010-000') == False

# cep padrão br separado por '.' - False
def test_cep_regex_false_2():
    assert cepRegex('91010.000') == False

# cep padrão br sem separação - False
def test_cep_regex_false_3():
    assert cepRegex('91010000') == False

# cep com quantidade de digitos errado - False
def test_cep_regex_false_4():
    assert cepRegex('91010-00') == False


# ------------------------------------ dateConvert ----------------------------------------- #

# converte formato do banco de dados (aaaa-mm-dd) para formato BR (dd-mm-aaaa)
def test_date_convert_true_1():
    assert dateConvert('1994-04-27') == '27/04/1994'

# converte formato do banco de dados (aaaa-mm-dd) para formato BR (dd-mm-aaaa)
def test_date_convert_true_2():
    assert dateConvert('1994/04/27') == '27-04-1994'

# converte formato BR (dd-mm-aaaa) para formato do banco de dados (aaaa-mm-dd)
def test_date_convert_true_3():
    assert dateConvert('27/04/1994') == '1994-04-27'

# converte formato BR (dd-mm-aaaa) para formato do banco de dados (aaaa-mm-dd)
def test_date_convert_true_4():
    assert dateConvert('27-04-1994') == '1994/04/27'

# Passando formato errado, deve retornar vazio ''
def test_date_convert_true_4():
    assert dateConvert('27041994') == ''