meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "PPRT": "Abreviação da sigla papo reto",
            "67": "Piada sem graça da internet, ocorrida quando o indivídua observa o número 67",
            "TCHÊ TCHÊ": "técnica geralmente falha usada por humens para tentar conquistar em sua maioria mulheres, consiste em repetir tchê tchê",
            "FARMAR AURA": "Fazer algo maneiro, geralmente isto também é usado por pessoas com menos de 9 anos",
            "SS": "Abreviação da palavra sim",
            "ROBLOX": "Plataforma de jogos jogada em sua maioria por crianças e adolescentes",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('eu não achei')
