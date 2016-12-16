#open file
file = open('makelist.txt', 'w')
#add items to the file

for x in range(10):
    file.write(str(n + 1) + "." + input("Item") + '\n')

file.close()