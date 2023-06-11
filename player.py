class Player:
    def __init__(self, name, capital, property, technology1, technology2, technology3, audience, platform, influencer):
        self.name = name
        self.capital = capital
        self.property = property
        self.technology1 = technology1
        self.technology2 = technology2
        self.technology3 = technology3
        self.platform = platform
        self.influencer = influencer
        self.audience = audience

    def transfer_money(self, amount, to):
        if self.capital < amount:
            return 'Недостаточно средств'
        else: 
            self.capital-=amount
            to.capital+=amount
            return f'Перевод выполнен. Ваш баланс {self.capital} у.е.'
    
    def check_capital(self):
        ans = f'Ваш баланс {self.capital} у.е.'
        return ans
    
class Bank (Player):
    def __init__(self, name, capital, property, technology1, technology2, technology3, audience, platform, influencer):
        super().__init__(name, capital, property, technology1, technology2, technology3, audience, platform, influencer)

class IT (Player):
    def __init__(self, name, capital, property, technology1, technology2, technology3, audience, platform, influencer):
        super().__init__(name, capital, property, technology1, technology2, technology3, audience, platform, influencer)
    def install(self, company, technology):
        if technology == '1':
            company.technology1 = True
        elif technology == '2':
            company.technology2 = True
        elif technology == '3':
            company.technology3 = True
        company.property+=', '
        company.property+=technology