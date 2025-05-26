from entidades import *
import animacoes as cena
from rich.panel import Panel

tema = Theme({
    "default": "bold grey82"
})


console = Console(theme=tema)


# Selecionar a classe do personagem
def selecionar_classe():
    console.clear()
    
    personagens = [
        tanque,
        cavaleiro,
        assassino
    ]
    
    mensagem = ""

    for i, personagem in enumerate(personagens, 1):
        mensagem += f"\n[bold magenta]{i}[/] - {personagem.nome}\n"
        mensagem += f"{" " * 4}[bold bright_green]Vida: {personagem.vida_max}[/] | [bold red1]Ataque: {personagem.ataque}[/] | [bold bright_yellow]Defesa: {personagem.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {personagem.velocidade}[/]\n"
        mensagem += f"{" " * 4}[bold ]Arma: [bold red1]Dano {personagem.arma.dano}[/] ([bold orange1]Crítico: {personagem.arma.critico}%[/])\n"
    
    console.print(Panel.fit(mensagem, title="[bold royal_blue1]Escolha sua Classe", border_style="bold slate_blue3", style="default"))

    while True:
        escolha = console.input(f"\n[bold grey82]Escolha sua classe (1-{len(personagens)}): ")
        
        if escolha in ["1", "2", "3", "4"]:
            personagem_escolhido = personagens[int(escolha)-1]
            console.print(f"\nVocê escolheu o [bold orange1]{personagem_escolhido.nome}[/]!", style="default")
            return personagem_escolhido
        else:
            console.print("[bold red1]Opção inválida! Escolha de 1 a 4", style="default")

personagem = selecionar_classe()

while True:
    console.print("\nO que você deseja fazer?", style="default")
    console.print("[bold magenta]1[/] - Seguir em frente\n[bold magenta]2[/] - Ver status\n[bold magenta]3[/] - Testes\n[bold magenta]4[/] - Sair do jogo", style="default")
    
    escolha = console.input("[bold grey82]Escolha uma opção: ")
    
    if escolha == "1":
        # não sei como vai ser o sistema pra achar inimigo, daí só coloquei aleatório
        # e outra, sobre desviar e contra atacar, não sei se vou conseguir fazer uma animação bonitinha
        # daí acho que só vou trocar a cor da tela, que nem faço quando o bicho é atingido
        inimigo = random.choices(["Mago"], weights=[100])[0]
        
        # não tá funcionando, precisei parar
        if inimigo == "Mago":
            luta_atual = Jogo(personagem, mago)

        luta_atual.executar()


        pass

    elif escolha == "2":
        pass

    elif escolha == "3": # Teste de todas as animações
        menu_teste = (
            "\n(1) - Animação ataque personagem"
            "\n(2) - Animação ataque inimigo"
            "\n(3) - Animação personagem atingido"
            "\n(4) - Animação monstro atingido"
        )
        console.print(Panel.fit(menu_teste))
        escolha = console.input("[bold grey82]Qual cena rodar? ")
        if escolha == "1":
            inimigo = "Mago"
            tipo = "Fogo"
            cena.ataque_personagem(inimigo, tipo)
            tipo = "Gelo"
            cena.ataque_personagem(inimigo, tipo)

        elif escolha == "2":
            inimigo = "Mago"
            tipo = "Fogo"
            cena.ataque_monstro(inimigo, tipo)
            tipo = "Gelo"
            cena.ataque_monstro(inimigo, tipo)

        elif escolha == "3":
            inimigo = "Mago"
            tipo = "Fogo"
            cena.personagem_atingido(inimigo, tipo)
            tipo = "Gelo"
            cena.personagem_atingido(inimigo, tipo)

        elif escolha == "4":
            inimigo = "Mago"
            tipo = "Fogo"
            cena.monstro_atingido(inimigo, tipo)
            tipo = "Gelo"
            cena.monstro_atingido(inimigo, tipo)

    elif escolha == "4":
        exit()
    else:
        console.print("[bold red1]Opção inválida![/]", style="default")