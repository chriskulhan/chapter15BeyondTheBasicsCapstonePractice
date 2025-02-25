import wizcoin

purse = wizcoin.Wizcoin(2, 5, 99) 
#the ints are passed to __init__()
print (purse)
print('G:', purse.galleons, 'S:', purse.sickles, "K:", purse.knuts)
print("Total value:", purse.value())
print('Weight:', purse.weightInGrams(), 'grams')

print() #prints a space

#output: 
# <wizcoin.Wizcoin object at 0x74584a9bc0b0>
# G: 2 S: 5 K: 99
# Total value: 1230
# Weight: 613.906 grams

coinJar = wizcoin.Wizcoin(13,0,0)
#The ints are passed to __init__()
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.value())
print('Weight:', coinJar.weightInGrams(), 'grams')

#output: 
# <wizcoin.Wizcoin object at 0x74584a9bc0e0>
# G: 13 S: 0 K: 0
# Total value: 6409
# Weight: 404.339 grams