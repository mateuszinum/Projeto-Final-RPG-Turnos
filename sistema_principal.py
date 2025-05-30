from classes import *
from rich.panel import Panel
from personagens import *

tema = Theme({
    "default": "bold grey82"
})


console = Console(theme=tema)



def selecionar_classe():
    console.clear()
    
    herois = [
        tanque,
        cavaleiro,
        assassino
    ]
    
    mensagem = ""

    for i, heroi in enumerate(herois, 1):
        mensagem += f"\n[bold plum1]{i}[/] - {heroi.nome} [bold plum1](Nível {heroi.level})[/]\n"
        mensagem += f"{' ' * 4}[bold bright_green]Vida: {heroi.vida_max}[/] | [bold red1]Ataque: {heroi.ataque}[/] | [bold bright_yellow]Defesa: {heroi.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {heroi.velocidade}[/]\n"
        mensagem += f"{' ' * 4}[bold]Arma: [bold red1]Dano {heroi.arma.dano}[/] ([bold orange1]Crítico: {heroi.arma.critico}%[/])\n"
    
    console.print(Panel.fit(mensagem, title="[bold medium_orchid]Escolha sua Classe", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n\n\n{' ' * 20}[bold grey82]Escolha sua classe (1-{len(herois)}): ")
        
        if escolha in ["1", "2", "3"]:
            heroi_escolhido = herois[int(escolha)-1]
            console.print(f"\n\n\n{' ' * 20}Você escolheu o [bold orange1]{heroi_escolhido.nome}[/]!", style="default")
            return heroi_escolhido
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida! Escolha de 1 a 4", style="default")


heroi = selecionar_classe()


while True:
    console.print(f"\n\n\n{' ' * 20}O que você deseja fazer?", style="default")
    console.print(f"\n{' ' * 20}([bold plum1]1[/]) - Explorar Dungeon\n{' ' * 20}([bold plum1]2[/]) - Abrir a porta do Boss\n{' ' * 20}([bold plum1]3[/]) - Ver status\n{' ' * 20}([bold plum1]0[/]) - Sair do jogo", style="default")

    escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
    
    if escolha == "1":
        if heroi.level <= 1:
            inimigo_nome = "Mago"

        elif heroi.level <= 2:
            inimigo_nome = random.choices(["Mago", "Fenix"], weights=[55, 45])[0]

        else:
            inimigo_nome = random.choices(["Fenix", "Guardiao"], weights=[60, 40])[0]
        
        inimigo = criar_monstro(inimigo_nome)
        
        luta_atual = Jogo(heroi, inimigo)

        luta_atual.executar()


        pass

    elif escolha == "2" :
        if heroi.chave:
            console.clear()
            console.print(f"\n\n\n{' ' * 20}Você abre a sala trancada e.", style="default")
            time.sleep(1)
            console.clear()
            console.print(f"\n\n\n{' ' * 20}Você abre a sala trancada e..", style="default")
            time.sleep(1)
            console.clear()
            console.print(f"\n\n\n{' ' * 20}Você abre a sala trancada e...", style="default")
            time.sleep(1)
            console.clear()
            inimigo = criar_monstro("Demonio")

            luta_atual = Jogo(heroi, inimigo)

            luta_atual.executar()

        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]A sala do boss está trancada![/]", style="default")
            console.print(f"{' ' * 20}[bold red1](Dica: Derrote os lacaios do boss para conseguir a chave e entrar na sala!)", style="default")
            pass

    elif escolha == "3":
        heroi.verificar_personagem()

    elif escolha == "0":
        exit()

    else:
        console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida![/]", style="default")



def menu_carregar_jogo():
    console.clear()
    console.print(Panel.fit("Bem-vindo ao NOME!", title="[bold medium_orchid]Menu Principal", border_style="medium_orchid", style="default"))
    console.print("\n\n\n([bold plum1]1[/]) - Novo Jogo")
    console.print("([bold plum1]2[/]) - Carregar Jogo")
    console.print("([bold plum1]0[/])- Sair do Jogo")

    while True:
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
        
        if escolha == "1":
            return selecionar_classe()
        elif escolha == "2":
            pass
            # Carregar jogo
        elif escolha == "0":
            exit()
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida!", style="default")

def menu_novo_jogo():
    console.clear()
    console.print(Panel.fit("Bem-vindo ao NOME!", title="[bold medium_orchid]Menu Principal", border_style="medium_orchid", style="default"))
    console.print("\n\n\n([bold plum1]1[/]) - Novo Jogo")
    console.print("([bold plum1]0[/]) - Sair do Jogo")

    while True:
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
        
        if escolha == "1":
            return selecionar_classe()
        elif escolha == "0":
            exit()
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida!", style="default")



# FAZER

# botar os menus iniciais
# ver se não ficou mt tosco o que eu fiz quando o herói entra na sala do boss
# bufar um pouco a poção de cura ou fazer com que quando tome ela, não conte como uma ação (o inimigo não ataca de volta)
# nerfar um pouco o boss final, mt vida slk