from entidades import *
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
        mensagem += f"\n[bold plum1]{i}[/] - {personagem.nome}\n"
        mensagem += f"{' ' * 4}[bold bright_green]Vida: {personagem.vida_max}[/] | [bold red1]Ataque: {personagem.ataque}[/] | [bold bright_yellow]Defesa: {personagem.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {personagem.velocidade}[/]\n"
        mensagem += f"{' ' * 4}[bold]Arma: [bold red1]Dano {personagem.arma.dano}[/] ([bold orange1]Crítico: {personagem.arma.critico}%[/])\n"
    
    console.print(Panel.fit(mensagem, title="[bold medium_orchid]Escolha sua Classe", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n\n\n{' ' * 20}[bold grey82]Escolha sua classe (1-{len(personagens)}): ")
        
        if escolha in ["1", "2", "3"]:
            personagem_escolhido = personagens[int(escolha)-1]
            console.print(f"\n\n\n{' ' * 20}Você escolheu o [bold orange1]{personagem_escolhido.nome}[/]!", style="default")
            return personagem_escolhido
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida! Escolha de 1 a 4", style="default")


personagem = selecionar_classe()


while True:
    console.print(f"\n\n\n{' ' * 20}O que você deseja fazer?", style="default")
    console.print(f"\n{' ' * 20}([bold plum1]1[/]) - Seguir em frente\n{' ' * 20}([bold plum1]2[/]) - Ver status\n{' ' * 20}([bold plum1]3[/]) - Sair do jogo", style="default")
    
    escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
    
    if escolha == "1":

        inimigo = random.choices([mago, fenix, guardiao], weights=[33, 33, 33])[0]

        luta_atual = Jogo(personagem, inimigo)

        luta_atual.executar()


        pass

    elif escolha == "2":
        pass

    elif escolha == "3":
        exit()

    else:
        console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida![/]", style="default")


# FAZER


# fazer o negócio pra ver status do personagem
# botar pra dropar chave pro boss
# botar mais um inimigo
# fazer gerar certinho novos inimigos
# botar menos pontos pra upar e diminuir quanto cada atributo recebe, mt forte
# balancear inimigos, sistema de xp, (personagens?)