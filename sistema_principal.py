from classes import *
from rich.panel import Panel
from menus import *


tema = Theme({
    "default": "bold grey82"
})


console = Console(theme=tema)

heroi = menu_inicial()

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

# FAZER

# bufar um pouco a poção de cura ou fazer com que quando tome ela, não conte como uma ação (o inimigo não ataca de volta)
# nerfar um pouco o boss final, mt vida slk
