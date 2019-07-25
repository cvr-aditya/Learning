import pandas as pd
from datetime import timedelta
from datetime import datetime
from datetime import date
import numpy as np

data = pd.read_csv("Report5.csv",
                   encoding="ISO-8859-1")
df = pd.DataFrame(data)
test = data[['CAN', 'Date', 'Balance', 'Trans Type']]
avgDemand = 10
testRows = df.CAN.unique()
today = pd.Timestamp(date.today()).to_pydatetime()
index = len(testRows)
print(index)
defaultMonths = 0


for can in testRows:
    singleConsumer = test[test['CAN'] == can]
    singleConsumer = singleConsumer[::-1]
    print("len singlecons is ",len(singleConsumer))
    for i, row in singleConsumer.iterrows():
        if (singleConsumer['Trans Type'][i] == 'WaterBillCollection' or singleConsumer['Trans Type'][i] == 'ReverseWaterBillDemand'):
            if (singleConsumer['Balance'][i] <= avgDemand):
                defDate = datetime.strptime(singleConsumer['Date'][i].strip(), '%d/%m/%Y')
                print(defDate)
                break
   
    
    print("def Date: ", defDate)
    defDays = today - defDate
    print("def days: ", defDays)
    print("def months: ", defDays / 30)
