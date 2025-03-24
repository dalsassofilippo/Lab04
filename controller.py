import time
import flet as ft
import model as md
from view import View

class SpellChecker:

    def __init__(self, v: View):
        self._multiDic = md.MultiDictionary()
        self._view = v

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate += str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate += str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate +=str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self,e):
        # Controllo se tutti i campi sono stati selezionati
        if self._view._menuLanguage.value is None:
            self._view._messageTxt.value = "Errore: seleziona una lingua!"
            self._view._messageTxt.color = "red"
            self._view.page.update()
            return
        elif self._view._menuModality.value is None:
            self._view._messageTxt.value = "Errore: seleziona un tipo di ricerca!"
            self._view._messageTxt.color = "red"
            self._view.page.update()
            return
        elif self._view._menuSentence.value.strip()=="":
            self._view._messageTxt.value = "Errore: inserisci un testo da correggere!"
            self._view._messageTxt.color = "red"
            self._view.page.update()
            return
        else:
            # Tutti i campi sono validi, esegui la correzione ortografica
            incorrect_words, elapsed_time = self.handleSentence(
                self._view._menuSentence.value,self._view._menuLanguage.value, self._view._menuModality.value
            )
            # Mostra i risultati nella ListView
            self._view._txtOut.controls.append(ft.Text(f"Testo inserito: {self._view._menuSentence.value}"))
            self._view._txtOut.controls.append(
                ft.Text(f"Parole errate: {incorrect_words if incorrect_words else 'Nessun errore'}"))
            self._view._txtOut.controls.append(ft.Text(f"Tempo di ricerca: {elapsed_time:.4f} sec"))
            self._view._txtOut.controls.append(ft.Text(value="-------------------------------------------"))

            # Svuota il campo di input
            self._view._menuSentence.value = ""

            self._view._messageTxt.value = "Correzione completata!"
            self._view._messageTxt.color = "green"

        self._view.page.update()

    def handleLanguageSelection(self,e):
        if self._view._menuLanguage.value!="":
            self._view._messageTxt.value=f"Lingua selezionata: {self._view._menuLanguage.value}"
            self._view._messageTxt.color="green"
        else:
            self._view._messageTxt.value = "Errore: seleziona una lingua!"
            self._view._messageTxt.color = "red"
            self._view.page.update()
            return
        self._view.page.update()

    def handleModalitySelection(self,e):
        if self._view._menuModality.value!="":
            self._view._messageTxt.value=f"Modalità selezionata: {self._view._menuModality.value}"
            self._view._messageTxt.color="green"
        else:
            self._view._messageTxt.value = "Errore: seleziona una modalità!"
            self._view._messageTxt.color = "red"
            self._view.page.update()
            return
        self._view.page.update()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text