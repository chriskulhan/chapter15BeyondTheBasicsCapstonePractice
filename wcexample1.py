import wizcoin

purse = wizcoin.Wizcoin(2, 5, 99) 
#the ints are passed to __init__()
print (purse)
print('G:', purse.galleons, 'S:', purse.sickles, "K:", purse.knuts)
print("Total value:", purse.value())
print('Weight:', purse.weightInGrams(), 'grams')

print()

coinJar = wizcoin.Wizcoin(13,0,0)
#The ints are passed to __init__()
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.value())
print('Weight:', coinJar.weightInGrams(), 'grams')
