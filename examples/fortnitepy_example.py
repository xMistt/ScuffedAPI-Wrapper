import fortnitepy
import ScuffedAPI

client = fortnitepy.Client(
    email='example@email.com',
    password='password123'
)

@client.event
async def event_friend_message(message):
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!playlist':
        playlist = await ScuffedAPI.get_playlist(name=content)
        await client.user.party.set_playlist(playlist=playlist.id)
        
client.run()
