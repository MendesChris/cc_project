# Traue Bank

## Endpoints

endpoint        | Description   	|   Parametros
---             |   ---         	|   ---
create_account  |   cria o usuario no banco.    |   email, senha
login           |   aonde faz login.            |   email, senha
transactions    |   lista de transações         |   value, to
deposit         |   deposito imetiado na conta  |   value
withdraw        |   withdraw from account balance|  value

## Banco de Dados

### Tabelas

#### Users

field   	| type
---     	|   ---
id      	|   int
nome		|   string
sobrenome	|   string
cpf	    	|   string
genero		|   string
telefone	|   string
email		|   string
senha		|   string
cep	    	|   string
endereco	|   string
numero		|   int
bairro  	|   string
balance 	|   float

#### Transactions

field   |   type    |   none
---     |   ---     |   ---
type    |   ENUM    |   no
from    |   int     |   no
value   |   float   |   no
to      |   int     |   yes
