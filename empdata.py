empdata = [ { "EmpID":1
             ,"EmpName":"AAA"
             ,"Sal":2000
             ,"Projects":[1,2,3]}
           ,{ "EmpID":2
            ,"EmpName":"BBB"
            ,"Sal":5000
            ,"Projects":[2,3,44,55,56,1,22,33,4444,4444444,11,414,44244]}
           ,{ "EmpID":3
            ,"EmpName":"CCC"
            ,"Sal":3000
            ,"Projects":[1,2,11,3333]}
           ,{ "EmpID":4
            ,"EmpName":"DDD"
            ,"Sal":6000
            ,"Projects":[44,2,3]}]

for a in empdata:
    print(a)

#Print employee name in whose first Project is an even number
print("List of employees whose first project is an even number")
i = 0
for element in empdata:
    if (element['Projects'][0])%2 == 0:
        i += 1
        print(i, " Employee Name : ",element['EmpName'])