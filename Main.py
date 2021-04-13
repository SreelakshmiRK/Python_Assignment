#calling a python file from another python file
import MasterData
import lms_engine
import sys
import os


#l_cust_name ='CCC'
#l_cust_creditscore =-10
#l_cust_requestedloanamount = 35000

# l_cust_name = input("Enter name: ")
# l_cust_creditscore = input("Enter credit score: ")
# l_cust_requestedloanamount = input("Enter required loan Amount : ")

# output_data = lms_engine.lms_engine(l_cust_name, l_cust_creditscore, l_cust_requestedloanamount, MasterData.g_loan_masterdata)
# print(output_data)



#l_cust_name ='CCC'
#l_cust_creditscore =-10
#l_cust_requestedloanamount = 35000

l_UserInput1 = input("Enter name and press enter: ")
l_cust_name = l_UserInput1
greetings(l_cust_name)
l_UserInput2 = input("Enter credit score and press enter: ")
l_UserInput3 = input("Enter required loan amount and press enter: ")
l_cust_name = l_UserInput1
l_cust_creditscore = int(l_UserInput2)
l_cust_requestedloanamount = int(l_UserInput3)

output_data = lms_engine.lms_engine(l_cust_name, l_cust_creditscore, l_cust_requestedloanamount, MasterData.g_loan_masterdata)
print(output_data)

new_file = open("C:\\Users\\sreen\\OneDrive\\Desktop\\Python\\training/"+l_cust_name+".txt", "a")

# STEP 3: Write to file using write method
new_file.write(str(output_data))
new_file.close()