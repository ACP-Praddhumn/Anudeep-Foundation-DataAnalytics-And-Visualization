seconds =  int(input("Time in Second : "))
#time validation
if(seconds >= 0):
    hour , minute = 0 , 0 
    #hour validation
    if(seconds >= 3600):
        hour = int(seconds / (60 * 60))
        seconds %= (60*60)
    #minute validation
    if(seconds >= 60):
        minute = int(seconds / 60)
        seconds %= 60
    print("Output : ",hour," Hour ",minute, " Minute ", seconds, " seconds")
else : 
    print("Time can not be negative .")

