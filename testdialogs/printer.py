import wx

if __name__ == "__main__":
    app = wx.App()
    wx.Printer().PrintDialog(None)
    #dialog.ShowModal()
    #dialog.Destroy()