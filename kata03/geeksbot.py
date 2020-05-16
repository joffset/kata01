from telegram.ext import Updater


def main():
    # instanciamos el updater
    updater =  Updater(token="")
    
    # empezamos a pedir notificaciones a telegram
    updater.start_polling()
    
    # capturamos señales telegram
    updater.idle()


main()