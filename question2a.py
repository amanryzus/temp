date=[int(z) for z in input("Enter a date in DD/MM/YY format:").split('/')]
dict={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

if(date[0]==1):
    print(str(date[0])+"st "+dict[date[1]]+ " " + str(date[2]))

elif (date[0]==2):
    print(str(date[0])+"nd "+dict[date[1]]+ " " + str(date[2]))

elif date[0]==3:
    print(str(date[0])+"rd "+dict[date[1]]+ " " + str(date[2]))

else:
    print(str(date[0])+"th "+dict[date[1]]+ " " + str(date[2]))
