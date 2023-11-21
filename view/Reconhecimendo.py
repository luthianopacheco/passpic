import glob
import os
import cv2
import face_recognition
import numpy as np
import tkinter as tk
import awesometkinter as atk
from pathlib import Path

class ReconhecimentoFacial:

    def reconhecer():
        try:
            # Obtém o caminho para a área de trabalho do usuário atual
            desktop_path = os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop')

            # Concatena o caminho da pasta "Fotos Data 'PassPic'" na área de trabalho
            data_folder_path = os.path.join(desktop_path, "Fotos Data 'PassPic'")

            # Cria um objeto PastaOrganizador
            sfr = ReconhecimentoFacial()

            # Carrega as imagens codificadas de faces conhecidas
            sfr.load_encoding_images(data_folder_path)

            # Resto do código é igual ao anterior
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            # Detecta as faces e as compara com as faces conhecidas
            while True:
                ret, frame = cap.read()
                face_locations, face_names = sfr.detect_known_faces(frame)

                for face_loc, name in zip(face_locations, face_names):
                    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                    cv2.putText(frame, name, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                cv2.imshow("Aperte 'ESC' para sair do modo Scanner", frame)

                # Pressione 'ESC' para sair do modo Scanner
                key = cv2.waitKey(1)

                if key == 27:
                    break

            # Fecha a janela
            cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            def close():
                error.destroy()
                exit()

            print("Ocorreu um erro 'code-7'\n"+str(e))
            error = tk.Tk()
            error.resizable(width=False, height=False)
            error.title("Erro código 7")
            error.wm_iconbitmap('images/passpic.ico')
            error.geometry("720x240")
            error.configure(background="red")

            error_label = tk.Label(error, text="Erro cod 7: Janela de Reconhecimento Facial", font=(
                "Arial", 24), bg="red", fg="black")
            button = atk.Button3d(error, text="OK", bg="red", fg="red", cursor="hand2", command=close)
            tip_label = tk.Label(error, text="Erro ao carregar janela", font=(
                "Arial", 12), bg="red", fg="black")
            tip2_label = tk.Label(error, text="Dica: Foto cadastrada com desfoque!", font=(
                "Arial", 12, "bold"), bg="red", fg="black")
            report_problem_label = tk.Label(error, text="Reportar problema: teste@teste.com", font=(
                "Arial", 10), bg="red", fg="black")

            error_label.place(x=35, y=20)
            tip_label.place(x=275, y=70)
            tip2_label.place(x=220, y=100)
            button.place(x=320, y=145)
            report_problem_label.place(x=480, y=210)
            error.mainloop()

    try:
        # Método __init__ é definido, que inicializa os atributos da classe
        def __init__(self):

            # Cria duas listas vazias para armazenar os codificações faciais conhecidas e os nomes correspondentes
            self.known_face_encodings = []
            self.known_face_names = []

            # Define o atributo frame_resizing com o valor de 0.25
            self.frame_resizing = 0.25

        # Define o método load_encoding_images, que recebe o caminho para a pasta com as imagens
        def load_encoding_images(self, images_path):

            # Usa a biblioteca glob para encontrar todas as imagens na pasta e armazená-las em uma lista
            images_path = glob.glob(os.path.join(images_path, "*.*"))

            # Imprime o número de imagens encontradas
            print("{} imagens foram encontradas.".format(len(images_path)), "\n")

            # Loop pelas imagens encontradas
            for img_path in images_path:
                # Lê a imagem usando a biblioteca cv2
                img = cv2.imread(img_path)

                # Converte a imagem de BGR para RGB
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Usa a biblioteca face_recognition para extrair as codificações faciais da imagemm
                img_encoding = face_recognition.face_encodings(rgb_img)[0]

                # Extrai o nome do arquivo da imagem e armazena-o na lista de nomes conhecidos
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)
                self.known_face_names.append(filename)

                # Armazena a codificação facial correspondente na lista de codificações conhecidas
                self.known_face_encodings.append(img_encoding)

            # Imprime os nomes das imagens encontradas
            print("Image's encontrda's: ", self.known_face_names, "\n")

        # Define o método detect_known_faces, que recebe um quadro de imagem como entrada
        def detect_known_faces(self, frame):

            # Redimensiona o quadro de imagem para um quarto do tamanho original
            small_frame = cv2.resize(
                frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

            # Converte o quadro de imagem de BGR para RGB
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # Usa a biblioteca face_recognition para localizar as faces no quadro de imagem redimensionado
            face_locations = face_recognition.face_locations(rgb_small_frame)

            # Extrai as codificações faciais correspondentes às faces encontradas
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            # Cria uma lista vazia para armazenar os nomes das faces correspondentes
            face_names = []

            # Loop pelas codificações faciais encontradas
            for face_encoding in face_encodings:

                # Compara as codificações faciais com as codificações faciais conhecidas e retorna uma lista
                # de booleanos
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, face_encoding)

                # padrão, só alterá-lo se houver uma correspondência
                name = "Nao cadastrado"

                # Se houver uma correspondência, encontra o índice da codificação facial correspondente com
                # a menor distância
                face_distances = face_recognition.face_distance(
                    self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                # Se a correspondência for encontrada, atribui o nome correspondente à face
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

                # Adiciona o nome da face à lista de nomes de faces
                face_names.append(name)

            # Converte as localizações das faces em um array numpy e divide pelo valor de redimensionamento
            face_locations = np.array(face_locations)
            face_locations = face_locations / self.frame_resizing

            # Converte as localizações das faces em inteiros e retorna tanto as localizações quanto os nomes das faces
            return face_locations.astype(int), face_names
    except Exception as e:
        print('Erro Reconhecimento\n'+str(e))
        pass