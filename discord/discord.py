#================================ Discord ================================



token_chuj = os.getenv('token') 
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)


@client.command(pass_context=True)
async def h(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Help === \n !w - Zużycie wody \n !ws - Aktualny stan licznika \n !p - Zużycie pompy ")


@client.command(pass_context=True)
async def ws(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"Aktualny stan licznika - {stan_licznika()}")



@client.command(pass_context=True)
async def w(ctx):
    channel = client.get_channel(1021783221475754057)
    #await channel.send(f"=== Zużycie Wody === \n Dzisiaj: {woda_dzisiaj()} \n Wczoraj: {water_per_day()['dzien1']}  \n 2-dni: {water_per_day()['dzien2']} \n 3-dni: {water_per_day()['dzien3']} \n 4-dni: {water_per_day()['dzien4']} \n 5-dni: {water_per_day()['dzien5']} \n 6-dni: {water_per_day()['dzien6']} \n ")
    await channel.send(f"Nie ma :( ")

@client.command(pass_context=True)
async def p(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Zużycie Pompy === \n Dzisiaj: {pompa_dzisiaj()} \n Wczoraj: {pump_per_day()['dzien1']}  \n 2-dni: {pump_per_day()['dzien2']} \n 3-dni: {pump_per_day()['dzien3']} \n 4-dni: {pump_per_day()['dzien4']} \n 5-dni: {pump_per_day()['dzien5']} \n 6-dni: {pump_per_day()['dzien6']} \n ")




@client.command(pass_context=True)
async def kurwa(ctx):
    channel = client.get_channel(1017555311365722246)
    await channel.send('test')

client.run(token_chuj)