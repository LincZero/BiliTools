# 正式bili小程序
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import biliClass.biliAid as biliv
import biliClass.biliMid as biliu

win = tk.Tk()
win.title('BiliTools (测试版v0.2)')
# win.geometry('400x400')

# 菜单部分
# menubar = tk.Menu(win)

# menu_set = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='首选项',menu=menu_set)
# menu_set.add_command(label='设置')
# menu_set.add_command(label='Open')
# menu_set.add_command(label='Save')

# menu_about = tk.Menu(menubar,tearoff=0)
# menubar.add_cascade(label='关于',menu=menu_about)
# menu_about.add_command(label='设置')
# menu_about.add_command(label='Open')
# menu_about.add_command(label='Save')

# win.config(menu=menubar)

# 标签控制部分
tabControl = ttk.Notebook(win)

tab_vdo = ttk.Frame(tabControl)
tabControl.add(tab_vdo, text=' 视频页 ')
tab_user = ttk.Frame(tabControl)
tabControl.add(tab_user, text=' 用户页 ')
tab_about = ttk.Frame(tabControl)
tabControl.add(tab_about, text=' 关于 ')

tabControl.pack(expand=1, fill="both")

# 框架1-------------------------
fram_vdo = ttk.LabelFrame(tab_vdo, text=' 视频页 ')
fram_vdo.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

# 控件部分
label_aid = tk.Label(fram_vdo, text='请输入b站av号: ')
label_aid.grid(column=0, row=0)
tips_aid = tk.StringVar()
tips_aid.set('19349301')
input_aid = tk.Entry(fram_vdo, textvariable=tips_aid)
input_aid.focus()
input_aid.grid(column=1, row=0)


def aid_mess():
    av = input_aid.get()
    aid = biliv.Aid(int(av))
    str_aidmess.set(aid.fns_line())


button = tk.Button(fram_vdo, text='查询', command=aid_mess)
button.grid(column=2, row=0, padx=12, pady=10)

# 控制台
fram_vdo_ct = ttk.LabelFrame(tab_vdo, text=' [控制台] 输出信息 ')
fram_vdo_ct.grid(column=0, row=1, padx=8, pady=4, sticky=tk.W)

str_aidmess = tk.StringVar()
str_aidmess.set('')
mess_aid = tk.Message(fram_vdo_ct, textvariable=str_aidmess)
mess_aid.grid(column=0, row=0, pady=4, sticky=tk.W)

# 框架2-------------------------
fram_user = ttk.LabelFrame(tab_user, text=' 用户页 ')
fram_user.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

# 控件部分
label_mid = tk.Label(fram_user, text='请输入b站用户id: ')
label_mid.grid(column=0, row=0)
tips_mid = tk.StringVar()
tips_mid.set('3129234')
input_mid = tk.Entry(fram_user, textvariable=tips_mid)
input_mid.focus()
input_mid.grid(column=1, row=0)


def mid_mess():
    global mid
    md = input_mid.get()
    mid = biliu.Mid(int(md))
    str_midmess.set(mid.fns_line())


button = tk.Button(fram_user, text='查询', command=mid_mess)
button.grid(column=2, row=0, padx=10, pady=5)

# 滑动条
fram_user_live = ttk.LabelFrame(tab_user, text=' 直播监控【tips:频率请不要调得过低，以免ip被封】 ')
fram_user_live.grid(column=0, row=2, padx=8, pady=4, sticky=tk.W)


def set_livetime(v):
    global livetime
    livetime = int(v)*1000


sc = tk.Scale(fram_user_live, label='直播监控刷新频率(s/次)', from_=5, to=60,
            orient=tk.HORIZONTAL, length=250,
            showvalue=1, tickinterval=10, resolution=1,  # 数值显示类参数
            command=set_livetime)  # 这里很神奇的就传参了
sc.set(10)
livetime = 10000  # 控制直播监控的刷新频次，要写在set后面
sc.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

b_live = 0  # 是否监控直播


def mid_live():
    global mid
    md = input_mid.get()
    mid = biliu.Mid(int(md))
    global b_live
    b_live = not b_live
    loop_live()


def loop_live():
    global mid
    global b_live
    global livetime
    islive = mid.islive()

    if (b_live):
        if (not islive[0]):
            str_midmess.set(f"监控对象：{mid.dic['up']['姓名']}\n【Up未直播】{islive[1]}")
            win.after(int(livetime), loop_live)
        else:
            str_midmess.set(f"监控对象：{mid.dic['up']['姓名']}\n【Up直播了】{islive[1]}")
            tk.messagebox.showinfo(title='监控信息', message='您监控的Up直播了！')
    else:
        str_midmess.set('已关闭直播监控')


button = tk.Button(fram_user_live, text='直播监视', command=mid_live)
button.grid(column=1, row=0, padx=10, pady=5)

# 控制台
fram_user_ct = ttk.LabelFrame(tab_user, text=' [控制台] 输出信息 ')
fram_user_ct.grid(column=0, row=3, padx=8, pady=4, sticky=tk.W)

#     img_mid = PhotoImage(file=mid.dic['up']['头像地址'])
# img_mid = tk.PhotoImage(file="./resource/img/folder.jpg")
# img_mid = tk.PhotoImage(src="i0.hdslb.com/bfs/face/152658d7a5b74dc84b7bf9cc509df228349572ca.jpg")
# label = tk.Label(fram_user_ct,image=img_mid)
# label.image = img_mid
# label.grid(column=0, row=0)

str_midmess = tk.StringVar()
str_midmess.set('')
mess_mid = tk.Message(fram_user_ct, textvariable=str_midmess, width=500)
mess_mid.grid(column=0, row=0, pady=4, sticky=tk.W)

# 框架3-------------------------
fram_about = ttk.LabelFrame(tab_about, text=' 关于 ')
fram_about.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W)

str_about = tk.StringVar()
str_about.set('''biliToos

版本信息：测试版 v0.2
开发者：  Linc
反馈联系：QQ762699299
''')
mess_ablout = tk.Message(fram_about, textvariable=str_about, width=500)
mess_ablout.grid(column=0, row=0)

win.mainloop()
