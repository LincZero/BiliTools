import requests
import json
import time
from network.reqjson import reqjson
from biliClass.biliFid import Fid


class Mid:
    mid = 0
    reallink = {}  # 真实地址
    dic = {}  # 构造信息

    def __init__(self, mid):
        self.mid = mid
        self.reallink = {
            # 用户信息
            'up': f'https://api.bilibili.com/x/space/acc/info?mid={mid}',
            'link': f'https://space.bilibili.com/{mid}',
            # video: 'https://api.bilibili.com/x/space/top/arc?vmid=3129234&jsonp=jsonp',  # 主投稿
            # videos: 'https://api.bilibili.com/x/space/arc/search?mid=3129234&pn=1&ps=25&jsonp=jsonp'  # 所有投稿
            # animate: 'https://space.bilibili.com/ajax/Bangumi/getList?mid=3129234'  # 追番'
            # start: 'https://api.bilibili.com/x/v3/fav/folder/created/list?pn=1&ps=10&up_mid=3129234'
            # 粉丝数等
            'follow': f'https://api.bilibili.com/x/relation/stat?vmid={mid}',
            # 获赞数等
            'video_all': f'https://api.bilibili.com/x/space/upstat?mid={mid}',
            # 直播相关
            'live': f'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={mid}',
        }
        self.rebuild()

    # 重建信息数据
    def rebuild(self):
        self.dic = {}  # 重设地址、以免覆盖
        cont_json = reqjson(self.reallink['up'])['data']
        self.dic['up'] = {
            '姓名': cont_json['name'],
            '签名': cont_json['sign'],
            '头像地址': cont_json['face'],
            '个人空间': self.reallink['link'],
        }
        cont_json = reqjson(self.reallink['follow'])['data']
        self.dic['follow'] = {
            '关注数': cont_json['following'],
            '粉丝数': cont_json['follower'],
        }
        cont_json = reqjson(self.reallink['video_all'])['data']
        self.dic['video'] = {
            '获赞数': cont_json['likes'],
            '播放量': cont_json['archive']['view'],
            '阅读量': cont_json['article']['view'],
        }
        cont_json = reqjson(self.reallink['live'])['data']
        self.dic['live'] = {
            '直播状态': '正在直播' if cont_json['liveStatus'] else '未开播',
            '直播室号': cont_json['roomid'],
            '直播地址': cont_json['url'],
            '直播标题': cont_json['title'],
            '人气值': cont_json['online'],
            '直播封面地址': cont_json['cover'],
        }

    # 可视化输出字符串（基础信息）
    def fns_line(self):
        s = ''
        for v1 in self.dic.values():
            for k2, v2 in v1.items():
                s += ('【%s】：%s\n' % (k2, v2))
            s += '——————————————————————————\n'
        return s

    # 可视化输出字符串（json格式美化）
    def fns_json(self):
        return json.dumps(self.dic, indent=2)

    # 重建信息数据 - 直播监控【单次版】
    def islive(self):
        link = self.reallink['live']
        cont_json = reqjson(link)
        timestr = time.strftime('%Y-%m-%d %H:%M:%S',
                                time.localtime(time.time()))
        return [cont_json['data']['liveStatus'], timestr]

    # 重建信息数据 - 直播监控【调试版】
    def live(self, time_space=30):
        load_list = ['\\', '|', '/', '—']
        load_list_count = 0
        print(f"{self.dic['up']['姓名']} 直播状态：(状态刷新频率：{time_space}s)")
        while not self.islive()[0]:
            timestr = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            time_count = 0
            while True:
                print(
                    f'\r【Up未直播】{timestr} {load_list[load_list_count%4]}', end='')
                time_count += 1
                load_list_count = (load_list_count+1) % 4
                time.sleep(1)
                if(time_count*1 >= time_space):
                    break
        else:
            print('\nUp直播了！ -- %s' % str(timestr))
            print(f"直播地址：{self.dic['live']['直播地址']}")

    def fav_list(self):
        # 查看所有公开的收藏夹的fid（收藏夹id）
        favorite_id = f'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={self.mid}'
        cont_json = reqjson(favorite_id)
        return cont_json['data']['list']

    # 构建收藏夹对象
    def fav(self, index=0):  # 默认获取第一个收藏夹，一般而言是默认收藏夹
        fid = self.fav_list()[index]['id'] # 要注意这里的id才是真正的，fid不是
        return Fid(fid)

    # 构建收藏夹对象 - 对象数列版
    def fav_all(self):
        fav_list = self.fav_list()
        fid_list = []
        for index in range(len(fav_list)):
            fid_list.append(Fid(fav_list[index]['id']))
        return fid_list

    # 生成收藏夹sql
    def sql_fav(self):
        pass
