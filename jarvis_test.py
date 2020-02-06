from jarvis import JarvisCommands

j1 = JarvisCommands()

@j1("make tea")
def f1():
    print('I will make tea')

@j1("introduce yourself")
def f2():
    print('my name is Jarvis')

@j1("atakan")
def f3():
    print('Give admin access')

@j1("are you there")
def f4():
    print('yes, sir!')

@j1("are you there")
def f10():
    print ('At your service, Sir')
    
@j1("initiate new day protocol")
def f10():
    print ('new day')
    

@j1("make tea")
def f10():
    print ('tea')
    

@j1("make coffee")
def f10():
    print ('coffee')
    
    
@j1("turn on the lights")
def f10():
    print ('3 lights on')
    
    
@j1("turn off the lights")
def f10():
    print ('3 lights off')
    

@j1("activate cinema mode")
def f10():
    print ('3 lights off')
         

@j1("close the first light")
def f10():
    print ('1 off')
    

@j1("close the second light")
def f10():
    print ('2 off')
    
    
@j1("close the third light")
def f10():
    print ('3 off')
    

@j1("open the first light")
def f10():
    print ('1 on')
    

@j1("open the second light")
def f10():
    print ('2 on')
    
    
@j1("open the third light")
def f10():
    print ('3 on')
    
    
@j1("google that")
def f10():
    print ('googling')
    
    
@j1("note that")
def f10():
    print ('taking note')
    
    
@j1("play music")
def f10():
    print ('music')
    

while True:
    j1.listen()
