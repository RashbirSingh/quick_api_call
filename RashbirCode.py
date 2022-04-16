from datetime import datetime, timedelta


class fraudDetectionAnalyzer:
    
    def __init__(self, dataStoreObject):
        self.dataStoreObject = dataStoreObject
    
    def analyzer(self,
                 hashed: str,
                 timestamp: datetime,
                 amount: float,
                 threshold: float):
        
        indexObject = -1
        sumAmount = 0
        dataToAnalyseIndex = []
        
        for hashData in self.dataStoreObject["hashed"]:
            indexObject = indexObject + 1
            if hashData == hashed:
                dataToAnalyseIndex.append(indexObject)
                
        currentTimestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        pastTimestamp = currentTimestamp - timedelta(days = 1 ), "%Y-%m-%dT%H:%M:%S"
        
        
        for index in dataToAnalyseIndex:
            if datetime.strptime(self.dataStoreObject["currentTimestamp"][index], "%Y-%m-%dT%H:%M:%S") >= pastTimestamp[0]:
                sumAmount = sumAmount + self.dataStoreObject["amount"][index]
                
                
        if sumAmount >= threshold:
            return hashed



class dataStore:
    
    def __init__(self,
                 dataValues = {"hashed": [], 
                               "currentTimestamp": [], 
                               "pastTimestamp": [], 
                               "amount": [], 
                               "threshold": []
                               }):
        self.dataValues = dataValues
    
    
    def getData(self):
        return self.dataValues
    
    def setData(self,
             hashed: str,
             currentTimestamp: datetime,
             pastTimestamp: datetime,
             amount: float,
             threshold: float):
        
       self.dataValues["hashed"].append(hashed)
       self.dataValues["currentTimestamp"].append(currentTimestamp)
       self.dataValues["pastTimestamp"].append(pastTimestamp)
       self.dataValues["amount"].append(amount)
       self.dataValues["threshold"].append(threshold)



