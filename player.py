class Player:
    def __init__(self, name, capital, property, technology1, technology2, technology3, 
                 audience, experts, influencer, teacher, course=0, mentorship=0, simple=0, complex=0):
        self.name = name
        self.capital = capital
        self.property = property
        self.technology1 = technology1
        self.technology2 = technology2
        self.technology3 = technology3
        self.experts = experts
        self.influencer = influencer
        self.audience = audience
        self.teacher = teacher
        self.course = course
        self.mentorship = mentorship
        self.simple = simple
        self.complex = complex

    def transfer_money(self, amount, to):
        if self.capital < amount:
            return 'Недостаточно средств'
        else: 
            self.capital-=amount
            to.capital+=amount
            return f'Перевод выполнен. Ваш баланс {self.capital} у.е.'
    
    def check_capital(self):
        ans = f'Баланс {self.capital} у.е.\n\nТехнологии:\n'
        if self.technology1: ans+='Автоматизация производства продукта\n'
        if self.technology2: ans+='Предиктивная аналитика\n'
        if self.technology3: ans+='Замена экспертов на ИИ\n'
        ans+='Имущество:\n'
        if self.course==1:
            ans+='Один курс\n'
        if self.course>1:
            ans+=f'{self.course} курса\n'
        if self.mentorship>0:
            ans+='Одно наставничество\n'
        if self.simple==1:
            ans+='Один простой продукт\n'
        if self.simple>1:
            ans+=f'{self.simple} простых продукта\n'
        if self.complex==1:
            ans+='Один сложный продукт\n'
        if self.complex>1:
            ans+=f'{self.complex} сложных продукта\n\n'
        if self.experts>0:
            ans+=f'{self.experts} свободных команд экспертов для создания сложных продуктов\n\n'
        if self.influencer == True:
            ans+=f'Личная аудитория {self.audience} человек\n'
        if len(self.property) > 3:
            ans+= f'Другое имущество: {self.property}\n\n'
        return ans
    
class IT (Player):
    def __init__(self, name, capital, property, technology1, technology2, technology3, audience, influencer,
                  teacher, experts, course=0, mentorship=0, simple=0, complex=0):
        super().__init__(name, capital, property, technology1, technology2, technology3, audience, influencer, 
                         teacher, experts, course=0, mentorship=0, simple=0, complex=0)
    def install(self, company, technology):
        if technology == '1':
            company.technology1 = True
        elif technology == '2':
            company.technology2 = True
        elif technology == '3':
            company.technology3 = True
        else:
            company.property+=', '
            company.property+=technology
        return f'Технология {technology} внедрена {company}'