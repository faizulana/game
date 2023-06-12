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
            if company.influencer==False:
                return 'У вас нет инфлюенсера для создания курса'
            else:
                if company.technology1 == False:
                    company.capital-= 8
                else: company.capital -= 4
                company.course+=1
                return 'курс создан'
        
        if components[1] == 'наставничество':
            if company.influencer==False:
                return 'У вас нет инфлюенсера для создания наставничества'
            else:
                if company.technology1 == False:
                    company.capital-= 8
                else: company.capital -= 4
                company.mentorship+=1
                return 'наставничество готово'

        if components[1] == 'простой':
            if company.teacher==False:
                return 'У вас нет экспертности для создания простого образовательного продукта. Обратитесь в школу'
            else:
                if company.technology1 == False:
                    company.capital-= 10
                else: company.capital -= 5
                company.simple+=1
                return 'простой продукт создан'
        
        if components[1] == 'сложный':
            if company.experts==0:
                return 'У вас нет команды экспертов для создания сложного образовательного продукта. Обратитесь в школу'
            else:
                if company.technology1 == False:
                    company.capital-= 50
                else: company.capital -= 20
                company.experts-=1
                company.complex+=1
                return f'Сложный продукт создан. Осталось {company.experts} свободных экспертов'

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


