import player

skillbox = player.Player(name = 'Skillbox', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          platform = True, influencer = False)
entspace = player.Player(name = 'Entspace', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          platform = True, influencer = False)
skolkovo = player.Player(name = 'Skolkovo', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          platform = True, influencer = False)
like = player.Player(name = 'Like центр', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          platform = True, influencer = False)
couch = player.Player(name = 'Коуч', capital = 100, property = '', technology1=False,
                      technology2=False, technology3=False, audience=50, platform = False, influencer = True) #50
mentor = player.Player(name = 'Наставник', capital = 100, property = '', technology1=False,
                      technology2=False, technology3=False, audience=50, platform = False, influencer = True)
expert = player.Player(name = 'Эксперт', capital = 100, property = '', technology1=False,
                      technology2=False, technology3=False, audience=50, platform = False, influencer = True)
soe = player.Player(name = 'School of Education', capital = 100, property = '', 
                    technology1=False, technology2=False, technology3=False, audience= 0, influencer=False, platform=True) #50   develop 150
smart = player.IT(name = 'Smart Lab', capital=100, property='',
                  technology1= False, technology2=False, technology3=False, audience=0, platform=False, influencer=False) #50  develop 100
bank = player.Bank(name = 'Тинькофф', capital=800, property='',
                  technology1= False, technology2=False, technology3=False, audience=0, platform=False, influencer=False)
investor = player.Player(name = 'Российская Инвестиционная Компания', capital=700, property='',
                  technology1=False, technology2=False, technology3=False, audience=0, platform=False, influencer=False)

add1 = player.Player(name = 'Новая компания', capital=0, property='',
                  technology1=False, technology2=False, technology3=False, audience=0, platform=False, influencer=False)
add2 = player.Player(name = 'Новая компания', capital=0, property='',
                  technology1=False, technology2=False, technology3=False, audience=0, platform=False, influencer=False)
add3 = player.Player(name = 'Новая компания', capital=0, property='',
                  technology1=False, technology2=False, technology3=False, audience=0, platform=False, influencer=False)

def expences():
    skolkovo.capital-=150
    entspace.capital-=150
    like.capital-=150
    skillbox.capital-=150
    couch.capital-=50
    couch.audience-=couch.audience*0.2
    mentor.capital-=50
    mentor.audience-=couch.audience*0.2
    expert.capital-=50
    expert.audience-=couch.audience*0.2
    smart.capital-=50
    soe.capital-=50
    bank.capital-=100