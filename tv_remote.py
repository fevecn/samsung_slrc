import tkinter as tk
from tkinter import ttk
import samsungctl

# samsungctl config
config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.0.107",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

# Send commands to the TV
def send_command(command):
    try:
        with samsungctl.Remote(config) as remote:
            remote.control(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def arrow_up():
    send_command("KEY_UP")

def arrow_down():
    send_command("KEY_DOWN")

def arrow_left():
    send_command("KEY_LEFT")

def arrow_right():
    send_command("KEY_RIGHT")

def enter():
    send_command("KEY_ENTER")

def voltar():
    send_command("KEY_RETURN")

# Função para aumentar o volume
def volume_up():
    send_command("KEY_VOLUP")

# Função para diminuir o volume
def volume_down():
    send_command("KEY_VOLDOWN")

# Função para abrir o menu
def open_menu():
    send_command("KEY_MENU")

def smarthub():
    send_command("KEY_CONTENTS")

# Create Tkinter window
root = tk.Tk()
root.title("Controle Remoto Samsung")

# Frame to arrow buttons
arrow_frame = ttk.Frame(root)
arrow_frame.grid(row=0, column=0, padx=10, pady=10)

# Adicionar botões de seta ao Frame
ttk.Button(arrow_frame, text="↑", command=arrow_up).grid(row=0, column=1)
ttk.Button(arrow_frame, text="↓", command=arrow_down).grid(row=2, column=1)
ttk.Button(arrow_frame, text="←", command=arrow_left).grid(row=1, column=0)
ttk.Button(arrow_frame, text="→", command=arrow_right).grid(row=1, column=2)
ttk.Button(root, text="Enter", command=enter).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(root, text="Voltar", command=voltar).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(root, text="VOL +", command=volume_up).grid(row=1, column=1, padx=10, pady=10)
ttk.Button(root, text="VOL -", command=volume_down).grid(row=2, column=1, padx=10, pady=10)
ttk.Button(root, text="Menu", command=open_menu).grid(row=1, column=0, columnspan=1, padx=10, pady=10)
ttk.Button(root, text="Smart Hub", command=smarthub).grid(row=2, column=0, columnspan=1, padx=10, pady=10)

# Iniciar loop da GUI
root.mainloop()


