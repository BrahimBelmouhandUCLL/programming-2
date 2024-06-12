class AssocList:
    def __init__(self):
        self.__items = []
    def __setitem__(self, key, value):
        # ???

en_to_fr = AssocList()
en_to_fr['cat'] = 'chat'
en_to_fr['dog'] = 'chien'
en_to_fr['cheese'] = 'fromage'

print