#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lms_engine(p_cust_name, p_cust_creditscore, p_cust_requestedloanamount, p_loan_masterdata):
    loan_application_data = {}
    loan_application_data['cust_name']=p_cust_name
    loan_application_data['cust_creditscore']=p_cust_creditscore
    loan_application_data['cust_requestedloanamount']=p_cust_requestedloanamount
    for mdata in p_loan_masterdata : 
        if (p_cust_creditscore >= mdata['cs_start']) and (p_cust_creditscore <= mdata['cs_end'])         and (p_cust_requestedloanamount >= mdata['LoanAmtStart']) and (p_cust_requestedloanamount <= mdata['LoanAmtEnd']):
                loan_application_data['status'] = 'Approved'
                loan_application_data['message'] = """Dear {cust},
                We are pleased to inform that your requested loan amount of ${amt} has been approved with an 
                interest rate of {rate}% for a duration of {dur} months.""".format(cust=p_cust_name, amt=p_cust_requestedloanamount, rate = mdata["Interest"], dur =mdata['Duration'])
                loan_application_data['interest'] = mdata['Interest'] 
                loan_application_data['duration'] = mdata['Duration']
    if p_cust_requestedloanamount> 40000:
        loan_application_data['status'] = 'Rejected'
        loan_application_data['message'] ="""Dear {cust},
                  We regret to inform that your requested loan amount of ${amt} has been rejected 
                  since the maximum loan amount cannot exceed $40000""".format(cust=p_cust_name, amt=p_cust_requestedloanamount)
    elif p_cust_requestedloanamount < 10001 and p_cust_creditscore <101:
        loan_application_data['status'] = 'Rejected'
        loan_application_data['message']="""Dear {cust},
                  We regret to inform that your requested loan amount of ${amt} has been rejected 
                  since the minimum loan amount cannot be less than $10000 if your credit score less than 101""".format(cust=p_cust_name, amt=p_cust_requestedloanamount)
    elif p_cust_creditscore < 0:
        loan_application_data['status'] = 'Error'
        loan_application_data['message']= 'Invalid Credit score'
    return (loan_application_data) 


# In[ ]:




