class PartyAnimal:
    x = 5

    def party(who):
        who.x = who.x + 1
        print('So far :', who.x)


an = PartyAnimal()
an.party()
an.party()
#  an.party()
PartyAnimal.party(an)
PartyAnimal.party(an)