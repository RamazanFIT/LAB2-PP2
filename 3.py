def solve(numheads, numlegs):
    chicken = numheads 
    numrab = (numlegs - chicken*2)//2
    dict = {}
    dict["chickens"] = chicken 
    dict["rabbits"] = numrab 
    return(dict)



     



heads = int(input())

legs = int(input())

answer = solve(heads, legs)

print(answer)

