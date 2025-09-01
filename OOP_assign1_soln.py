# My Solution to Python Dev Week 5 Assignment 1 Question
# Designing a Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, battery=100):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        if self.battery > 0:
            print(f'{self.brand} {self.model} is calling {number} 📞...')
            self.battery -= 10
        else:
            print('Battery too low to make a call!')

    def install_app(self, app_name):
        if self.storage != '0':
            print(f'{app_name} installed on {self.model}.')
        else:
            print('Insufficient Storage Space!')

    def battery_status(self):
        if (self.battery != 0):
            print(f'Battery at {self.battery}')
        else:
            print('Battery Dead!')
        
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f'{self.brand} {self.model} charged to {self.battery}% 🔋')

# Inheritance at work!
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system=True):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 20:
            print(f'{self.brand} {self.model} is playing {game} 🎮...')
            self.battery -= 20
        else:
            print('Battery too low to play games!')

# Quick Demo
if __name__ == '__main__':
    phone1 = Smartphone('Samsung', 'Galaxy S23', '256GB', 85)
    phone1.make_call('08012345678')
    phone1.install_app('WhatsApp')
    phone1.battery_status()
    phone1.charge(20)

    gamer_phone = GamingSmartphone('Asus', 'ROG Phone 7', '512GB', 90)
    gamer_phone.play_game('PUBG Mobile')
    gamer_phone.make_call('09098765432')