class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu == value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory == value

    def make_computations(self):
        return (self.__cpu + self.__memory)

    def __str__(self):
        return f'Cpu: {self.cpu} Memory: {self.memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value: list):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер "{call_to_number}" с сим-карты №{sim_card_number}-'
            f'{self.__sim_cards_list[sim_card_number]}')

    def __str__(self):
        return f'Sim-Card list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        print(f'Построен маршрут до {location}: (3, 10) km')

    def __str__(self):
        return Computer.__str__(self) + ' ' + Phone.__str__(self)


hp = Computer(10080, 980)
nokia = Phone(['MegaCom'])
samsung = SmartPhone(9800, 512, ['MegaCom', 'O!'])
iphone = SmartPhone(12000, 128, ['Beeline'])
print(hp)
print(nokia)
print(samsung)
print(iphone)

print('Make Computation:', hp.make_computations())
samsung.call(0, '+996708869616')

iphone.use_gps('БЦ Victory')

print('Сравнение:')
print(hp > samsung)
print(iphone < samsung)
print(hp >= iphone)
print(samsung <= hp)
print(samsung == hp)
print(samsung != iphone)