

import numpy as np
import pickle
import streamlit as st

# load trained model
model=pickle.load(open('D:/deployment model/loan_model.sav','rb'))

# creating functions for prediction

def loan_prediction(input_data):
    input_data_asnumpy_array=np.asarray(input_data)


    reshaped_array=input_data_asnumpy_array.reshape(1,-1)

    prediction=model.predict(reshaped_array)
    print(prediction)
    if(prediction[0]==0):
      return "loan not approved"
    else:
      return "loan approved"
  
    
def main():
    # giving a title 
    st.title('loan prediction web app')
    
    # getting the input from user
    #Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area
    
    Gender=st.text_input('Gender')
    Married=st.text_input('married status')
    Dependents=st.text_input('Enter dependents')
    Education=st.text_input('Education')
    Self_Employed=st.text_input('Self_Employed')
    ApplicantIncome=st.text_input('ApplicantIncome')
    CoapplicantIncome=st.text_input('CoapplicantIncome')
    LoanAmount=st.text_input('LoanAmount')
    Loan_Amount_Term=st.text_input('Loan_Amount_Term')
    Credit_History=st.text_input('Credit_History')
    Property_Area=st.text_input('Property_Area')
    
    
    #code for prediction
    result=''
    
    # creating buttons
    
    if st.button('loan_test_result'):
        result=loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
        
        
        
        st.success(result)
        
        
if __name__ =='__main__' :
    main()
       
        
  
     