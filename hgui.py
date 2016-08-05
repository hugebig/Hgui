# encoding=utf8
import swampy.Gui as gui
from radio_monitor import Radio_monitor
from Tkinter import END

def hprint(info='hello hgui!'):
	log_text.insert(END, info + '\n')

cell_voltage = ("单体",[{'高一':4.19},{'高二':4.21},{'高三':4.23},
	{'低一':3.25},{'低二':3.1},{'低三':2.8},
	{'正常':3.31}],hprint)

high_voltage = ("总电压",[{'高一':351.5},{'高二':353},{'高三':355},
	{'低一':270},{'低二':260},{'低三':250},
	{'正常':330}],hprint)

temperature = ("温度",[{'高一':46},{'高二':49},{'高三':51},
	{'低一':-2},{'低二':-15},{'低三':-30},
	{'正常':25}],hprint)

current = ("电流",[{'充一':85},{'充二':110},{'充三':125},
	{'放一':-195},{'放二':-200},{'放三':-205},
	{'正常':0}],hprint)

buttons=['测试启动','测试关闭','测试清理','充电模式',\
'行车模式','加热模式','上电','下电','重启']

hgui = gui.Gui()
hgui.title("Hgui 1.0")
hgui.resizable(False, False)

hgui.row()

hgui.col()
hgui.gr(2)
for each in buttons:
	hgui.bu(each,command=gui.Callable(hprint,each))

def ccs_set():
	hprint('CCS Enable' if ccs.swampy_var.get() else 'CCS Disable')

ccs = hgui.cb(text='CCS',command=ccs_set,onvalue=1, offvalue=0)
hgui.endcol()

log_text = hgui.st().text
log_text.configure(height=10,width=25)

hgui.endrow()

monitors = [cell_voltage,high_voltage,temperature,current]
for each in monitors:
	Radio_monitor(each).add_gui(hgui)
hgui.endcol()

hgui.mainloop()
