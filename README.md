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

field   	| type      |   nullable
---     	|   ---     |   ---
id      	|   int     |   não
nome		|   string	|   não
sobrenome	|   string	|   não
cpf	    	|   string	|   não
genero		|   string	|   não
telefone	|   string	|   não
email		|   string	|   não
senha		|   string	|   não
cep	    	|   string	|   não
endereco	|   string	|   não
numero		|   int     |   não
bairro  	|   string	|   não
balance 	|   float   |   não

**primary-key:** id

#### Transactions

field   | type      |   nullable
---     |   ---     |   ---
id      |   int     |   não
type    |   ENUM    |   não
from    |   int     |   não
value   |   float   |   não
to      |   int     |   sim

**primary-key:** id