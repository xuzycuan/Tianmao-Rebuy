import pandas as pd
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
user_info = pd.read_csv('user_info_format1.csv')
user_log = pd.read_csv('user_log_format1.csv').rename(columns={'seller_id':'merchant_id'})

#填充缺失值
user_info['gender'].fillna(2, inplace=True) #2和null都代表性别不确定
user_info['age_range'].fillna(-1, inplace=True)
user_log['brand_id'].fillna(-1, inplace=True)

from matplotlib import pyplot as plt
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(user_log['time_stamp']) #time_tamp 购买时间（格式：mmdd）
plt.title('time_stamp')
plt.subplot(1,3,2)
plt.hist(user_log['action_type'])
plt.title('action_type') #action_type包含{0, 1, 2, 3}，0表示单击，1表示添加到购物车，2表示购买，3表示添加到收藏夹
plt.subplot(1,3,3)
plt.hist(user_info['gender']) #gender用户性别。0表示女性，1表示男性，2和NULL表示未知
plt.title('gender')
plt.show()