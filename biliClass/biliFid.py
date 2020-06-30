import time

class Fid:
    uid=''
    fid=''

    def __init__(self, uid, fid):
        self.uid = uid
        self.fid = fid

    def fav(self):
        mid = self.mid
        # 收藏夹id
        # 查看所有公开的收藏夹的fid
        favorite_id = f'https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid={mid}'
        cont_json = self.reqjson(favorite_id)
        fid = cont_json['data']['list'][0]['id']  # 这里只获取默认收藏夹
        pn = 1
        while True:
            time.sleep(1.5)
            # 收藏【默认收藏夹】
            medias = f'https://api.bilibili.com/x/v3/fav/resource/list?media_id={fid}&pn={pn}&ps=20'
            pn += 1
            cont_json = self.reqjson(medias)
            cont_json = cont_json['data']['medias']
            if cont_json is not None:
                for i in cont_json:
                    print(i['id'], end=', ')
                    # print(f'\n【第{pn-1}页】————————————————')
            else:
                break
