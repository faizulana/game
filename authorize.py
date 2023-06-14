import players

codes = {'2464':players.entspace, '2678':players.skillbox, '2267':players.netology, '3934':players.smart, 
         '3578':players.soe, '8937':players.bank, '4978':players.tutor,
         '8476':players.investor, '4563':players.couch, '4239':players.mentor, '4104':players.expert,
         '9255':players.add1, '9923':players.add2, '9791':players.add3,
         }
sessions = []
admins=[861236842]

ADMIN_CODE = 98403
# ENTSPACE_CODE = 2464
# SKOLKOVO_CODE = 3678
# NETOLOGY_CODE = 2267

# SMART_CODE = 3934
# SOE_CODE = 3578

# BANK_CODE = 8937
# INVESTOR_CODE = 8476

# COUCH_CODE = 4563
# MENTOR_CODE = 4239
# EXPERT_CODE = 4104
# TUTOR_CODE = 4978

# ADD1_CODE = 9255
# ADD2_CODE = 9923
# ADD3_CODE = 9791

class Auth:
    def __init__(self, chat_id, code):
        self.chat_id = chat_id
        self.code = code
        self.company = codes[code]

def authenticate (message):
    global sessions
    chat_id = message.chat.id
    code = message.text
    for s in sessions:
        if s.chat_id == chat_id:
            sessions.remove(s)
    auth = Auth (chat_id, code)
    sessions.append(auth)

def authorize (chat_id):
    for s in sessions:
        if s.chat_id == chat_id:
            return s.company

def identify_company(name):
    if name in ['skillbox', 'skill', 'скилбокс', 'скиллбокс', 'скил', 'скилл', 'скиллбоксу', 'скилбоксу', 'скил-бокс', 'скилл-бокс']:
        return players.skillbox
    elif name in ['entspace', 'ent', 'ентспейс', 'ентспэйс', 'энтспейс', 'энтспэйс', 'ент', 'энт']:
        return players.entspace
    elif name in ['сколково', 'skolkovo', 'scolcovo', 'scolkovo', 'мшу', 'скол']:
        return players.skolkovo
    elif name in ['нетология', 'нетологи', 'netology', 'netologia', 'нэтология', 'нет']:
        return players.like
    elif name in ['ментор', 'mentor']:
        return players.mentor
    elif name in ['tutor', 'nastavnik', 'наставник', 'наставни', 'тьютор', 'тютор']:
        return players.tutor
    elif name in ['коуч', 'коучер', 'кауч', 'couch', 'коч']:
        return players.couch
    elif name in ['expert', 'ent', 'ентспейс', 'ентспэйс', 'энтспейс', 'энтспэйс', 'ент', 'энт']:
        return players.expert
    elif name in ['smart', 'lab', 'smartlab', 'smart_lab', 'smart-lab', 'смарт', 'лаб']:
        return players.smart
    elif name in ['school', 'soe', 'schoolofeducation', 'school-of-education', 'школа', 'сое', 'школа-образования']:
        return players.soe
    elif name in ['тинькофф', 'тинькоф', 'банк', 'тинькофбанк', 'тинькоффбанк', 'тинькофф-банк', 'bank']:
        return players.bank
    elif name in ['investor', 'рик', 'инвестор', 'российская', 'российской', 'российская_инвестиционная_компания', 'росийская', 'российской_инвестиционной_компании']:
        return players.investor
