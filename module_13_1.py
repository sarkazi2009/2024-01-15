import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    await asyncio.gather(
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    )

if __name__ == '__main__':
    asyncio.run(start_tournament())