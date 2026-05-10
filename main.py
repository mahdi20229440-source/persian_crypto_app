from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


alphabet = {
    "a":"01","b":"02","c":"03","d":"04","e":"05","f":"06","g":"07","h":"08","i":"09",
    "j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18",
    "s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26",
    " ": "27", ".": "28", ",": "29", "!": "30", "?": "31", "-": "32", ":": "33", ";": "34"
}

reverse_alphabet = {v: k for k, v in alphabet.items()}


def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch in alphabet:
            result += alphabet[ch]
    return result


def decrypt(code):
    result = ""
    for i in range(0, len(code), 2):
        part = code[i:i+2]
        if part in reverse_alphabet:
            result += reverse_alphabet[part]
    return result


class MenuScreen(Screen):
    def on_kv_post(self, *args):
        Clock.schedule_once(self.setup_texts, 0)

    def setup_texts(self, dt):
        self.ids.title_label.text = "Simple Encryptor"
        self.ids.encrypt_btn.text = "Encrypt"
        self.ids.decrypt_btn.text = "Decrypt"
        self.ids.exit_btn.text = "Exit"


class EncryptScreen(Screen):
    def on_kv_post(self, *args):
        Clock.schedule_once(self.setup_texts, 0)

    def setup_texts(self, dt):
        self.ids.input_text.hint_text = "Enter text to encrypt"
        self.ids.encrypt_button.text = "Encrypt"
        self.ids.back_button.text = "Back"

    def do_encrypt(self):
        self.ids.output_code.text = encrypt(self.ids.input_text.text)


class DecryptScreen(Screen):
    def on_kv_post(self, *args):
        Clock.schedule_once(self.setup_texts, 0)

    def setup_texts(self, dt):
        self.ids.input_code.hint_text = "Paste numeric code here"
        self.ids.decrypt_button.text = "Decrypt"
        self.ids.back_button.text = "Back"

    def do_decrypt(self):
        self.ids.output_text.text = decrypt(self.ids.input_code.text)


class CryptoManager(ScreenManager):
    pass


Builder.load_file("crypto.kv")


class CryptoApp(App):
    def build(self):
        return CryptoManager()


if __name__ == "__main__":
    CryptoApp().run()
