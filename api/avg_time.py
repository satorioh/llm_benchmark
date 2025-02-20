import os
import pandas as pd
import matplotlib.pyplot as plt

# 定义结果文件夹路径
result_folder = './result'

# 获取所有csv文件
csv_files = [f for f in os.listdir(result_folder) if f.endswith('.csv')]

# 创建一个画布
plt.figure(figsize=(10, 6))

# 遍历每个csv文件
for csv_file in csv_files:
    # 读取csv文件
    file_path = os.path.join(result_folder, csv_file)
    df = pd.read_csv(file_path)

    # 提取'Concurrent Request Number'和'Average Time'栏位的值
    concurrent_request_number = df['Concurrent Request Number']
    average_time = df['Average Time (s)']

    # 绘制折线图
    plt.plot(concurrent_request_number, average_time, label=csv_file)

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('Average Time (s)')
plt.xlabel('Concurrent Request Number')
plt.ylabel('Average Time (s)')

# 显示图形
plt.show()