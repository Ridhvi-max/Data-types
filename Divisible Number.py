print("Enter a number (Numerator):")
numn=int(input())
print("Enter a number (Denominator):")
numd=int(input())
if numn%numd==0:
    print("\n"+str(numn)+" Is divisible by "+str(numd))
else:
    print("\n"+str(numn)+" Is not divisible by "+str(numd))
    
