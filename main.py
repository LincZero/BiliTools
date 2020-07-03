from biliClass.biliAid import Aid
from biliClass.biliMid import Mid
from biliClass.biliFid import Fid
import network.db as db
import time

###################################################### 三个id爬取库
# 爬取单个视频
# aidObj = Aid(19349301)
# print(aidObj.fns_line())

# 爬取某用户
# midObj = Mid(333566878)
# print(midObj.fav())

# 从用户爬取收藏夹, mid -> fid_list，fid -> aid_list
# midObj = Mid(333566878)
# fid_list = midObj.fav_all() # 返回多个fid
# for fidObj in fid_list:
#   print(f'【{fidObj.title()}】')
#   print(fidObj.aid()) # 从fid遍历出aid

####################################################### 数据库类

# 将单个收藏夹写入数据库
# fidObj = Fid(971763078)
# db.insert(fidObj.title(), fidObj.aid())

# 将所有收藏夹写入数据库
# midObj = Mid(333566878)
# fid_list = midObj.fav_all() # 返回多个fid
# for fidObj in fid_list:
#   db.insert(fidObj.title(), fidObj.aid())

# 从数据库读取数据
# print(db.read('id>=350')) #353

# 自动更新数据库数据
db.autoUpdata("id>352")

