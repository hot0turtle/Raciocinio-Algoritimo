import random
import tkinter as tk
from tkinter import ttk

def set_choice(text1, command1):
    option1_button.config(text=text1, command=command1)
    option2_button.config(text=text2, command=command2)
    # Retira opcoes antes da decisao
    choice_frame.pack_forget() 
    choice_frame.pack(side='bottom', fill='x', pady=5)

def set_choices(text1, command1, text2, command2):
    option1_button.config(text=text1, command=command1)
    option2_button.config(text=text2, command=command2)
    # Retira opcoes antes da decisao
    choice_frame.pack_forget() 
    choice_frame.pack(side='bottom', fill='x', pady=5)


def hide_choices():
    """=Funcao para esconder."""
    choice_frame.pack_forget()

def start_choice():
    """Inicio."""
    text_area.insert('end', "Você acorda em uma ilha deserta após um naufrágio. O sol quente bate em sua pele, e o som das ondas quebra o silêncio. Sua última lembrança é do barco afundando durante uma tempestade. Agora, você precisa tomar decisões para garantir sua sobrevivência.\n")
    set_choices("Explorar a floresta em busca de recursos. ", go_left, "Caminhar pela praia e procurar sinais de vida.", go_right)

#Floresta

def go_left():
    new_value = max(progress['value'] - random.randint(20, 40), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    print(new_value)
    hide_choices()
    text_area.insert('end', "Você entra na floresta e logo encontra um pequeno rio de água cristalina. A sombra das árvores oferece um alívio do calor intensoa.\n")
    set_choices("Beber a agua do Rio", continacao_left, "Beber a agua do Rio", continacao_le)

def  continacao_left():
    hide_choices()
    text_area.insert('end', "Humm, voce começou a passar mal, o que deseja fazer? .\n")
    set_choices("Beber mais a água do rio", rio, "Procurar uma fonte de água mais segura", procurar)

def  continacao_le():
    hide_choices()
    text_area.insert('end', "Humm, voce começou a passar mal, o que deseja fazer? .\n")
    set_choices("Beber mais a água do rio", rio, "Procurar uma fonte de água mais segura", procurar)

def  rio():
    new_value = max(progress['value'] - random.randint(15, 35), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', " A água pode estar contaminada. Você começa a se sentir mal; O sol começa a se pôr, e a temperatura cai rapidamente. O vento aumenta, e você sabe que precisa se preparar para a noite. Após algum tempo, você encontra destroços do barco, incluindo madeira, cordas e pedaços de tecido.\n")
    set_choices(" Construir um abrigo", abrigo, " Acender uma fogueira", fogueira)

def procurar():
    new_value = max(progress['value'] + random.randint(5, 15), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Você encontra um coqueiro e consegue beber água de coco.\n O sol começa a se pôr, e a temperatura cai rapidamente. O vento aumenta, e você sabe que precisa se preparar para a noite. Após algum tempo, você encontra destroços do barco, incluindo madeira, cordas e pedaços de tecido.")
    set_choices(" Construir um abrigo", abrigo, "Acender uma fogueira", fogueira)


#Cenario 3
    
def abrigo():
    new_value = max(progress['value'] - random.randint(15, 30), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Pela manhã, pescadores da ilha o encontram e decidem ajudá-lo.\n")
    set_choice(" Construir um abrigo", resultado)

def fogueira():
    new_value = max(progress['value'] - random.randint(5, 15), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Um navio distante vê a fumaça e envia uma equipe de resgate rapidamente.\n")
    set_choice(" Construir um abrigo", resultado)


#Praia
def go_right():
    new_value = max(progress['value'] + random.randint(5, 15), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Você encontra um coqueiro e consegue beber água de coco.\n")
    set_choices("Enter a cave", enter_cave, "Return", return_back)



#final



root = tk.Tk()
root.title("Text Based Game")

# Create a text widget for displaying game narrative
text_area = tk.Text(root, wrap='word', height=20, width=60)
text_area.pack(side='top', fill='both', expand=True)


# Create a frame for the status bar (progress bar and number label)
status_frame = tk.Frame(root)
status_frame.pack(side='bottom', fill='x')

progress_label = tk.Label(status_frame, text="100", font=("Helvetica", 10))
progress_label.pack(side='right', padx=10)

progress = ttk.Progressbar(status_frame, orient='horizontal', length=200,
                           mode='determinate', maximum=100)
progress.pack(side='right')
progress['value'] = 100  # Starting at 100

# Create a frame to hold the choice buttons (do not pack it initially)
choice_frame = tk.Frame(root)
option1_button = tk.Button(choice_frame, text="Option 1")
option1_button.pack(side='left', padx=10)
option2_button = tk.Button(choice_frame, text="Option 2")
option2_button.pack(side='left', padx=10)

# For demonstration, start with the initial choice after 2 seconds
root.after(2000, start_choice)

root.mainloop()