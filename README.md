# 🛡️ SISTEMA DE RPG DE TURNO

Neste jogo, o jogador escolhe um Herói entre três classes: **Tanque**, **Cavaleiro** e **Assassino**.  
Após a escolha, ele se aventura em uma **Dungeon**, onde enfrentará inimigos de acordo com o seu nível, como **Mago**, **Fênix**, **Guardião** e, por fim, o **Boss: Demônio**.

Alguns inimigos têm chance de carregar a **Chave do Boss**. Ao obtê-la, o jogador poderá entrar na sala do Demônio e tentar conquistar a Dungeon.

---

## 🎮 Sistema de Combate por Turno

A cada turno, o jogador pode escolher entre as seguintes ações:

### ⚔️ Atacar
- Tenta acertar o inimigo.
- Pode **falhar** ou **acertar criticamente** (dobrando o dano).
- O dano é calculado com base nos atributos **Ataque** e **Dano da Arma**.
- A chance de crítico é baseada em **Ataque** e no atributo **Crítico da Arma**.

### 🌀 Esquivar
- Tenta evitar o ataque inimigo.
- Se for bem-sucedido, **anula o dano recebido**.
- A chance de esquiva depende da **Velocidade** do Herói.

### 🔁 Contra-Atacar
- Espera o ataque do inimigo para tentar revidar.
- Se tiver sucesso, **ataca o inimigo e não sofre dano**.
- A chance de sucesso depende da **Velocidade**.

### 🧪 Tomar Poção
- Recupera **30% da Vida Máxima**.
- Apenas se houver poções disponíveis no inventário.

### 🛡️ Defender
- Aumenta a **Defesa em 50%** por 1 turno.
- Não possui chance de falha.

> O **inimigo**, por enquanto, só possui a ação de ataque.

---

## 📊 Atributos dos Personagens (Heróis e Inimigos)

- **Vida**: Total de dano que o personagem pode suportar.
- **Ataque**:  
  - Aumenta o dano causado.  
  - Aumenta a chance de crítico.
- **Defesa**: Reduz o dano recebido.
- **Velocidade**:  
  - Determina quem ataca primeiro.  
  - Afeta a chance de esquiva e contra-ataque.

---

## 🎒 Inventário

### 🔫 Arma
- **Dano**: Contribui no cálculo do ataque.
- **Crítico**: Aumenta a chance de ataque crítico.

### 💊 Poções
- Apenas os **Heróis** possuem.
- São recuperadas ao fim de cada combate.
- Número de uso é limitado.

### 🔑 Chave
- Obtida ao derrotar certos inimigos.
- Necessária para entrar na **Sala do Boss**.

---

## 📈 Sistema de Level Up

- A cada combate vencido, o Herói ganha **XP**, proporcional ao nível do inimigo.
- Ao alcançar o **XP Máximo**, o Herói sobe de nível.
- Cada nível oferece **pontos de atributos** para distribuir livremente.

---

## 🎞️ Sistema de Animação

O sistema de combate é renderizado **frame a frame**, utilizando a biblioteca [`rich`](https://github.com/Textualize/rich), o que proporciona uma experiência visual imersiva mesmo no terminal.

O design do sistema foi feito de forma que seja **fácil adicionar novos inimigos**.  
Para isso, basta fornecer:
- O **sprite** (imagem ASCII ou visual) do inimigo
- O **espaçamento inicial** adequado (baseado no tamanho da arte)
  
Isso garante que o inimigo e o herói fiquem corretamente alinhados na tela, independentemente do tamanho dos sprites.

---

## 💾 Sistema de Carregamento e Salvamento

### 📂 **Sistema de Carregar Jogo**

Ao iniciar o jogo, o jogador pode:

- 🔁 **Carregar um jogo salvo**, mantendo todos os atributos, nível, experiência e progresso da campanha.
- 🆕 **Começar uma nova jornada do zero**, escolhendo um novo herói e iniciando uma nova aventura na Dungeon.

---

### 💾 **Sistema de Save**

O sistema de salvamento é implementado com a biblioteca **`sqlite3`**, garantindo persistência completa de dados durante toda a jogatina.

Durante o jogo, **todas as ações** são salvas automaticamente, incluindo:

- O estado atual do Herói (vida, ataque, defesa, nível, XP, poções, chave)
- Os inimigos enfrentados
- Cada turno do combate
- Todo o histórico da partida

Essa abordagem permite que o jogador **retome exatamente de onde parou**, mesmo após fechar o jogo. Além disso, serve como uma poderosa ferramenta para que o **administrador ou desenvolvedor** monitore detalhadamente o que está acontecendo no jogo, analisando o banco de dados para fins de balanceamento, depuração ou narrativa.

---

## 🧰 Recursos Utilizados

Este projeto utiliza diversas bibliotecas e técnicas para criar uma experiência interativa e modular no terminal. Abaixo estão os principais recursos aplicados:

### 📚 Bibliotecas

- **[rich](https://github.com/Textualize/rich)** – Utilizada para criar uma interface visual elegante e animada no terminal (ex: painéis, cores, animações frame a frame).
- **sqlite3** – Banco de dados embutido para persistência de dados dos personagens, inimigos, combates, ações e histórico de turnos.

### 🧱 Estrutura do Projeto

- **Programação Orientada a Objetos (POO)** – Heróis, inimigos e lutas são implementados como classes com encapsulamento de lógica e atributos.
- **Sistema de combate baseado em turnos** – Controlado por lógica condicional baseada na velocidade dos personagens.
- **Banco de dados relacional** – Com tabelas como `Personagens`, `Inimigos`, `Jogos`, `Turnos`, `Historico`, e `Acoes`, que registram todas as ações do jogador e dos inimigos.
- **Sistema de XP e Level Up** – Com crescimento dinâmico baseado em fórmulas matemáticas e pontos de atributo distribuíveis.
- **Sistema de Save e Load** – Permite que o progresso do jogador seja salvo automaticamente e carregado em sessões futuras.

### 🖼️ Animações ASCII (sprites)
- Renderização por frame no terminal com posicionamento baseado em espaçamento horizontal.
- Estrutura modular que facilita a adição de novos personagens e inimigos com novos sprites.

### ⚙️ Outros destaques
- Lógica de chance de sucesso (ataque, crítico, esquiva, etc.) com **pesos probabilísticos** (`random.choices`).
- Sistema de chave e progressão até o Boss.
- Separação de responsabilidades por arquivos:
  - `classes.py` – Lógica de herói, inimigo e combate
  - `personagens.py` – Instanciamento dos heróis e inimigos
  - `sql.py` – Interface com banco de dados
  - `sistema_principal.py` – Menu principal e controle de fluxo do jogo

---

