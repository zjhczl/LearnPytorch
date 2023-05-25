# 创建读取csv
import pandas as pd
import pandas
import os
# 创建data文件夹
os.makedirs(os.path.join(".", "data"), exist_ok=True)
data_file = os.path.join(".", "data", "house_tiny.csv")
with open(data_file, "w") as f:
    f.write("name,Alley,Price\n")
    f.write("N1,pave,127500\n")
    f.write("N2,dsa,12552\n")
    f.write("N2,sada,12546\n")
    f.write("N4,NA,11546\n")
data = pd.read_csv(data_file)
print(data)
