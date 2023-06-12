import players

codes = {'2464':players.entspace, '2678':players.skillbox, '2267':players.like, '3934':players.smart, 
         '3578':players.soe, '8937':players.bank, 
         '8476':players.investor, '4563':players.couch, '4239':players.mentor, '4104':players.expert,
         '9255':players.add1, '9923':players.add2, '9791':players.add3,
         }
sessions = []

# ENTSPACE_CODE = 2464
# SKOLKOVO_CODE = 3678
# LIKE_CODE = 2267

# SMART_CODE = 3934
# SOE_CODE = 3578

# BANK_CODE = 8937
# INVESTOR_CODE = 8476

# COUCH_CODE = 4563
# MENTOR_CODE = 4239
# EXPERT_CODE = 4104

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
    if name == 'skillbox':
        return players.skillbox
    elif name == 'entspace':
        return players.entspace
    elif name == 'skolkovo':
        return players.skolkovo
    elif name == 'like':
        return players.like
    elif name == 'наставник':
        return players.mentor
    elif name == 'коуч':
        return players.couch
    elif name == 'эксперт':
        return players.expert
    elif name == 'smart lab':
        return players.smart
    elif name == 'school of education':
        return players.soe
    elif name == 'тинькофф':
        return players.bank
    elif name == 'российская инвестиционная компания':
        return players.investor
