from FileHandler import load_history, load_saldo_and_magazyn, save_saldo_and_magazyn_to_file, save_history

class Manager():

    def __init__(self, history_file, magazyn_and_saldo_file):
        self.history_file = history_file
        self.magazyn_and_saldo_file = magazyn_and_saldo_file
        self.history = load_history(history_file)
        self.saldo, self.magazyn = load_saldo_and_magazyn(magazyn_and_saldo_file)
        self.actions = {}

    def assign(self, name):
        def wrapper(function):
            self.actions[name] = function
        return wrapper

    def execute(self, name):
        if not name in self.actions:
            print("Niestety nie ma takiej akcji")
        else:
            self.actions[name](self)