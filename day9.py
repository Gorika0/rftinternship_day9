import pandas as pd
data={
    "name":["aman","riya","karan","sneha","rahul"],
    "age":[25,32,28,24,35],
    "salary":[60000,45000,70000,52000,40000]
}
df=pd.DataFrame(data)
print(df)
filtered_data=df[(df["salary"]>50000)&(df["age"]<30)]
print("filtered data:")
print(filtered_data)
filtered_data.to_csv("filtered_data.csv",index=False)

#using if else 
for i in range(len(df)):
    if df["salary"][i]>50000 and df["age"][i]<30:
        print(df.loc[i])
    else:
        pass    
