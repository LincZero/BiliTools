import time
from network.reqjson import reqjson


class Fid:
    mid = '' # 每一个fid都有一个mid，与创立者有关，你可以收藏别人的收藏夹
    fid = '' # 这里的fid其实是media_id，唯一性确定收藏夹，而在json中的那个fid可以重复，没啥用

    def __init__(self, fid):
        self.fid = fid

    def title(self): # 获取收藏夹名称，返回字符串
        medias = f'https://api.bilibili.com/x/v3/fav/resource/list?media_id={self.fid}&pn=1&ps=20'
        cont_json = reqjson(medias)
        return cont_json['data']['info']['title']

    def aid(self): # 获取收藏夹所有aid，返回数组
        pn = 1
        fid = self.fid
        av_list = []
        while True:
            time.sleep(1)
            # 收藏【默认收藏夹】
            medias = f'https://api.bilibili.com/x/v3/fav/resource/list?media_id={fid}&pn={pn}&ps=20'
            pn += 1
            cont_json = reqjson(medias)
            cont_json = cont_json['data']['medias']
            if cont_json is not None:
                print(f'【log: 第{pn-1}页】',end='') # 调试用
                for i in cont_json:
                    av_list.append(i['id'])
            else: # 收藏夹翻页，翻到没有为止调出
                break
        return av_list
            # for i in av_list:
            #     print(i['id'], end=', ')
                # print(f'\n【第{pn-1}页】————————————————')
