import requests
import uiautomation as ui
import pyperclip

wx = ui.WindowControl(Name="微信")    # 绑定微信主窗口控件
wx.SwitchToThisWindow()    # 切换窗口
hw = wx.ListControl(Name="会话")    # 绑定会话控件
while True:
    we = hw.TextControl(searchDepth=4)   # 查找未读消息
    try: # 报错处理
        if we.Name:  #假如存在未读消息
            we.Click(simulateMove=False) #点击未读消息
            last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name    # 读取最后一条消息
            response = requests.get(f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={last_msg}")   # 智能接口
            msg = response.json()['content']  # 提取回复内容
            pyperclip.copy(msg.replace('{br}','\n'))   # 替换换行符
            wx.SendKeys("{Ctrl}v",waitTime=0)   # 将结果从粘贴板到文字框
            wx.SendKeys("{Enter}",waitTime=0)   # 点击发送
            wx.TextControl(SubName=msg[:5]).RightClick()    # 通过消息匹配检索会话中的联系人并右击
            ment = ui.MenuBarControl(ClassName="CMenuWnd")    # 匹配右击控件
            ment.TextControl(Name="不显示聊天").Click()  # 右击不显示聊天
    except:
        pass