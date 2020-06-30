import requests
import json
import sys
import os
# print(sys.path)
# sys.path.append(os.path.abspath("../"))
import avbv as ab


class Aid:
    dic = {}  # 信息集合

    # av号构造完整对象
    def __init__(self, av):
        bv = ab.encode(int(av))
        reallink = 'https://api.bilibili.com/x/web-interface/view?bvid=' + \
            str(bv)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        r = requests.get(reallink, headers=headers)
        # json数据处理
        cont_str = r.text
        cont_json = json.loads(cont_str)
        # 提取数据
        cont_json = cont_json['data']
        self.dic = {
            'video': {
                'bv': ['bv号', cont_json['bvid']],
                'av': ['av号', cont_json['aid']],
                'title': ['标题', cont_json['title']],
                'pic': ['封面地址', cont_json['pic']],
                'descript': ['视频简介', cont_json['desc']],
                'dynamic': ['视频标签', cont_json['dynamic']],
            },
            'owner': {
                'o_name': ['Up主', cont_json['owner']['name']],
                'o_face': ['Up主头像地址', cont_json['owner']['face']],
            },
            'stat': {
                's_view': ['观看数', cont_json['stat']['view']],
                's_danmaku': ['弹幕数', cont_json['stat']['danmaku']],
                's_reply': ['评论数', cont_json['stat']['reply']],
                's_like': ['点赞数', cont_json['stat']['like']],
                's_coin': ['投币数', cont_json['stat']['coin']],
                's_favorite': ['收藏数', cont_json['stat']['favorite']],
                's_share': ['转发数', cont_json['stat']['share']],
            },
        }

    # 可视化输出字符串
    def fns_line(self):
        s = ''
        for v1 in self.dic.values():
            for v2 in v1.values():
                s += ('【%s】：%s\n' % (str(v2[0]), str(v2[1])))
            s += '——————————————————————————\n'
        return s

    # 可视化输出字符串（json格式美化）
    def fns_json(self):
        return json.dumps(self.dic, indent=2)

    # sql代码生成：仅填充av
    def sql_fill_av(self):
        pass

    # sql代码生成根据：填充全部
    def sql_fill_all(self):
        pass

    # sql代码生成：根据av更新信息
    def sql_fill_update(self):
        pass

aid1 = Aid(19349301)
aid2 = Aid(39740049)
print(aid1.fns_line())
print(aid2.fns_line())
print(aid1.fns_line())

# print(aid.fns_json())
