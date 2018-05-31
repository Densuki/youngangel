# ===================================================
# IMPORT'S
# ===================================================

import discord
import asyncio
import youngangel
import secreto

# ----------------------------------------------------

# ----------------------------------------------------

# ===================================================
client = discord.Client()
# ===================================================
COR = 0x690FC3
Token = secreto.seu_token()
msg_id = None
msg_user = None

# ===================================================
# IDENTIDADE PELO CONSOLE
# ===================================================

@client.event
async def on_ready():
    print('===================================================')
    print('BOT ONLINE: - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('===================================================')
    print('Version - 1.2')
    print('===================================================')


# ===================================================
# TEST
# ===================================================

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
