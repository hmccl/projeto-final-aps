# Projeto Final APS

## Documentação

### Diagrama de caso de uso

![Diagrama de caso de uso](./docs/diagrama-de-caso-de-uso.png)

#### Anotar pedido

**Descrição:** Atendente anota pedido do cliente.

**Atores:** Atendente.

**Pré-condições:** Atendente seleciona seu nome.

**Fluxo básico:**

1. Inicia pedido, caso o cliente tenha um cadastro.

1. Adiciona as pizzas desejadas pelo cliente.

1. Finaliza o pedido do cliente.

**Fluxo alternativo:**

1. Cliente não é cadastrado.

1. Cadastrar cliente.

#### Cadastrar dados

**Descrição:** Atendente cadastra os dados do cliente.

**Atores:** Atendente.

**Pré-condições:** Cliente não está cadastrado.

**Fluxo básico:**

1. Inicia o cadastro do cliente, pedindo nome, número de telefone e endereço.

1. Finaliza o cadastro do cliente.

**Fluxo alternativo:**

1. Cliente é cadastrado.

1. Não cadastrar cliente novamente.

### Diagrama de sequência

![Diagrama de sequência](./docs/diagrama-de-sequencia-1.png)

![Diagrama de sequência](./docs/diagrama-de-sequencia-2.png)

### Diagrama de classe

![Diagrama de classe](./docs/diagrama-de-classe.png)

## Instruções

Crie um *virtual environment*.

```
python3 -m venv env
```

Instale as bibliotecas.

```
env/bin/pip install -r requirements.txt
```

Execute o programa.

```
env/bin/python3 main.py
```

## Captura de tela

![Captura de tela](./docs/captura-de-tela.png)
