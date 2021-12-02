# Traue Bank

## Objetivos

O site Traue Internet Banking tem como objetivo facilitar a operação online de consultas e transações do Traue Bank. Utilizando telas de aparência amigável, a intenção é que todas as operações sejam intuitivas e de fácil acesso para todos os usuários, até mesmo os que não tem muito conhecimento em tecnologia.  
Também temos como objetivo trazer confiança e segurança para os usuários, tentando crescer cada vez mais, para alcançar um maior público, já que o nosso objetivo é atingir todo tipo de público.  

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