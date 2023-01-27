# d_backend

Aplicação Back-End paseada em um arquivo de texto(CNAB)


# Instruções para inicializar o projeto:

Após clonar o repositório

# Venv
Inicie um hambiente virtual em sua maquina 
    Python -m venv venv

# Ativação do hambiente virtual
Ative o hambiente
    source venv/scripts/activate

# Instalação de dependencias
Execute 
    pip install -r requirements.txt

# Migrações da Model
Para rodarmos as migrações devemos executar:
    python manage.py makemigrations
    python manage.py migrate

# Rodar o servidor
Rode o servidor com 
    python manage.py runserver

Abra o link gerado no navegador
    

