# pip install openai-agents
# pip install python-dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# Load Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# External client setup for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Translation dictionary (simple offline example)
translations = {
    "hello": {"spanish": "hola", "french": "bonjour", "german": "hallo"},
    "goodbye": {"spanish": "adiós", "french": "au revoir", "german": "tschüss"},
    "thank you": {"spanish": "gracias", "french": "merci", "german": "danke"},
    "love": {"spanish": "amor", "french": "amour", "german": "liebe"},
}

# Tool function for translation
@function_tool
def translate(word: str, language: str):
    word = word.lower()
    language = language.lower()
    if word in translations and language in translations[word]:
        return f"'{word}' in {language.capitalize()} is: {translations[word][language]}"
    else:
        return f"Sorry, I don’t know how to translate '{word}' into {language}."

# Translator Agent
async def main():
    agent = Agent(
        name="Translator Agent",
        instructions="You are a helpful translator agent. Use the translate tool when asked.",
        tools=[translate]
    )

    response = await Runner.run(
        agent,
        input="Translate 'hello' into Spanish.",
        run_config=config
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
