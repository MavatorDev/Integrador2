from DataBase import db
from datetime import date
from datetime import datetime

tem = db.temperature


def saveGeneratedTemperature(dataframe):
    temp = {"Date": datetime.now(), 's_Tr_AmbC': float(dataframe['s_Tr_AmbC']), 
    's_Tr_CrcC': float(dataframe['s_Tr_CrcC']), 
    's_Tr_CrcF': float(dataframe['s_Tr_CrcF']), 
    's_Tr_FyrF': float(dataframe['s_Tr_FyrF']), 
    's_Tr_GdF': float(dataframe['s_Tr_GdF']), 
    's_Tr_GoyaF': float(dataframe['s_Tr_GoyaF']), 
    's_Tr_Hal1F': float(dataframe['s_Tr_Hal1F']), 
    's_Tr_PitF': float(dataframe['s_Tr_PitF']), 
    's_Tr_StdsC': float(dataframe['s_Tr_StdsC']), 
    's_Tr_StdsF': float(dataframe['s_Tr_StdsF']), 
    's_TRet_AmbF': float(dataframe['s_TRet_AmbF']), 
    's_TRet_StllC': float(dataframe['s_TRet_StllC']), 
    's_TRet_StllF': float(dataframe['s_TRet_StllF']), 
    'z_Tr_AmbC': float(dataframe['z_Tr_AmbC']), 
    'z_Tr_GyrreC': float(dataframe['z_Tr_GyrreC']), 
    'z_Tr_HalSAPAF': float(dataframe['z_Tr_HalSAPAF']), 
    'z_Tr_OrchReheF': float(dataframe['z_Tr_OrchReheF']), 
    'z_Tr_Sng4': float(dataframe['z_Tr_Sng4']), 
    'z_TRet_Bllt': float(dataframe['z_TRet_Bllt']), 
    'z_TRet_Choir': float(dataframe['z_TRet_Choir']), 
    'z_TRet_CrcC': float(dataframe['z_TRet_CrcC']), 
    'z_TRet_CrcF': float(dataframe['z_TRet_CrcC']), 
    'z_TRet_Hal6F': float(dataframe['z_TRet_Hal6F']), 
    'z_TRet_OffiF': float(dataframe['z_TRet_OffiF']), 
    'z_TRet_R14': float(dataframe['z_TRet_R14']), 
    'z_TRet_Store': float(dataframe['z_TRet_Store']), 
    'z_TRet_Tech': float(dataframe['z_TRet_Tech'])
    }

    try:
        tem.insert_one(temp)
    except Exception as e:
        print ("Unexpected error:", type(e), e)

def getTemperatures():
    list = tem.sort("_id", -1)
    return list
