# t.csv
import pandas as pd
df_t = pd.read_csv("t.csv", delimiter="|")

# print(df_t['Date'].astype(str))
numb = -1
lt = []
#Trước khi tách
print(df_t.shape)
for txt in df_t['Date']:
    for x in txt:
        
        if x == "{":
            # df_t['Date'].drop(df_t.index[idx])
            numb+=1
            lt.append(numb)
            print(numb)
            break
        numb+=1
        break

for i in lt:
    df_t = df_t.drop(i)
# print("Dau")
# print(df_t.head(10))
# print("Cuoi")
# print(df_t.tail(30))
#Sau khi tách Date chứa "{}"
print(df_t.shape)
lt_content = []
for idx,txt in enumerate(df_t['Content']):
    try:
        if txt.__contains__("nan|Nan|NaN|"):
            lt_content.append(idx)
    except:
        pass
    
for i in lt_content:
    df_t = df_t.drop(i)
#Sau khi tách Content chứa "nan"
print(df_t.shape)