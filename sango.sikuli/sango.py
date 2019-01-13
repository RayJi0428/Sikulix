Region(567,184,935,528)
card = False
target = False
while 1: 
    "出牌階段"
    if exists("1547399243127.png"):
        card = False
        if (card == False):
            if exists("1547400366355.png"):
                card = True
                click("1547400366355.png")
                wait(1)
        elif (card == True and exists("1547400748664.png")):
            target = True
            click("1547400748664.png")
            wait(1)
        elif (target == True and exists("1547398179829.png")):
            card = False
            target = False
            click("1547398179829.png")
            wait(1)
    else:
        if exists("1547400066832.png"):
            click("1547400066832.png")
            wait(1)
            
            
    
        
        
       
       
