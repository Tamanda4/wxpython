
from random import choices

import wx

class MyFrame(wx.Frame):
    def _init_(self):
        super()._init_(parent=None, title='Hello World')
        panel = wx.Panel(self)

        # text control widget
        self.text_ctrl = wx.TextCtrl(panel, pos=(120, 75))
        self.text_ctrl = wx.TextCtrl(panel, value='initial text',pos=(150, 5))
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_PASSWORD,pos=(150, 35))

        #radiobutton widget
        self.gender = wx.RadioButton(panel, label='Male',pos=(5,5))
        self.gender = wx.RadioButton(panel, label='Female',pos=(5,20))

        #STATICTEXT widget
        self.name = wx.StaticText(panel, label="Enter your name:", pos=(5, 75))

        #checkbox widget
        self.Black = wx.CheckBox(panel, label="Black",pos=(5, 40))

        #combobox widget
        items=["Apple", "Rice", "Cheese cake"]
        self.combo = wx.ComboBox(panel, choices= items, pos=(5,95))

        #slider widget
        self.slider = wx.Slider(panel, value= 50, minValue=0, maxValue=100, pos=(5,170))

        # button widget
        self.my_btn = wx.Button(panel, label='Press Me', pos=(5, 150))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
