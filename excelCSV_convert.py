import pandas as pd
read_file = pd.read_excel('Online_Retail.xlsx')

read_file.to_csv ('selectionscashflows_2024.csv',  
                  index = None, 
                  header=True) 
    
# read csv file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_csv('Online_Retail.csv')) 
  
# show the dataframe 
df