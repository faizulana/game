import player

skillbox = player.Player(name = 'Skillbox', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          teacher = True, influencer = False, experts=0)
entspace = player.Player(name = 'Entspace', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          teacher = True, influencer = False, experts = 1)
skolkovo = player.Player(name = 'Skolkovo', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          teacher = True, influencer = False, experts=1)
netology = player.Player(name = 'Нетология', capital = 400, property = '',
                          technology1=False, technology2=False, technology3=False, audience=0, 
                          teacher = True, influencer = False, experts=0)
couch = player.Player(name = 'Коуч', capital = 100, property = '', technology1=False, experts=0,
                      technology2=False, technology3=False, audience=50, teacher = False, influencer = True) #50
mentor = player.Player(name = 'Ментор', capital = 100, property = '', technology1=False, experts=0,
                      technology2=False, technology3=False, audience=50, teacher = False, influencer = True)
expert = player.Player(name = 'Эксперт', capital = 100, property = '', technology1=False, experts=0,
                      technology2=False, technology3=False, audience=50, teacher=False, influencer = True)
tutor = player.Player(name = 'Наставник', capital = 100, property = '', technology1=False, experts=0,
                      technology2=False, technology3=False, audience=50, teacher=False, influencer = True)
soe = player.Player(name = 'School of Education', capital = 100, property = '', experts=0,
                    technology1=False, technology2=False, technology3=False, audience= 0, influencer=False, teacher=True) #50   develop 150
smart = player.IT(name = 'Smart Lab', capital=100, property='', experts=0,
                  technology1= False, technology2=False, technology3=False, audience=0, teacher=False, influencer=False) #50  develop 100
bank = player.Player(name = 'Тинькофф', capital=800, property='', experts=0,
                  technology1= False, technology2=False, technology3=False, audience=0, teacher=False, influencer=False)
investor = player.Player(name = 'Российская Инвестиционная Компания', capital=700, property='', experts=0,
                  technology1=False, technology2=False, technology3=False, audience=0, teacher=False, influencer=False)

add1 = player.Player(name = 'Новая компания', capital=0, property='', experts=0,
                  technology1=False, technology2=False, technology3=False, audience=0, teacher=True, influencer=False)
add2 = player.Player(name = 'Новая компания', capital=0, property='', experts=0,
                  technology1=False, technology2=False, technology3=False, audience=0, teacher=False, influencer=False)
add3 = player.Player(name = 'Новая компания', capital=0, property='', experts=0,
                  technology1=False, technology2=False, technology3=False, audience=0, teacher=False, influencer=False)

companies=[entspace, skillbox, skolkovo, netology, bank, investor, smart, soe, mentor, couch, expert, tutor, add1, add2, add3]

def expences():
    skolkovo.capital-=150
    entspace.capital-=150
    netology.capital-=150
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
    for company in companies:
        company.course=0
        company.mentorship=0
        company.simple=0
        if company.complex>0:
            company.experts+=int(company.complex)
            company.complex=0