import pandas as pd


# 1. 数据导入，在pd模块中有csv的处理函数
train_data = pd.read_csv("E:\\xunlei\\train\\train.csv")
test_data = pd.read_csv("E:\\xunlei\\train\\test.csv")


print(train_data.iloc[0, :])
# 2. 数据预处理，我觉得summary肯定是没用的，address我也不能理解，因为每个房子的address一定是不同的，第二个就是就是state 都是ca
# 根据网上的信息，pandas删除列的Api是del，传入的是字符串，代表的是列的名字
# 所以第一步，将需要删除的列安在一个数组，遍历这个数组进行删除
delet_list = ['Address','Summary','State']
for index in delet_list:
    del train_data[index],test_data[index]
all_features = pd.concat((train_data.iloc[:, 0:-1], test_data.iloc[:, 0:]))
# print(all_features.dtypes) 现在就需要对数值类型的进行缩放，对字符串类型进行独热编码

numeric_feature = all_features[all_features.dtypes != 'object']
print(numeric_feature)
# numeric_feature = all_features[all_features.dtypes != 'object'].index
# all_features[numeric_feature] = all_features[numeric_feature].apply(
#     lambda x:(x-x.mean())/x.std() # 归一化？
# )
# print(all_features[numeric_feature])
