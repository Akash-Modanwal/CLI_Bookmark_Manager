import helperfun

print("Welcome to bookmark manager")
print("Uses")
cmd= int(input("1.View\n2.Add\n3.Remove\n4.Edit "))

if cmd==1:
    helperfun.view()
elif cmd==2:
    helperfun.Add()
elif cmd==3:
    helperfun.remove()
elif cmd==4:
    helperfun.edit()
else:
    print("Not a valid input")
