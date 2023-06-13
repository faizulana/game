from authorize import identify_company

def process_message(company, text):
    components=str(text).lower().split()
    if components[0] == 'перевести':
        receiver = identify_company(components[2])
        answer = company.transfer_money(amount=int(components[1]), to=receiver)
        return answer
    
    elif components[0] == 'создать':

        if components[1] == 'курс':
            if company.course>0:
                return 'У вас уже есть курс для реализации в этом такте'
            else:
                if company.technology1 == False:
                    company.capital-= 8
                else: company.capital -= 4
                company.course+=1
                return 'Вы создали курс. Теперь вы можете реализовать его на свою аудиторию.'
        
        if components[1] == 'наставничество':
            if company.mentorship>0:
                return 'У вас уже есть наставничество для реализации в этом такте'
            else:
                if company.technology1 == False:
                    company.capital-= 8
                else: company.capital -= 4
                company.mentorship+=1
                return 'Вы создали программу наставничества. Теперь вы можете реализовать ее на свою аудиторию'

        if components[1] == 'простой':
            if company.teacher==False:
                return 'У вас не хватает знаний для создания простого образовательного продукта. Обратитесь в School of Education для обучения'
            else:
                if company.technology1 == False:
                    company.capital-= 10
                else: company.capital -= 5
                company.simple+=1
                return 'Вы создали простой продукт, и теперь можете реализовать его на личную или свободную аудиторию'
        
        if components[1] == 'сложный':
            if company.experts==0:
                return 'У вас нет свободной команды экспертов для создания сложного образовательного продукта. Обратитесь в School of Education или дождитесь следующего такта.'
            else:
                if company.technology1 == False:
                    company.capital-= 50
                else: company.capital -= 20
                company.experts-=1
                company.complex+=1
                return f'Сложный продукт создан. У вас осталось {company.experts} свободных экспертов'

        if components[1] == 'технология1':
            if company.capital >= 150:
                company.technology1= True
                company.property+='\nТехнология 1'
                return 'Технология разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'технология2':
            if company.capital >= 150:
                company.technology2= True
                company.property+='\nТехнология 2'
                return 'Технология разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'технология3':
            if company.capital >= 150:
                company.technology3= True
                company.property+='\nТехнология 3'
                return 'Технология разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'эксперты':
            if company.capital >= 150:
                company.experts+=1
                return 'Команда экспертов создана'
            else: return 'У вас недостаточно средств для обучения экспертов'


