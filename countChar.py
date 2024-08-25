str = "Pyth465cho swapcase() m5583 converted *"
t,a,n,s = 0,0,0,0
count = 0

str = str.lower()

for ch in str:
    if(ch.isalpha()):
        a += 1
    elif(ch.isnumeric()):
        n += 1
        count += int(ch)
    else :
        s += 1

t = s+n+a
print("Total characters : ",t)
print("special characters : ",s)
print("numeric characters : ",n)
print("alphabetic characters : ",a)
print("Sum of numeric characters is : ",count)


dict = { 
    'a' : 2,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 4
}
st = set()
for i in dict.values():
    st.add(i)
print(st)
