print("You can count 1 number or two at once.")
print("who ever counted 30 loses.")
print("Let's start the game!")
print("")

start = 1
while True :
    inputList = []
    inputList = input( 'Please input your count:' )
    if "quit" in inputList:
        break;
    if int(inputList.split(' ')[0]) != start:
        print("don't cheat!")
    else :
        if "30" in inputList:
            print("YOU LOSE!")
            break;
        else:
            end = int(inputList.split(' ')[-1])
            if end%3 == 0:
                print(end+1, end+2)
                if(end+1 == 30 or end+2 ==30):
                    print("YOU WIN!!")
                    break;
                start = end+3
            if end%3 == 1:
                print(end+1)
                if(end+1 == 30):
                    print("YOU WIN!!")
                    break;
                start = end+2
            if end%3 == 2:
                print(end+1)
                if(end+1 == 30):
                    print("YOU WIN!!")
                    break;
                start = end+2