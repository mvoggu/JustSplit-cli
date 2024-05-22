def settled(ledger):
    for user in ledger:
        if ledger[user] != 0:
            return False
    return True    

def trySettle(ledger):
    minima = min(ledger, key=ledger.get)
    maxima = max(ledger, key=ledger.get)

    minimaVal = ledger[minima]
    maximaVal = ledger[maxima]

    ledger[minima] = 0
    ledger[maxima] = maximaVal + minimaVal # + instead of - since minimaVal is expected to be negative

    print(f'{maxima} to pay Rs.{-minimaVal} to {minima}')


myLedger = {
}

while(True):
    Command = input('Enter command: ')
    if Command == 'Q':
        break

    if Command == 'A':
        User = input('Enter username of person: ')
        if User in myLedger:
            print('User already exists in ledger!')
            continue

        myLedger.update({User: 0})

    if Command == 'P':
        if len(myLedger) == 0:
            print('Please add a user first!')
            continue

        Payor = input('Enter name of person who is paying: ')
        Amount = int(input('Enter amount paid: '))

        existing = myLedger.get(Payor)
        myLedger.update({Payor: existing - Amount})
        
        split = Amount/len(myLedger) # TODO: implement unequal splits

        for user in myLedger:
            myLedger[user] = myLedger[user] + split


print(f'\nLedger before settling:\n{myLedger}')
print('\nHere is how to clear your splits!:')

while not settled(myLedger):
    trySettle(myLedger)

print('\nLedger would like this after settling up:')
print(myLedger)