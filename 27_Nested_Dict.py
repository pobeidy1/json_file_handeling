# -*- coding: utf-8 -*-
"""
Description: How to extract values of Particular Key in Nested dictionary
Using list comprehension

Created:     On Sun Mar 13 20:28:01 2022
@author:     Pobeidy
last edited: PO 24/11/2022
code status: Working fine 

"""

  
#--------config---------------------------------------------------------------
# initializing dictionary
main_dict =   {'dict01' : {"key01" : 7,   "key02" : 9,   "key3" : 12},
               'dict02' : {"key01" : 17,  "key02" : 10,  "key3" : 20}, 
               'dict03' : {"key01" : 16,  "key02" : 18,  "key3" : 11}}

# initializing key(extract all the values for this key)
key_of_interest = "key3"


#--------Function-------------------------------------------------------------  
def extract_value_form_nested_dict (main_dict, expected_key):
    
    # input: 
    #     (a) json object as nested dictionary 
    #     (b) Key_of_interest: key which is similar among the nested dictionaries  
    #         and you want to extract its value

    # printing original dictionary
    print("The original dictionary is : " + str(main_dict))
      
    # using item() to extract key value pair as whole (\ is only breaking the line)
    outcome_values = [val[expected_key] for key, val in main_dict.items() \
                      if expected_key in val]
      
    # printing result 
    print("The extracted values : " + str(outcome_values)) 
    return outcome_values

#---------Run part------------------------------------------------------------
if __name__ == "__main__" :
    
    
    outcome_values= extract_value_form_nested_dict (main_dict, key_of_interest)