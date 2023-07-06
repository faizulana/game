from authorize import identify_company

def process_request(text):
    components = str(text).lower().split()
    if components[0] == '=':    #добавить
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property+=', '
            company.property+=' '.join(components[3::])
            return company.property
        if components[1] == 'д':
            company = identify_company(components[2])
            company.capital+=int(components[3])
            return company.capital
        if components[1] == 'т1':
            company = identify_company(components[2])
            company.technology1=True
            return company.technology1
        if components[1] == 'т2':
            company = identify_company(components[2])
            company.technology2=True
            return company.technology2
        if components[1] == 'т3':
            company = identify_company(components[2])
            company.technology3=True
            return company.technology3      
        if components[1] == 'э':
            company = identify_company(components[2])
            company.experts+=1
            return company.experts
        if components[1] == 'курс':
            company = identify_company(components[2])
            company.course+=1
            return company.course
        if components[1] == 'н':
            company = identify_company(components[2])
            company.mentorship+=1
            return company.mentorship
        if components[1] == 'простой':
            company = identify_company(components[2])
            company.simple+=1
            return company.simple
        if components[1] == 'сложный':
            company = identify_company(components[2])
            company.complex+=1
            return company.complex
        if components[1] == 'а':
            company = identify_company(components[2])
            company.audience+=int(components[3])
            return company.audience
        
    if components[0] == '-':  #убрать
        if components[1] == 'д':
            company = identify_company(components[2])
            company.capital-=int(components[3])
            return company.capital
        if components[1] == 'а':
            company = identify_company(components[2])
            company.audience-=int(components[3])
            return company.audience
        if components[1] == 'э':
            company = identify_company(components[2])
            company.experts-=int(components[3])
            return company.experts
        
    if components[0] == '!':  #изменить
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property=' '.join(components[3::])
            return company.property
        if components[1] == 'д':
            company = identify_company(components[2])
            company.capital=int(components[3])
            return company.capital
        if components[1] == 'название':
            company = identify_company(components[2])
            company.name=' '.join(components[3::])
            return company.name
        if components[1] == 'а':
            company = identify_company(components[2])
            company.audience=int(components[3])
            return company.audience
        if components[1] == 'учитель':
            company = identify_company(components[2])
            if company.teacher== True: company.teacher=False
            elif company.teacher==False: company.teacher=True
            return company.teacher
        if components[1] == 'инфл':
            company = identify_company(components[2])
            if company.influencer== True: company.influencer=False
            elif company.influencer==False: company.influencer=True
            return company.influencer        

    elif components[0] == '!с':
        company = identify_company(components[1])
        return f'{company.check_capital()} \nучит {company.teacher}'
    elif components[0] == '!аудитория':
        if len(components) > 1:
            global audience
            audience+=int(components[1])
            return f'аудитория {str(audience)}'
        else: return audience
