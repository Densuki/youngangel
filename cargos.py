# ===================================================
#EXPORT
# ===================================================
def cargos_roles();
# ===================================================
#CARGOS
# ===================================================
@client.event
async def on_message(message): #Condição

    if message.content.lower().startswith('#cargos'):  #BASE PARA CARGOS
     if message.author.id == "286206456108154880":  # permissão por ID [EU]
      embed1 = discord.Embed(
        title="**Cargos Superiores**\n "
              ,
        color=COR,
        description="Escolha o cargo que será proposto!\n"
                    "- Fundador = ⚡🌌⚡\n"
                    "- Dono(a)  =  ⭐⭐ \n"
                    "- adm  = ⭐ \n" 
                    "- Bomber Rank S  = ⚜🔰 \n"
                    "- Bomber Rank A  = 🔧 \n"
                    "- Bomber Rank B  = 🛠 \n"
                    "- Bomber Rank C  = 🔨",)

     botmsg = await client.send_message(message.channel, embed=embed1)

     await client.add_reaction(botmsg, "🌌")
     await client.add_reaction(botmsg, "⚡")
     await client.add_reaction(botmsg, "⭐")
     await client.add_reaction(botmsg, "⚜")
     await client.add_reaction(botmsg, "🔧")
     await client.add_reaction(botmsg, "🛠")
     await client.add_reaction(botmsg, "🔨")


     global msg_id
     msg_id = botmsg.id

     global msg_user
     msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🌌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🌀⚡Fundador🌀⚡", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "⭐⭐Dono(a)⭐⭐", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⭐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "adm", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank S", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank A", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank B", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank C", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🌌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "🌀⚡Fundador🌀⚡", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "⭐⭐Dono(a)⭐⭐", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⭐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "adm", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚜" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank S", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔧" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank A", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🛠" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank B", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔨" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bomber Rank C", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")
# ===================================================
#
# ===================================================
