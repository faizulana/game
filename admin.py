from authentication import identify_company
from players import expences

def process_request(text):
    components = str(text).lower().split()
    if components[0] == '!добавить':
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property+=', '
            company.property+=' '.join(components[3::])
            return company.property
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital+=int(components[3])
            return company.capital
        if components[1] == 'технологии':
            company = identify_company(components[2])
            company.technology+=', '
            company.technology+=' '.join(components[3::])
            return company.technology
    if components[0] == '!убрать':
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital-=int(components[3])
            return company.capital
    if components[0] == '!изменить':
        if components[1] == 'имущество':
            company = identify_company(components[2])
            company.property=' '.join(components[3::])
            return company.property
        if components[1] == 'деньги':
            company = identify_company(components[2])
            company.capital=int(components[3])
            return company.capital
        if components[1] == 'технологии':
            company = identify_company(components[2])
            company.technology=' '.join(components[3::])
            return company.technology
        if components[1] == 'аудитория':
            company = identify_company(components[2])
            company.audience+=int(components[3])
            return company.capital
    elif components[0] == '!состояние':
        company = identify_company(components[1])
        return f'{str(company.capital)} у.е., {str(company.property)}, технология {str(company.technology)}, аудитория {str(company.audience)} '
    elif components[0] == '!аудитория':
        if len(components) > 1:
            global audience
            audience+=int(components[1])
            return f'аудитория {str(audience)}'
        else: return audience
    elif components[0] == '!отбивка':
        expences()
        return f'Такт завершен. Свободная аудитория в следующем такте {audience}'