import cv2
import tkinter as tk
import threading
from tkinter import messagebox
import pygetwindow as gw
from ScreenCapture import *

WINDOW_NAME = "Escolha a janela a ser capturada"

# Função para capturar a tela da janela selecionada
def capture_screen(window_name):
    screenshot = None
    while True:
        key = cv2.waitKey(1)
        if key == ord('q'):  # Pressione 'q' para encerrar a captura
            break

        screenshot = capture_win_alt(window_name)
        cv2.imshow('Computer Vision', screenshot)  # Mostra em tela cheia a tela capturada

    cv2.destroyAllWindows()  # Fecha a janela do OpenCV após encerrar a captura

# Função para iniciar a captura em uma thread separada
def start_capture(window_name):
    capture_thread = threading.Thread(target=capture_screen, args=(window_name,))
    capture_thread.start()

# Função para selecionar a janela
def select_window():
    selected_window = window_dropdown.get()  # Obtém o valor selecionado no dropdown
    if selected_window:
        start_capture(selected_window)
    else:
        messagebox.showerror("Erro", "Nenhuma janela selecionada!")

# Criação da janela principal
window = tk.Tk()
window.title("Seleção de Janela")
window.geometry("300x100")

# Label e dropdown para selecionar a janela
window_label = tk.Label(window, text="Selecione a janela:")
window_label.pack()

window_dropdown = tk.StringVar()
window_dropdown.set(WINDOW_NAME)  # Valor padrão
window_menu = tk.OptionMenu(window, window_dropdown, *gw.getAllTitles())
window_menu.pack()

# Botão para capturar a tela da janela selecionada
capture_button = tk.Button(window, text="Capturar", command=select_window)
capture_button.pack()

# Função para fechar a janela
def close_window():
    window.destroy()

# Loop principal da interface gráfica
window.mainloop()
