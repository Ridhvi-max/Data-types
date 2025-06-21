text={"Apples":20,"orange":10,"banana":15,"mango":10,"Grapes":10,}
print("The orignal dictionary:"+ str(text))
x=10
f=0
for i in text:
    if text[i]==x:
        f=f+1
print("Frequency of 10 in fruit is :"+ str(f))