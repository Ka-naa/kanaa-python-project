import random

while True:
    start = int(input('Start(1) or Stop(0) : '))
    print()

    if start != 1 and start != 0:
        print('Input no valid!')
    else:
        if start == 1:
            print('Game Start! \n')

            playerPotition = 0
            botPotition = 0
            while True:
                walk = int(input('Walk(1) or Return(0) : '))
                print()
                if walk != 1 and walk != 0:
                    print('Input not valid!')
                else:
                    if walk == 1:
                        playerStep = random.randint(1,6)
                        playerPotition += playerStep

                        if playerPotition > 30:
                            playerPotition = 30-(playerPotition-30)
                            print(f'Your potition: {playerPotition}')
                        else:
                            print(f'Your potition: {playerPotition}')

                        botStep = random.randint(1,6)
                        botPotition += botStep

                        if botPotition > 30:
                            botPotition = 30-(botPotition-30)
                            print(f'Bot potition: {botPotition}')
                            print()
                        else:
                            print(f'Bot potition: {botPotition}')
                            print()

                        if playerPotition == 30:
                            print('You Win!')
                            print()
                            break
                        elif botPotition == 30:
                            print('You Lose!')
                            print()
                            break
                        
                    elif walk == 0:
                        break
                
        elif start == 0:
            break
