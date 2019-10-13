import random
inputList = []
inputList = input( 'Please input your selections split with comma: ' )
resultList = [x.strip() for x in inputList.split(',')]
print("Try :", random.choice(resultList))
