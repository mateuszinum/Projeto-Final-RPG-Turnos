from reset import *
from classes import *
from personagens import *
from rich.panel import Panel


def menu_inicial():
    if ha_jogos_salvos():
        return menu_carregar_jogo()
    else:
        return menu_novo_jogo()

def menu_carregar_jogo():
    console.clear()
    mensagem = (
        f"\n([bold plum1]1[/]) - Novo Jogo\n"
        f"([bold plum1]2[/]) - Carregar Jogo\n"
        f"([bold plum1]0[/]) - Sair do Jogo\n"
    )
    console.print(Panel.fit(mensagem, title="[bold grey82]Menu Principal", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")

        if escolha == "1":
            console.print(f"\n\n{' ' * 20}[bold red1]Isso irá apagar todo o progresso anterior![/]", style="default")
            confirmacao = console.input(f"{' ' * 20}[bold grey82]Deseja continuar? ([green]S[/]/[red]N[/]): ").lower()

            if confirmacao == "s":
                console.print(f"\n\n{' ' * 20}[bold green_yellow]Progresso anterior apagado com sucesso![/]\n", style="default")
                tanque, cavaleiro, assassino = criar_personagem_novo()
                time.sleep(2)
                return menu_selecionar_classe(tanque, cavaleiro, assassino)
            else:
                console.print(f"\n\n{' ' * 20}[bold yellow]Cancelado. Voltando ao menu...[/]", style="default")
                time.sleep(2)
                return menu_carregar_jogo()

        elif escolha == "2":
            tanque, cavaleiro, assassino = obter_herois()
            return menu_selecionar_classe(tanque, cavaleiro, assassino)
        elif escolha == "0":
            exit()
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida!", style="default")

def menu_novo_jogo():
    console.clear()
    mensagem = (
        f"\n\n([bold plum1]1[/]) - Novo Jogo\n"
        f"([bold plum1]0[/]) - Sair do Jogo\n"
    )
    console.print(Panel.fit(mensagem, title="[bold grey82]Menu Principal", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
        
        if escolha == "1":
            tanque, cavaleiro, assassino = criar_personagem_novo()
            return menu_selecionar_classe(tanque, cavaleiro, assassino)
        elif escolha == "0":
            exit()
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida!", style="default")

def menu_selecionar_classe(tanque, cavaleiro, assassino):
    console.clear()

    herois = [
        tanque,
        cavaleiro,
        assassino
    ]

    mensagem = ""

    for i, heroi in enumerate(herois, 1):
        mensagem += f"\n[bold plum1]{i}[/] - {heroi.nome[:len(heroi.nome) - 11]} [bold plum1](Nível {heroi.level})[/]\n"
        mensagem += f"{' ' * 4}[bold bright_green]Vida: {heroi.vida_max}[/] | [bold red1]Ataque: {heroi.ataque}[/] | [bold bright_yellow]Defesa: {heroi.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {heroi.velocidade}[/]\n"
        mensagem += f"{' ' * 4}[bold]Arma: [bold red1]Dano {heroi.arma.dano}[/] ([bold orange1]Crítico: {heroi.arma.critico}%[/])\n"
    
    console.print(Panel.fit(mensagem, title="[bold medium_orchid]Escolha sua Classe", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n\n\n{' ' * 20}[bold grey82]Escolha sua classe (1-{len(herois)}): ")
        
        if escolha in ["1", "2", "3"]:
            heroi_escolhido = herois[int(escolha)-1]
            console.print(f"\n\n\n{' ' * 20}Você escolheu o [bold orange1]{heroi_escolhido.nome[:len(heroi_escolhido.nome) - 11]}[/]!", style="default")
            return heroi_escolhido
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida! Escolha de 1 a 4", style="default")