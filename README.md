# MVCPython

O *MVCPython* é um projeto desenvolvido com base nas aulas sobre MVC em Python do (Programador Lhama)[https://github.com/programadorLhama], porém com alguns adendos pessoais.

Playlist: [Padrão MVC em Python](https://www.youtube.com/watch?v=abqeIMr1hsg&list=PLAgbpJQADBGKvsjOu4gHU5E9WUQs8XRgS&ab_channel=ProgramadorLhama)

# Funcionalidades
Como o foco do projeto é a implementação da aquitetura suas funcionalidades são bem básicas:
- Adicionar pessoas em um banco de dados (simulado em memória)
- Buscar pessoas por nome
- Sair

# MVC
Como o foco do projeto é o MVC aqui vai a explicação dos componentes da implementacao dessa arquitetura:
## Constructor

Dentro dele, temos um diretório chamado constructor/ onde vamos colocar funções que serão responsáveis pelos casos de uso da nossa aplicação. Cada caso de uso (aqui chamado de construtor ou processo) será responsável por instância/chamar e coordenar os componentes necessários para que o resultado esperado ocorra (às vezes somente a View e as vezes a View e Controller). O constructor vai construir os componentes que nossa aplicação vai utilizar.\

## Models

## Views

## Controllers


# Melhorias
## Respostas
As respostas retornadas pelo `PersonController` poderiam ser um objeto. Isso permitira que a logica das respostas pudesse ser alterada sem ter que acessar o `controller`. Alem de que permitira criar um padrao para as respostas.

## Paginacao
Se fosse possivel verificar todos os usuarios no banco de dados incluir um sistema de paginacao seria muito util para tornar a leitura mais facil e menos custosa (pois nao seria necessario ler todo o banco de dados de uma vez).

## Erros Personalizados
Os erros poderiam ser extensoes da classe Exception do Python, permitindo assim lancar erros especificos e fazer um tratamento de erros personalizado.
