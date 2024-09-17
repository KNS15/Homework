import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball_number in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball_number} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    tasks1 = asyncio.create_task(start_strongman('Паша', 3))
    tasks2 = asyncio.create_task(start_strongman('Денис', 4))
    tasks3 = asyncio.create_task(start_strongman('Аполлон', 5))

    await tasks1
    await tasks2
    await tasks3

asyncio.run(start_tournament())