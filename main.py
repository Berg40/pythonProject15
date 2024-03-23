import telebot

CHAVE_API = "6316535518:AAESLamccY3xVUe8f0o4swtYOZuB7IojBa8"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pacote1"])
def pacote1(mensagem):
    bot.send_message(mensagem.chat.id, "Valor R$240,00 Por mês")

@bot.message_handler(commands=["pacote2"])
def pacote2(mensagem):
    bot.send_message(mensagem.chat.id, "Valor R$450,00 Por mês")

@bot.message_handler(commands=["pacote3"])
def pacote3(mensagem):
    bot.send_message(mensagem.chat.id, "Valor R$680,00 Por mês")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Valor de investimento (Clique na opção):
    /pacote1 Uma vez na semana
    /pacote2 Duas vezes na semana
    /pacote3 Três vezes na semana
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "O Muay Thai é uma arte marcial tailandesa que combina golpes de punho, cotovelos, joelhos, pernas e técnicas de clinch. Seus benefícios para a saúde incluem melhora da aptidão cardiovascular, fortalecimento muscular, aumento da flexibilidade, coordenação e reflexos. Durante uma aula de Muay Thai intensa, é possível perder até 600-800 calorias, dependendo do peso corporal e da intensidade do treino.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link do WhatsApp e informe o pacote escolhido, nome e disponibilidade de horário e dias para o treino: [aqui](https://api.whatsapp.com/send?phone=5512997071992&text=Agendamentos%20de%20aulas%20de%20Muay%20Thai)")

def verificar(mensagem):
    return True  # Esta função faz com que o bot responda a qualquer mensagem

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá, tudo bem? Clique em uma opção para continuar (clique no item):
    /opcao1 Saber mais sobre o Muay Thai
    /opcao2 Saber sobre os valores do personal de Muay Thai
    /opcao3 Agendamento de aulas
    """
    bot.reply_to(mensagem, texto)

bot.polling()


