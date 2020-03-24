# Aplicação de calculo de meses de experiência de freelancers

A API recebe um payload com um freelancer e seus trabalahos executados e retorna os meses de experiência em cada uma das skills mencionadas

## Subir aplicação 
1. Clonar repositório
1. Instalar o pipenv https://github.com/pypa/pipenv#installation
1. Com o pipenv instalado executar ``` pipenv install``
1. Executar ``` pipenv shell ```
1. Dentro do shell do python executar a aplicação 
    1. Definir variaveis de ambiente 
    ``` PYTHON_ENV=development ``` (*development* ou *production*) 
    1. Executar o comando ``` python src/main.py ```

## Como utilizar a API ?

A API recebe somente POSTs no endpoint **/freelance** que devem estar no formato de **examples/freelancer.json** conforme descrito na proposta do exercicio e retorna um json com os meses calculados conforme escopo

## Obsevações
1. Caso a api seja inicializada em modo desenvolvimento (PYTHON_ENV=development ou sem definição dessa variavel de ambiente), o swagger da api está localizado em **/api/swagger**