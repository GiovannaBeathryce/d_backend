# d_backend

Aplicação Back-End baseada em um arquivo de texto(CNAB) para controle de entradas e saidas de valores.
Dentro da aplicação temos uma página home, onde deve ser feito o upload do arquivo a ser parseado. Ao fim do carregagento os dados serão tratados e o usuário será encaminhado para uma página onde serão listadas todas as empresas que possuem registros no arquivo enviado, e ao clicar em cada uma delas será redirecionado para uma página que exibe uma tabela com todos os dados de entrada e saida de valores da empresa selecionada, junto ao valor total em caixa.


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
    

