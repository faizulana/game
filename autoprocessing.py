from authentication import identify_company

def process_message(company, text):
    components=str(text).lower().split()
    if components[0] == 'перевод':
        receiver = identify_company(components[1])
        answer = company.transfer_money(amount=int(components[2]), to=receiver)
        return answer
    
    elif components[0] == 'капитал':
        return company.check_capital()
    
    elif components[0] == 'создать':

        if components[1] == 'курс':
            if company.technology1 == False:
                company.capital-= 8
            else: company.capital -= 4
            company.property+='курс'
            return 'курс создан'
        
        if components[1] == 'наставничество':
            if company.technology1 == False:
                company.capital-= 10
            else: company.capital -= 5
            company.property+=' наставничество'
            return 'наставничество готово'

        if components[1] == 'простой':
            if company.technology1 == False:
                company.capital-= 10
            else: company.capital -= 5
            company.property+=' простой курс'
            return 'простой курс создан'
        
        if components[1] == 'сложный':
            if company.technology1 == False:
                company.capital-= 10
            else: company.capital -= 5
            company.property+=' сложный курс'
            return 'сложный курс создан'

        if components[1] == 'технология1':
            if company.capital >= 150:
                company.technology1= True
                company.property+=' технология 1'
                return 'Технология разработана и готова к внедрению'
            else: return 'недостаточно средств'
        
        if components[1] == 'технология2':
            if company.capital >= 150:
                company.technology2= True
                company.property+=' технология 2'
                return 'Технология разработана и готова к внедрению'
            else: return 'недостаточно средств'
        
        if components[1] == 'технология3':
            if company.capital >= 150:
                company.technology3= True
                company.property+=' технология 3'
                return 'Технология разработана и готова к внедрению'
            else: return 'недостаточно средств'
        
        if components[1] == 'эксперты':
            if company.capital >= 150:
                company.property+=' команда экспертов'
                return 'Команда экспертов создана'
            else: return 'Недостаточно средств для создания'


