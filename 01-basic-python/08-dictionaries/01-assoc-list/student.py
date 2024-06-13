class AssocList:
    def __init__(self):
        self.__items = []
    def __setitem__(self, key, value):
        self.__find_key_index
    def __getitem__(self, key):
        for pair                                    in __items:
            pair[0] = key
    def __contains__(self, key):
        if key in __items:
            return 
    def __len__(self):
        return len(self.__items)
    

en_to_fr = AssocList()
en_to_fr['cat'] = 'chat'
en_to_fr['dog'] = 'chien'
en_to_fr['cheese'] = 'fromage'

print