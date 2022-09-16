import sys, os

from cpu import CPU

def add_data(address, ram):
    if address in ram.keys():
        data = input(f'{address}: ')
        if data == '':
            data = None
        elif data.isdigit():
            data = int(data)
        else:
            data = data.split(' ')
            data[1] = int(data[1])
        ram[address] = data
    else:
        print('invalid address')

def print_ram(ram):
    for i in ram.keys():
        print(f'{i}: {ram[i]}')

def create_ram(MEMORY_ADDRESSES, ram):
    for i in range(MEMORY_ADDRESSES):
        ram[i] = None

MESSAGE = """
1) ram mode
2) execute mode
h) help
q) quit
"""
HELP_MESSAGE = """
ram mode:
type in the address to edit it
then enter the data.
then the program will automatically adjust the types for you.
execute mode:
after finishing editing the ram, use execute mode by entering 2 on the input box, then the screen will automatically clear.
you can choose a time delay, to watch the changes to the ram and the cpu
then the information from the ram and the cpu will be displayed onto the screen with the delay of your specified time. 
"""

MEMORY_ADDRESSES = 10

ram = {}
create_ram(MEMORY_ADDRESSES, ram)
while True:
    print(MESSAGE)
    answer = input('> ')

    if answer == '1':
        while True:
            address = input('enter memory address (q to quit, p to display ram): ')

        
            if address == 'q':
                break
            if address == 'p':
                os.system('cls')
                print_ram(ram)
                continue
            
            if not address.isdigit():
                print('invalid address')
                
            add_data(int(address), ram)

    if answer == '2':
        while True:
            try:
                delay = int(input('enter delay(seconds): '))
                break
            except:
                print('try again')
        cpu = CPU(ram, delay)
        cpu.run()

    if answer == 'q':
        sys.exit()

    if answer == 'h':
        print(HELP_MESSAGE)