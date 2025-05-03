import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(['start', 'help'])
def start(msg: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup()

    botao_sobre = types.KeyboardButton('Sobre')
    botao_ola = types.KeyboardButton('Olá')
    botao_jogadores = types.KeyboardButton('Jogadores')
    botao_resultados = types.KeyboardButton('Resultados')
    botao_jogos = types.KeyboardButton('Próximos Jogos')
    botao_estatisticas = types.KeyboardButton('Estatísticas')
    botao_noticias = types.KeyboardButton('Notícias')
    botao_comunidade = types.KeyboardButton('Comunidade')

    markup.add(botao_ola, botao_jogadores, botao_resultados, botao_jogos, botao_estatisticas, botao_noticias, botao_comunidade, botao_sobre)

    bot.send_message(msg.chat.id, 'Bem vindo(a) ao Fan Chat da Furia!' ,reply_markup=markup)

@bot.message_handler()
def resposta_botao(msg:types.Message):
    match msg.text:
        case 'Olá':
            bot.send_message(msg.chat.id, "Olá Furioso(a)! \nEssas são as funções que posso desempenhar atualmente: \n- Jogadores: Lista de Jogadores da Furia \n- Resultados: Últimos resultados do time de CS da Furia \n- Próximos Jogos: Lista dos próximos jogos do time de CS da Furia \n- Estatísticas: As estatísticas de cada jogador do time de CS da Furia \n- Notícias: Últimas notícias do time de CS da Furia \n- Comunidade: Seção onde você pode interagir com outros fans da Furia \nO você que quer fazer?")
        case 'Jogadores':
            bot.send_message(msg.chat.id, "Se quer mais informações sobre os jogadores da Furia, clica nesse link e você vai ser redirecionado para a landing page com as informações de cada um:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#jogadores")
        case 'Resultados':
            bot.send_message(msg.chat.id, "Se quer ver os últimos resultados do time da Furia, clica nesse link e você vai ser redirecionado para a landing page com os últimos resultados:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#resultados")
        case 'Próximos Jogos':
            bot.send_message(msg.chat.id, "Se quer saber quais e quando serão os próximos jogos da Furia, clica nesse link e você vai ser redirecionado para a landing page com as informações dos nossos próximos jogos:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#jogos")
        case 'Estatísticas':
            bot.send_message(msg.chat.id, "Se você quer ver as estatísticas dos nossos jogadores, clica nesse link e você vai ser redirecionado para a landing page com as estatísticas de cada jogador da Furia:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#estatisticas")
        case 'Notícias':
            bot.send_message(msg.chat.id, "Se você quer ver as últimas notícias sobre a Furia, clica nesse link e você vai ser redirecionado para a landing page com notícias exclusivas:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#noticias")
        case 'Comunidade':
            bot.send_message(msg.chat.id, "Se você quer interagir com a comunidade de fans da Furia, clica nesse link e você vai ser redirecionado para a seção de comentários da landing page, onde pode interagir com outros players:\nhttps://pedrorsilveira.github.io/landing-page-desafio-furia/#comentarios")
        case 'Sobre':
            bot.send_message(msg.chat.id, "Esse bot foi criado para o desafio da FURIA para Assistente de Engenharia de Software!")
@bot.message_handler(['olá'])
def ola(msg: telebot.types.Message):
    bot.reply_to(msg, 'Olá Furioso(a)! O que quer fazer?')

bot.infinity_polling()