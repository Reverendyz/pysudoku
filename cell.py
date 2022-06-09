#/usr/bin/python3.10

class Cell:
    def __init__(self) -> None:
        self.number = None
        self.neighbors = []

    def associate_number(self, number):
        self.number = number
        return

    def __get_neighbors(self):
        return self.neighbors
    
    def check_neighbors(self):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        neighbors = self.__get_neighbors()
        return