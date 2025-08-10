import os
import telebot

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Проверка: если токен не найден — не запускаем
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в переменных окружения!")

bot = telebot.TeleBot(TOKEN)

# Пример простой команды
@bot.message_handler(commands=["start", "help"])
def start_handler(message):
    bot.reply_to(message, "👋 Hello! I'm your bot, ready to work!")

# Ответ на любое текстовое сообщение
@bot.message_handler(func=lambda message: True)
def echo_handler(message):
    bot.reply_to(message, f"🔁 You said: {message.text}")

# Запуск бота
if __name__ == "__main__":
    print("✅ Bot is running...")
    bot.polling(non_stop=True)
