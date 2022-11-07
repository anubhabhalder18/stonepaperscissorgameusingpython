import random
pc_score=0
user_score=0

def print_score():
    global pc_score,user_score
    print("USER\t",str(user_score),"\t\tPC\t",str(pc_score))



def sc(c):
    input=""
    for x in c:
        if(x!=" "):
            input=input+x.lower()
            break
    return input


def game(U):
    global pcl
    global pc_score,user_score
    user=sc(U)
    pc=random.choice(pcl)
    print("PC >>>\t",pc)
    

    
    if(pc=="s" and user=="k"):
        pc_score+=1
        print_score()
    elif(pc=="p" and user=="s"):
        pc_score+=1
        print_score()
    elif(pc=="k" and user=="p"):
        pc_score+=1
        print_score()
    elif(pc=="k" and user=="s"):
        user_score+=1
        print_score()
    elif(pc=="s" and user=="p"):
        user_score+=1
        print_score()
    elif(pc=="p" and user=="k"):
        user_score+=1
        print_score()
    elif(pc=="p" and user=="p"):
        print("\t\t\tDRAW")
        print_score()
    elif(pc=="k" and user=="k"):
        print("\t\t\tDRAW")
        print_score()
    elif(pc=="s" and user=="s"):
        print("\t\t\tDRAW")
        print_score()
    
    
pcl=["s","p","k"]
Max=5
i=0
print("\t\tWELCOME TO STONE PAPER SCISSOR GAME ")
while(i<Max):
    User=input("\nEnter s for stone p for paper k for scissor and e to exit\t")
    if(sc(User)=="e"):
        i=Max
        print("\n\ngame exited \n\n")
   
    elif(sc(User) not in "spk"):
        
        print("Enter again")
        
    else:
        game(User)
        i+=1
if(pc_score==user_score):
    print("\n\n\n\t\tDRAW\n")
elif(pc_score>user_score):
    print("\n\n\n\t\tPC WON\n")
if(pc_score<user_score):
    print("\n\n\n\t\tYOU WON\n")




