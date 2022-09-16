import time, os
class CPU:
    def __init__(self, ram, delay = 1):
        self.program_counter = 0
        self.memory_address_register = 0
        self.memory_data_register = 0
        self.instruction_register = None
        self.accumulator = 0
        self.ram = ram
        self.delay = delay
    def run(self):
        while self.program_counter < len(self.ram.keys()) - 1:
            os.system('cls')
            
            self.memory_address_register = self.program_counter
            self.memory_data_register = self.ram[self.memory_address_register]
            if type(self.memory_data_register) is list:
                self.instruction_register = self.memory_data_register[0]
                address = self.memory_data_register[1]
                if self.instruction_register == 'LDA':
                    self.__LDA(address)
                
                elif self.instruction_register == 'STA':
                    self.__STA(address)
                
                elif self.instruction_register == 'ADD':
                    self.__ADD(address)
                
                elif self.instruction_register == 'SUB':
                    self.__SUB(address)
                
                elif self.instruction_register == 'OUT':
                    self.__OUT(address)
                
                elif self.instruction_register == 'BRA':
                    self.__BRA(address)

                else:
                    raise Exception("Unknown instruction")
            self.__display_registers()
            time.sleep(self.delay)            
            self.program_counter += 1        

    def __LDA(self, address):
        self.accumulator = self.ram[address]

    def __STA(self, address):
        self.ram[address] = self.accumulator
        self.accumulator = 0

    def __ADD(self, address):
        self.accumulator += self.ram[address]

    def __SUB(self, address):
        self.accumulator -= self.ram[address]

    def __OUT(self, address):
        print(self.ram[address])

    def __BRA(self, address):
        self.program_counter = address

    def __display_registers(self):
        for i in self.ram.keys():
            print(f'{i}: {self.ram[i]}')

        display_message = f"\n\n PC:{self.program_counter} \n MAR: {self.memory_address_register} \n MDR: {self.memory_data_register} \n IR: {self.instruction_register} \n ACCU: {self.accumulator}"

        print(display_message)