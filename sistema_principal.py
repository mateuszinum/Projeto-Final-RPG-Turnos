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
        mensagem += f"\n[bold plum1]{i}[/] - {personagem.nome}\n"
        mensagem += f"{" " * 4}[bold bright_green]Vida: {personagem.vida_max}[/] | [bold red1]Ataque: {personagem.ataque}[/] | [bold bright_yellow]Defesa: {personagem.defesa_inicial}[/] | [bold dodger_blue2]Velocidade: {personagem.velocidade}[/]\n"
        mensagem += f"{" " * 4}[bold]Arma: [bold red1]Dano {personagem.arma.dano}[/] ([bold orange1]Crítico: {personagem.arma.critico}%[/])\n"
    
    console.print(Panel.fit(mensagem, title="[bold medium_orchid]Escolha sua Classe", border_style="medium_orchid", style="default"))

    while True:
        escolha = console.input(f"\n\n\n{' ' * 20}[bold grey82]Escolha sua classe (1-{len(personagens)}): ")
        
        if escolha in ["1", "2", "3", "4"]:
            personagem_escolhido = personagens[int(escolha)-1]
            console.print(f"\n\n\n{' ' * 20}Você escolheu o [bold orange1]{personagem_escolhido.nome}[/]!", style="default")
            return personagem_escolhido
        else:
            console.print(f"\n\n\n{' ' * 20}[bold red1]Opção inválida! Escolha de 1 a 4", style="default")


personagem = selecionar_classe()


while True:
    console.print(f"\n\n\n{' ' * 20}O que você deseja fazer?", style="default")
    console.print(f"\n{' ' * 20}([bold plum1]1[/]) - Seguir em frente\n{' ' * 20}([bold plum1]2[/]) - Ver status\n{' ' * 20}([bold plum1]3[/]) - Testes\n{' ' * 20}([bold plum1]4[/]) - Sair do jogo", style="default")
    
    escolha = console.input(f"\n{' ' * 20}[bold grey82]Escolha uma opção: ")
    
    if escolha == "1":

        inimigo = mago

        luta_atual = Jogo(personagem, inimigo)

        luta_atual.executar()


        pass

    elif escolha == "2":
        pass

    elif escolha == "3": # Teste de todas as animações
        menu_teste = (
            f"\n\n\n{' ' * 20}(1) - Animação ataque personagem"
            f"\n{' ' * 20}(2) - Animação ataque inimigo"
            f"\n{' ' * 20}(3) - Animação personagem atingido"
            f"\n{' ' * 20}(4) - Animação monstro atingido"
        )
        console.print(Panel.fit(menu_teste))
        inimigo = mago
        escolha = console.input(f"\n{' ' * 20}[bold grey82]Qual cena rodar? ")
        if escolha == "1":
            cena.avanco_personagem(personagem, inimigo)

        elif escolha == "2":
            cena.ataque_monstro(personagem, inimigo)

        elif escolha == "3":
            cena.personagem_atingido(personagem, inimigo)

        elif escolha == "4":
            cena.monstro_atingido(personagem, inimigo)
        
        elif escolha == "5":
            cena.esquiva_personagem(personagem, inimigo)

    elif escolha == "4":
        exit()
    else:
        console.print(f"\n{' ' * 20}[bold red1]Opção inválida![/]", style="default")


# FAZER


# mudar as cores do personage, borda, etc pra ficar bonito
# por algum motivo algumas opções demoram para responder
# esquiva não funciona as vezes
# quando vai pro próximo inimigo, ele tá com a vida do antigo
# fazer a vida do inimigo não descer de 0
# botar menos pontos pra upar e diminuir quanto cada atributo recebe, mt forte