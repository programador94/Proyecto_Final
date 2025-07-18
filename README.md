# Proyecto_Final
🤖 Bot Discord de Datos Curiosos y Preguntas sobre el Cambio Climático
Este bot está diseñado para ofrecer datos curiosos en español y responder preguntas especializadas sobre el cambio climático usando inteligencia artificial. Integrando las bibliotecas discord.py, requests y google.generativeai, combina entretenimiento y educación en un solo asistente conversacional.
🚀 Funcionalidades principales
- !dato — Obtiene un dato curioso aleatorio desde una API pública en español.
- !pregunta [consulta] — Responde preguntas exclusivamente sobre cambio climático utilizando el modelo Gemini 1.5 Flash de Google AI.
⚠️ Si la consulta no está relacionada con el cambio climático, el bot lo indicará explícitamente y no responderá.

🛠️ Requisitos
- Python 3.8+
- Discord Bot Token
- API key de Google Generative AI
- Dependencias: discord, requests, google-generativeai
🧠 Características técnicas
- Usa discord.ext.commands para gestionar los comandos.
- Configura los permisos necesarios con Intents.
- Accede a Gemini para generar contenido especializado con contexto enfocado.
- Manejo de errores para respuestas fallidas o fuera de contexto.
