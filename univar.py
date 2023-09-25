class univar():
    def QuanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtype=='object'):
                #print("qual")
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual