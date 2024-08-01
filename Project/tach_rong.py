# t.csv
import pandas as pd
import re
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

df_t = df_t.drop(lt)
# print("Dau")
# print(df_t.head(10))
# print("Cuoi")
# print(df_t.tail(30))
#Sau khi tách Date chứa "{}"
df_t.reset_index(drop=True, inplace=True)
print(df_t.shape)
lt_content = []
for idx,txt in enumerate(df_t['Content']):
    try:
        if txt.__contains__("Content"):
            lt_content.append(idx)
    except:# Xử lý trường hợp txt kiểu float
        lt_content.append(idx)
        pass
    else:# bỏ qua tất cả
        pass
print(lt_content)
df_t = df_t.drop(lt_content)
#Sau khi tách Content chứa "nan"
df_t.reset_index(drop=True, inplace=True)
print(df_t.shape)
print(df_t[0:40])
print(df_t[40:92])
