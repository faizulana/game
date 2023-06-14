from authorize import identify_company

def process_message(company, text):
    components=str(text).lower().split()
    if components[0] == 'перевести':
        receiver = identify_company(components[2])
        if receiver is None:
            return 'Не удалось распознать компанию-получателя. Пожалуйста, убедитесь что название написано верно и сумма указана цифрой без указания единиц.'
        else:
            answer = company.transfer_money(amount=int(components[1]), to=receiver)
            return answer
    
    elif components[0] == 'создать':

        if components[1] == 'курс':
            if company.influencer == False:
                return 'У вас нет инфлюенсера для создания курса. Вы можете купить инфлюенсера за 200 у.е. или обратиться к игрокам на плацдарме.'
            else:
                if company.technology1 == False:
                    company.capital-= 5
                    company.course+=1
                    return 'Вы создали курс. Теперь вы можете реализовать его на свою аудиторию.'
                else:
                    company.course+=1
                    return 'Вы создали курс. Теперь вы можете реализовать его на свою аудиторию.'
        
        if components[1] == 'наставничество':
            if company.influencer == False:
                return 'У вас нет инфлюенсера для создания наставничества. Вы можете купить инфлюенсера за 200 у.е. или обратиться к игрокам на плацдарме.'
            elif company.mentorship>0:
                return 'У вас уже есть наставничество для реализации в этом такте'
            else:
                if company.technology1 == False:
                    company.capital-= 15
                    company.mentorship+=1
                    return 'Вы создали программу наставничества. Теперь вы можете реализовать ее на свою аудиторию'
                else: 
                    company.capital -= 8
                    company.mentorship+=1
                    return 'Вы создали программу наставничества. Теперь вы можете реализовать ее на свою аудиторию'

        if components[1] == 'простой':
            if company.teacher==False:
                return 'У вас не хватает знаний для создания простого образовательного продукта. Обратитесь в School of Education для обучения'
            else:
                if company.technology1 == False:
                    company.capital-= 10
                    company.simple+=1
                    return 'Вы создали простой продукт, и теперь можете реализовать его на личную или свободную аудиторию'
                else:
                    company.simple+=1
                    return 'Вы создали простой продукт, и теперь можете реализовать его на личную или свободную аудиторию'
        
        if components[1] == 'сложный':
            if company.experts==0:
                return 'У вас нет свободной команды экспертов для создания сложного образовательного продукта. Обратитесь в School of Education или дождитесь следующего такта.'
            else:
                if company.technology1 == False:
                    company.capital-= 50
                    company.complex+=1
                    company.experts-=1
                    return f'Сложный продукт создан. У вас осталось {company.experts} свободных экспертов'
                else: 
                    company.capital -= 20
                    company.experts-=1
                    company.complex+=1
                    return f'Сложный продукт создан. У вас осталось {company.experts} свободных экспертов'

        if components[1] == 'технология1':
            if company.capital >= 100:
                company.technology1= True
                company.property+='\nТехнология 1'
                return 'Технология "Автоматизация производства продукта" разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'технология2':
            if company.capital >= 150:
                company.technology2= True
                company.property+='\nТехнология 2'
                return 'Технология "Предиктивная аналитика" разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'технология3':
            if company.capital >= 200:
                company.technology3= True
                company.property+='\nТехнология 3'
                return 'Технология "Замена экспертов ИИ" разработана и готова к внедрению'
            else: return 'У вас недостаточно средств для разработки'
        
        if components[1] == 'эксперты':
            if company.capital >= 150:
                company.experts+=1
                company.capital-=150
                return 'Команда экспертов создана'
            else: return 'У вас недостаточно средств для обучения экспертов'


