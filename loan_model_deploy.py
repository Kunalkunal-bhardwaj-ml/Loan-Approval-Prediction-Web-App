# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:01:21 2026

@author: Lenovo
"""

import numpy as np
import pickle

# load trained model
model=pickle.load(open('D:/deployment model/loan_model.sav','rb'))

# input
input=(0,1	,1	,1	,0	,12841	,10968.0	,349.0	,360.0	,1.0,1)

# input data convert into array
input_data_asnumpy_array=np.asarray(input)


reshaped_array=input_data_asnumpy_array.reshape(1,-1)

prediction=model.predict(reshaped_array)
print(prediction)
if(prediction[0]==0):
  print("loan not approved")
else:
  print("loan approved")

