# GymBro Api

O projeto se trata de uma plataforma voltado para pessoas que gostam e querem poder cadastrar suas séries de academia de modo a ter sempre um local onde eles possam usar para fazer o seu treino matinal ou queiram saber o seu histórico de treinos para poder comprar exercício e executar estímulos diferentes no mesmo.

## Passo a passo para utilização (sem docker)

Criando o ambiente virtual python

1. virtualenv venv
2. source venv/bin/activate

Instalacao de dependencias via pip

3. pip install -r requirements.txt

Para rodar a aplicacao basta das o comando

4. flask run

Para debugar o programa basta dar o comando

5. flask --debug run

## Passo a passo para utilização (com docker)

1. Crie uma imagem docker utilizando **docker build -t gym-bro-api-docker .**
2. A partir da imagem acima execute o container rodando o comando **docker run -p 3000:5000 gym-bro-api-docker**
3. Caso queira interagir com o container utiliza o comando **docker exec -it <ID_do_seu_contêiner> bash** passando o id do container gerado no comando acima

### Para acessar o swagger:

- http://localhost:5000/docs

### A rota da api e:

- http://localhost:5000

### SWAGGER

Existem 4 rotas no swagger, a de login('/login'), a de registro('/register'), a de listar todos os exercicios cadastrados('/exercise->get') e a de cadastrar novo exercicio('/exercise->post').

#### ROTAS POST E GET DOS EXERCISES

As rotas de login e registro sao livres, ou seja, nao precisam de token de acesso para serem chamadas, ja as outras duas precisam, entao caso queira ver o funcionamento das ultimas, sugiro fazer o login no proprio swagger, copiar o token de acesso, clicar em authorize na tela do swagger, digitar o texto Bearer e colar o token em seguida com um espaco, desta maneira poderam ser feitas as chamadas para as outras rotas fechadas.
