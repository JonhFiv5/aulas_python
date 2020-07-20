# Executando programas externos com o Python

import subprocess

# Comando ping, passamos um número de IP, nesse caso vamos usar da própria
# máquin
# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4
# (é preciso desses argumentos extras para parar a execução, porque o
# Linux não para automaticamente)

# No windows só passamos os dois primeiros
# processo = subprocess.run(
#     ['ping', '127.0.0.1', '-c', '4'],
#     capture_output=True,  # Para guardar as informções em stdout
#     text=True  # Para passar as informações como texto
# )

# Executando outro arquivo Python
processo = subprocess.run(
    ['python3',
     '/home/joao/Programacao/CursoPython/playground/le_livros.py',
     '-l'],
    capture_output=True,
    text=True
)

saida = processo.stdout  # Estando armazenadas em stdout podemos tratar como
# quisermos
print(saida)
