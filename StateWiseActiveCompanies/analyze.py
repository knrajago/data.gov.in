import pandas as pd
import json
from pprint import pprint

json_data_loc = 'data/data.json'

def main():
    global json_data_loc
    print('Calling main()')
    data = json.load(open(json_data_loc))
    pprint(data)
    fieldsArray=data['fields']
    fieldNames=[]
    for oneField in fieldsArray:
        fieldNames.append(oneField['label'])
    #for oneFieldName in fieldNames:
    #    print(oneFieldName)
    dataArray=data['data']
    states=[]
    for data in dataArray:
        states.append(data[0])
    #print('States:')
    
    #for oneState in states:
    #    print(oneState)
    df=pd.DataFrame(data=dataArray,columns=fieldNames)
    
    df.set_index('State/UT',inplace=True)
    df=df.apply(pd.to_numeric)
    #df.append(df.sum(numeric_only=True), ignore_index=True)
    
    df['PublicShare']=df['No. of Companies - Public']/df['No. of Companies - Total']
    df['PublicInvestmentShare']=df['Authorized Capital - Public']/df['Authorized Capital - Total']
    allMoreThanHalf=df[df['PublicInvestmentShare'] < 0.5]
    print(df)
    print(allMoreThanHalf)
    pass

def main1():
    global json_data_loc
    print('Calling main()')
    df=pd.read_json(json_data_loc)
    print(df)
    pass

if __name__ == '__main__':
    main()
