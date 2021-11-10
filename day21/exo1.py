import pandas as pd 
#Sélectionner le sheet name parameter details via index
inco=pd.read_excel("PCE_huawei_GSM_OSN_NADC_211109092550.xlsx", sheet_name=1, usecols="H,J", dtype="int")
#Sélectionner les colonnes A,H J du sheet name Parameter details 
inco=pd.read_excel("PCE_huawei_GSM_OSN_NADC_211109092550.xlsx", sheet_name=1, usecols="A,H,J")
print(inco)
#inco=pd.read_excel("PCE_huawei_GSM_OSN_NADC_211109092550.xlsx", sheet_name="Parameter Details")

