# mad libs mini game thing
import discord

@client.event
async def on_message():
    
    # give message
    # define check
    # await user input
    # store user input

    
    if message.content.startswith('/madlib'):
        channel = message.channel
        await channel.send('Welcome to mab libs! You will be asked to give a number of nouns, adjectives, verbs, and more. At the end, everything you pick will be put together into a customized story. Press (x) to continue. Enter quit at any time to stop.')
        storeInp = []

        def check(m):
            return m.content == 'x'

        m = await client.wait_for('message', check=check)
        # got user input showing to start.
        await message.channel.send('Enter an adjective.')

        def check(m):
            return m.content != 'quit'
        
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter an adjective.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a number.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            

        await message.channel.send('Enter a honorific.')  # ???
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a name.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb ending in -ing.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a singular noun.')  # or change to body part
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a number.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send(f'Just another {storeInp[0]} day as i {storeInp[1]} at my computer. Yet again my {storeInp[2]} refused to work. It should be {storeInp[3]}, but no, my {storeInp[4]} never wants to {storeInp[5]}. Even after {storeInp[6]} hours, I still keep getting {storeInp[7]} errors. My teacher, {storeInp[8]} {storeInp[9]} said I just need to {storeInp[10]} but my code still keeps {storeInp[11]}. I am about to {storeInp[12]} my {storeInp[13]} {storeInp[14]} if it doesn\'t work after {storeInp[15]} more tries.')

