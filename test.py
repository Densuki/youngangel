# ===================================================
# IMPORT'S
# ===================================================

import discord
import asyncio
import secreto

# ----------------------------------------------------

# ----------------------------------------------------

# ===================================================
client = discord.Client()
# ===================================================
COR = 0x690FC3

msg_id = None
msg_user = None

# ===================================================
# IDENTIDADE PELO CONSOLE
# ===================================================

# ===================================================
# TEST
# ===================================================
def test():
    return ""
# ===================================================
# LOOP BREAK
# ===================================================

@client.event
async def on_message(text):
    if text.author.id == '451510020614389761': return # Berserker Debug

# ===================================================
# MODELO PARA COMANDOS
# ===================================================

@client.event
async def on_message(message):  # Condição
    if message.content.lower().startswith('fala'):  # PREFIX DO COMANDO (Deste, no caso)
        await client.send_message(message.channel,
                                  "**Estar tudo certo!**")  # Mensagem como resultado
