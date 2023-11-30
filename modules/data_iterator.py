import modules.add_functions as af

class DataIterator:
    def __init__(self):
        self.data = af.read_data(r"C:\Users\Admin\Desktop\University\2 cours\3 semester\PP\LabAppProg\LabApplicationProgramming\datasets\dataset.csv")
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> tuple:
        if self.index < len(self.data) - 1:
            self.index += 1
            return tuple(self.data[self.index])
        raise StopIteration