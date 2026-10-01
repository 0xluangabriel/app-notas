# 📝 App de Notas (Terminal)

Um gerenciador de notas de linha de comando escrito em **Python puro**, sem bibliotecas externas. Foi meu primeiro projeto pessoal em Python, feito na segunda semana de estudo, com o objetivo de praticar os fundamentos da linguagem construindo algo funcional do zero.

O programa roda no terminal e permite **criar, visualizar, editar e excluir** notas. As notas ficam salvas em um arquivo JSON, então continuam disponíveis mesmo depois de fechar o programa.

---

## ✨ Funcionalidades

- **Criar nota** — cadastra uma nota com título e conteúdo.
- **Visualizar notas** — lista todas as notas numeradas, com título e conteúdo.
- **Editar nota** — altera o conteúdo de uma nota existente.
- **Excluir nota** — remove uma nota, com confirmação antes de apagar.
- **Persistência em disco** — as notas são salvas automaticamente em `notas.json` a cada alteração e carregadas ao iniciar.
- **Tratamento de erros** — o programa não quebra se o usuário digitar uma opção inválida, letras onde se espera número, ou um número de nota que não existe.

---

## 🎬 Exemplo de uso

```
   (╬￣皿￣)凸    Escolha uma opção:
                        1. Criar nova nota
                        2. Editar nota existente
                        3. Visualizar notas
                        4. Excluir nota
                        5. Sair

Digite a opção desejada: 3
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
1 - Título: Compras
Conteúdo: arroz, feijão, café
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
2 - Título: Faculdade
Conteúdo: prova de Cálculo dia 10

Aperte Enter para voltar ao menu...
```

---

## 🛠️ Tecnologias e conceitos aplicados

O projeto usa **apenas a biblioteca padrão do Python** (nada de `pip install`). Ao longo do desenvolvimento, apliquei:

| Conceito | Onde foi usado |
|---|---|
| **Dicionários** | Estrutura principal para guardar as notas (`{título: conteúdo}`) |
| **Laço `while True`** | Menu que repete até o usuário escolher "Sair" |
| **`break` e `continue`** | Sair do loop do menu e voltar ao menu após erros |
| **`if` / `elif` / `else`** | Roteamento das opções do menu e validações |
| **Laço `for` com `enumerate()`** | Listar as notas numeradas a partir de 1 |
| **`try` / `except`** | Tratar entradas inválidas (`ValueError`) e arquivo inexistente (`FileNotFoundError`) |
| **Métodos de string** (`.upper()`, `.strip()`) | Padronizar a confirmação (S/N) e limpar espaços |
| **Módulo `json`** | Salvar (`json.dump`) e carregar (`json.load`) as notas |
| **`with open()`** | Abrir arquivos de forma segura (fechamento automático) |
| **`os.system`** | Limpar a tela do terminal entre as ações |

---

## 🧠 Como funciona (por dentro)

### Estrutura de dados

As notas são armazenadas em um **dicionário**, onde a **chave é o título** e o **valor é o conteúdo**:

```python
notas_usuario = {
    "Compras": "arroz, feijão, café",
    "Faculdade": "prova de Cálculo dia 10"
}
```

### O menu

O programa gira dentro de um `while True`. A cada volta ele mostra o menu, lê a opção do usuário e a converte para inteiro dentro de um `try/except` (para não quebrar se digitarem letras). A opção 5 executa um `break`, encerrando o loop.

### Numeração das notas

Como dicionário não tem posição, para exibir as notas numeradas eu uso o `enumerate()` sobre os itens, começando em 1:

```python
for numero, (titulo, conteudo) in enumerate(notas_usuario.items(), start=1):
    print(f'{numero} - Título: {titulo}')
    print(f'Conteúdo: {conteudo}')
```

Quando o usuário precisa escolher uma nota (para editar ou excluir), eu transformo as chaves em uma lista, converto o número digitado em posição (subtraindo 1) e recupero o título correspondente:

```python
lista_notas = list(notas_usuario.keys())
titulo_escolhido = lista_notas[numero_digitado - 1]
```

### Persistência (JSON)

- **Ao iniciar**, o programa tenta carregar as notas do arquivo `notas.json`. Se o arquivo ainda não existir (primeira execução), ele começa com um dicionário vazio:

```python
try:
    with open('notas.json', 'r', encoding='utf-8') as arquivo:
        notas_usuario = json.load(arquivo)
except FileNotFoundError:
    notas_usuario = {}
```

- **A cada alteração** (criar, editar ou excluir), o dicionário é gravado de volta no arquivo:

```python
with open('notas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(notas_usuario, arquivo, ensure_ascii=False, indent=4)
```

O `ensure_ascii=False` preserva os acentos (para "Reunião" não virar `Reunião`) e o `indent=4` deixa o arquivo legível.

### Validações

- **Opção inválida no menu** → cai no `else` e avisa o usuário.
- **Letras onde se espera número** → capturado por `try/except ValueError`.
- **Número de nota inexistente** (ex.: digitar 99 com só 3 notas) → verificado com `if` antes de acessar a lista.
- **Lista vazia** → ao tentar visualizar/editar/excluir sem notas, o programa avisa em vez de dar erro.

---

## 🚀 Como executar

Você só precisa ter o **Python 3** instalado.

```bash
# clone o repositório
git clone https://github.com/0xluangabriel/app-notas.git

# entre na pasta
cd app-notas

# execute
python main.py
```

> No Windows, dependendo da instalação, use `py main.py`.

O arquivo `notas.json` é criado automaticamente na primeira vez que você salva uma nota.

---

## 📁 Estrutura do projeto

```
.
├── main.py        # código-fonte do programa
├── notas.json     # arquivo gerado automaticamente com as notas salvas
└── README.md      # este arquivo
```

---

## 🔭 Melhorias futuras

Ideias que pretendo implementar para continuar praticando:

- [ ] Organizar o código em **funções** (`criar_nota()`, `salvar_notas()`, etc.) para eliminar repetição.
- [ ] Permitir **editar o título** da nota, não só o conteúdo.
- [ ] Adicionar **data de criação** a cada nota (módulo `datetime`).
- [ ] **Buscar** notas por palavra-chave.
- [ ] Adicionar cores ao terminal para melhorar a leitura.

---

## 📌 Sobre

Meu primeiro projeto pessoal em Python, feito para praticar os fundamentos da linguagem que venho estudando por conta própria. O foco foi **entender cada linha** em vez de copiar código pronto — todos os conceitos acima foram estudados e aplicados por mim durante a construção.

Feito por **Luan Gabriel Alves da Silva** — [github.com/&lt;luan-gabriel-silva&gt;](https://github.com/&lt;luan-gabriel-silva&gt;)
