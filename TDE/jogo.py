import random
import tkinter as tk
from tkinter import ttk



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
    hide_choices()
    text_area.insert('end', "Você entra na floresta e logo encontra um pequeno rio de água cristalina. A sombra das árvores oferece um alívio do calor intensoa.\n")
    set_choices("Beber a agua do Rio", continacao_left, "Procurar uma outra fonte de água ", procurar)

def  continacao_left():
    new_value = max(progress['value'] - random.randint(15, 35), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
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
    print(progress['value'])
    set_choices(" Ver Resultado", resultado,"Resultado", result)

def fogueira():
    new_value = max(progress['value'] - random.randint(5, 15), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Um navio distante vê a fumaça e envia uma equipe de resgate rapidamente.\n")
    set_choices(" Ver Resultado", resultado,"Resultado", result)


#Praia
def go_right():
    new_value = max(progress['value'] - random.randint(20, 40), 0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Você decide caminhar pela praia, sentindo o calor do sol e a areia quente sob seus pés. Você também começa a sentir fome e cansaço.\n")
    set_choices("Caçar ou Pescar", fish, "Procurar Frutas ", apples)

def fish():
    new_value = max(progress['value'] - random.randint(15,35),0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', "Você não consegue coletar nada de proteína")
    set_choices(" Construir um abrigo", abrigo, "Acender uma fogueira", fogueira)

def apples():
    new_value = max(progress['value'] + random.randint(10,25),0)
    progress['value'] = new_value
    progress_label.config(text=str(int(new_value)))
    hide_choices()
    text_area.insert('end', " Você encontra frutas e se sente reinvigorado\n")
    set_choices(" Construir um abrigo", abrigo, "Acender uma fogueira", fogueira)


#final

def resultado():
    if progress['value'] >= 70:
        hide_choices()
        text_area.insert('end', " O resgate chega e você está tão bem que dá até para dar autógrafos para os socorristas. (Final Alegre – Você foi resgatado, e até parece que esteve em um spa por dias! 😎)\n")
    elif progress['value'] >= 30 and progress['value'] < 70:
        hide_choices()
        text_area.insert('end', " O resgate chega, mas você está tão fraco que mal consegue fazer uma piada. (Final Irônico – Você sobreviveu, mas está mais parecendo um zumbi do que um herói.🤕)\n")
    elif progress['value'] < 30:
        hide_choices()
        text_area.insert('end', " O resgate chega, mas ele mal consegue levantar e até acha que o socorro é só mais um pesadelo. (Final Surreal – Você foi resgatado, mas vai precisar de muitos cafés para voltar à vida normal! ☠☠)\n")

def result():
    if progress['value'] >= 70:
        hide_choices()
        text_area.insert('end', " O resgate chega e você está tão bem que dá até para dar autógrafos para os socorristas. (Final Alegre – Você foi resgatado, e até parece que esteve em um spa por dias!)\n")
    elif progress['value'] >= 30 and progress['value'] < 70:
        hide_choices()
        text_area.insert('end', " O resgate chega, mas você está tão fraco que mal consegue fazer uma piada. (Final Irônico – Você sobreviveu, mas está mais parecendo um zumbi do que um herói.)\n")
    elif progress['value'] < 30:
        hide_choices()
        text_area.insert('end', " O resgate chega, mas ele mal consegue levantar e até acha que o socorro é só mais um pesadelo. (Final Surreal – Você foi resgatado, mas vai precisar de muitos cafés para voltar à vida normal!)\n")


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