# translator_agent.py

class TranslatorAgent:
    def __init__(self):
        # Small demo dictionary for translations
        self.dictionary = {
            "hello": {"spanish": "hola", "french": "bonjour", "german": "hallo"},
            "goodbye": {"spanish": "adiós", "french": "au revoir", "german": "tschüss"},
            "thank you": {"spanish": "gracias", "french": "merci", "german": "danke"},
            "love": {"spanish": "amor", "french": "amour", "german": "liebe"},
        }

    def translate(self, word, language):
        word = word.lower()
        language = language.lower()
        if word in self.dictionary and language in self.dictionary[word]:
            return f"🔤 '{word}' in {language.capitalize()} is: {self.dictionary[word][language]}"
        else:
            return f"❓ Sorry, I don't know how to translate '{word}' into {language}."


# Run demo
if __name__ == "__main__":
    agent = TranslatorAgent()

    print(agent.translate("hello", "spanish"))
    print(agent.translate("thank you", "french"))
    print(agent.translate("love", "german"))
    print(agent.translate("sun", "spanish"))
