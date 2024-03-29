import pandas as pd
# 1. 打开并处理 UoR Data.csv 文件
df = pd.read_csv(r'D:\GithubRepository\import_folder\4. VariousCodeProgram\Python_program\Python_Basic\Data\UoR_Data.csv',
            index_col='TimeStamp',
                  header=0,
                  skiprows=list(range(2, 101)))

# # 2. 重命名索引和列名
df.index.name = 'time'
# 命名'var' 要放在后面, 不然, 后面就会找不到, 因为 columns 全都命名了var , 那就找不到了.

# 3. 提取“G”, “LuW”, 'SuW'列的数据并保存到 practicel.csv 文件
subset_df = df[['G', 'Luw', 'Suw']]

df.columns.names = ['var']   # 将所有的列名都变为 var

subset_df.to_csv('practice1.csv', index=True)

# 4. 提取第21-30行，第5,7,9列的数据，并保存到 practice2.xlsx 文件
selected_columns = [4, 6, 8]  # Python中索引是从0开始的，所以第5、7、9列对应的索引为4、6、8
subset_df_2 = df.iloc[20:31, selected_columns]  # 注意：切片时，行数是左闭右开区间，所以用20:31来获取第21-30行
subset_df_2.to_excel('practice2.xlsx', index=False)  # 默认不包含索引


