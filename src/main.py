#   RUN ME

from widgets import win
from gui_layout import init_gui_layout, assign_btn_funcs
import matplotlib


matplotlib.use('TkAgg')
init_gui_layout()
assign_btn_funcs()
assign_btn_funcs()


win.mainloop()
