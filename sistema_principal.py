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
        mensagem += f"\n[bold plum1]{i}[/] - {heroi.nome}\n"
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
    console.print(f"\n{' ' * 20}([bold plum1]1[/]) - Seguir em frente\n{' ' * 20}([bold plum1]2[/]) - Ver status\n{' ' * 20}([bold plum1]3[/]) - Sair do jogo", style="default")

    #COLOCA UMA OPCAO 2 SENDO IR PARA SALA DO BOSS 

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

    elif escolha == "2":
        if heroi.chave:
            #COLOCA UMA MSG, ENTRANDO NA SALA DO BOSS, AI COLOCA UM TIME SLEEP, PRA DEPOIS ELE IR VERDADEIRAMENTE PRA BATALHA, SO PRA DAR UMA TENSAOZINHA
            inimigo = criar_monstro("Demonio")

            luta_atual = Jogo(heroi, inimigo)

            luta_atual.executar()

        else:
            #COLOCA UMA MSG FALANDO QUE A SALA DO BOSS TA TRANCADA, (Dica: A chave do boss fica com seus lacaios, derrote eles para achar a chave)
            pass

    elif escolha == "3":
        heroi.verificar_personagem()

    elif escolha == "4":
        exit()

    else:
        console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida![/]", style="default")


# FAZER

# Colocar as msg da chave e as msg de entrando na sala do boss 
# colocar a opcao de ir pra sala do boss
# Na hora de printar as opcoes de personagens, coloca o level dele do lado do Nome
# A msg se ele ganhou a chave, esta na funcao verificar_fim
# fazer o negócio pra ver status do personagem
# balancear inimigos, sistema de xp, (personagens?), eu dei uma balanceada, minha ideia é, mago o mais fraco, 
# fenix um pouco mais forte, guardiao um pouco mais forte q a fenix, o demonio ser bem forte, para ele ser o boss
# ai eu fiz caso o cara seja lvl 1, ele enfrentar so o mago, lvl2 mago ou fenix, level 3 fenix ou guardiao
# Trocar o nome da opcao 1, Seguir em frente, coloca algo do tipo, Caçar monstros, ou Explorar Dungueon