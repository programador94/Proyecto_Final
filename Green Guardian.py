import discord
from discord.ext import commands
import requests
import google.generativeai as genai

# 🔑 Configura tu API key de Google AI Studio
genai.configure(api_key="TU LLAVE DE GOOGLE GEMINI")

# 🚀 Inicializa el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está encendido y listo para conversar 🤖')

# 🎲 Comando para datos curiosos
@bot.command()
async def dato(ctx):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        dato = respuesta.json()["text"]
        await ctx.send(dato)
    except Exception as e:
        await ctx.send("No se pudo obtener un dato curioso 😢")

# 🧠 Comando para preguntas
@bot.command()
async def pregunta(ctx, *, consulta):
    await ctx.send("Pensando... 🧠")
    try:
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        prompt = "Actúa como un experto en cambio climático con enfoque científico y educativo. Tu objetivo es responder únicamente preguntas relacionadas con el cambio climático y temas afines, responde en español neutro."
        
        respuesta = modelo.generate_content(f"{prompt}\n\n{consulta}")
        await ctx.send(respuesta.text)
    except Exception as e:
        await ctx.send(f"No se pudo generar respuesta con Gemini: {e}")

bot.run("TU TOQUEN DE BOT")
