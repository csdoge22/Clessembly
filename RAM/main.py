class RAM:
    def __init__(self, latency, transfer_rate, capacity=160):
        self.__capacity = capacity
        self.__memory = self.populate_memory()
        self.__latency = latency
        self.__transfer_rate = transfer_rate
    
    def populate_memory(self):
        for i in range(self.capacity):
            self.memory[hex(i)] = None
    
    def modify_slot(self, hex, content):
        self.memory[hex] = content

