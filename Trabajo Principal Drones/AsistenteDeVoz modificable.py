import pyttsx3 
import webbrowser
import speech_recognition as sr



escuchar = sr.Recognizer()
apBot = pyttsx3.init()


def grabar():
    with sr.Microphone() as source:
        print("Deci algo")
        audio = escuchar.listen(source)
        voice_data = escuchar.recognize_google(audio, language='es-ES')
        return voice_data
        

def responder( voice_data ):
    if "nombre" in voice_data:   
         
        apBot.say("Mi nombre es Ap Bot")
        apBot.runAndWait()

    if "navegar" in voice_data:
        apBot.say("¿Que desea buscar?")
        apBot.runAndWait()
        busqueda = grabar()
        url = "https://google.com.ar/search?q="+ busqueda
        webbrowser.open_new( url )
        print("Esto es lo que encontre: " + busqueda)
    

    if "mapa" in voice_data:
        apBot.say("¿Donde quiere ir?")
        apBot.runAndWait()
        busqueda = grabar()
        url = 'https://google.com.ar/maps/place/' + busqueda + "/&amp"
        webbrowser.get().open(url)
        print("Esto es lo que encontre: " + busqueda)





    if "salir" in voice_data:
        apBot.say("Nos vemos, vuelve pronto")
        apBot.runAndWait()
        exit()



apBot.say("¿En que puedo ayudarte?")
apBot.runAndWait()

grabacion = grabar()
responder( grabacion ) 
