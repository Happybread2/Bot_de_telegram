from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TOKEN")
USER_ID = int(os.getenv("USER_ID"))       # ID de Telegram
USER_WINDOWS = os.getenv("USER_WINDOWS")  # Usuario de Windows con permisos
PASS_WINDOWS = os.getenv("PASS_WINDOWS")  # Contraseña del usuario de Windows
IP_WINDOWS = os.getenv("IP_WINDOWS")      # IP del PC Windows


async def mi_id(update, context):
    await update.message.reply_text(f"Tu ID es: {update.effective_user.id}")

async def start(update, context):
    await update.message.reply_text(
        "Hola, el bot está activo.\nUsa /comandos para ver los comandos disponibles."
    )

async def comandos(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text(
            "/apagar - Apagar la PC Windows\n"
            "/reiniciar - Reiniciar la PC Windows\n"
            "/id - Ver tu ID"
        )
    else:
        await update.message.reply_text("No tienes permiso para usar los comandos.")

async def apagar(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Apagando la PC Windows en 3 segundos...")
        cmd = f'net rpc shutdown -I {IP_WINDOWS} -U {USER_WINDOWS}%{PASS_WINDOWS} -t 3'
        os.system(cmd)
    else:
        await update.message.reply_text("No tienes permiso.")

async def reiniciar(update, context):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Reiniciando la PC Windows en 3 segundos...")
        cmd = f'net rpc shutdown -r -I {IP_WINDOWS} -U {USER_WINDOWS}%{PASS_WINDOWS} -t 3'
        os.system(cmd)
    else:
        await update.message.reply_text("No tienes permiso.")

# -------------------- Función principal -------------------- #
def main():
    app = Application.builder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("id", mi_id))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CommandHandler("apagar", apagar))
    app.add_handler(CommandHandler("reiniciar", reiniciar))

    # Ejecutar bot
    app.run_polling()

if __name__ == "__main__":
    main()
