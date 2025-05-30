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

## 💾 Sistema de Save

- Ao iniciar o jogo, o jogador pode:
  - **Carregar um jogo salvo** (mantendo level e atributos).
  - **Começar um novo jogo** do zero.


