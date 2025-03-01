from functions import *


#   Layout the main navigation panel (submit clear abc ...)
def place_nav_panel():
    txt_box.grid(row=1, column=0, sticky='new')

    i = 0
    for btn in frm_nav_buttons.children:
        frm_nav_buttons.children[btn].grid(row=0, column=i)
        i += 1


#   Layout the standard default panel
def place_std_btns():
    i,j = 0,0
    for btn in frm_standard.children:
        frm_standard.children[btn].grid(row=j, column=i)
        i += 1
        if i == 6:
            i = 0
            j += 1


#   Layout the symbols panel 
def place_symbols_btns():
    i, j = 0, 0
    for btn in frm_symbols.children:
        frm_symbols.children[btn].grid(row=j, column=i)
        i += 1
        if i % 10 == 0:
            j += 1
            i = 0


#   Layout the functions panel (sin cos tan ...)
def place_sci_func_btns():
    ent_summation_n.grid(row=0, column=0)
    btn_summation.grid(row=1, column=0)
    btn_absolute.grid(row=1, column=1)
    btn_imag.grid(row=1, column=2)
    btn_factorial.grid(row=1, column=3)
    ent_summation_start.grid(row=2, column=0)

    i = 0
    for btn in frm_calculus.children:
        frm_calculus.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_expand_factor.children:
        frm_expand_factor.children[btn].grid(row=0, column=i, padx=4)
        i += 1

    i = 0
    for btn in frm_log.children:
        frm_log.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_trig.children:
        frm_trig.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_inequality.children:
        frm_inequality.children[btn].grid(row=0, column=i)
        i += 1


#   Calls the layout functions above and layout the gui elements
def init_gui_layout():
    place_nav_panel()
    place_std_btns()
    place_sci_func_btns()
    place_symbols_btns()

    frm_txtbox.pack()
    frm_nav_buttons.pack()
    frm_standard.pack()

    lbl_trigonometry.pack()
    frm_trig.pack()
    lbl_inequality.pack()
    frm_inequality.pack()
    lbl_calculus.pack()
    frm_calculus.pack()
    lbl_log.pack()
    frm_log.pack()
    lbl_other.pack()
    frm_other_sci.pack()
    frm_expand_factor.pack()


#   Make every button functional by assigning a function to it
def assign_btn_funcs():
    btn_log.configure(command=lambda: insert_btn_txt(btn_log))

    btn_e.configure(command=lambda: insert_btn_txt(btn_e))
    btn_factorial.configure(command=lambda: insert_btn_txt(btn_factorial))
    btn_absolute.configure(command=lambda: compute('absolute'))
    btn_imag.configure(command=lambda: insert_btn_txt(btn_imag))
    btn_derivative.configure(command=lambda: compute('derivative'))
    btn_integral.configure(command=lambda: compute('integral'))

    btn_greater.configure(command=lambda: insert_btn_txt(btn_greater))
    btn_greater_equal.configure(command=lambda: insert_btn_txt(btn_greater_equal))
    btn_less.configure(command=lambda: insert_btn_txt(btn_less))
    btn_less_equal.configure(command=lambda: insert_btn_txt(btn_less_equal))

    btn_submit.configure(command=lambda: submit())
    btn_remove.configure(command=lambda: remove_char())
    btn_clear_txt.configure(command=lambda: clear_txt())
    btn_new_line.configure(command=lambda: insert_new_line())
    btn_sci_functions.configure(command=lambda: show_hide_sci_functions())
    btn_symbols.configure(command=lambda: show_hide_symbols())
    btn_open_image.config(command=lambda: read_from_image(open_file()))

    btn_expand.configure(command=lambda: compute('expand_expression'))
    btn_factor.configure(command=lambda: compute('factor_expression'))

    btn_limit.configure(command=lambda: compute('limit'))
    btn_insert_infinity.configure(command=lambda: ent_limit_value.insert(tk.END, '∞'))

    btn_summation.configure(command=lambda: compute('summation'))

    for btn in frm_trig.children:
        frm_trig.children[btn]['command'] = lambda x=frm_trig.children[btn]: insert_btn_txt(x)


    for btn in frm_standard.children:
        frm_standard.children[btn]['command'] = lambda x=frm_standard.children[btn]: insert_btn_txt(x)

    for btn in frm_symbols.children:
        frm_symbols.children[btn]['command'] = lambda x=frm_symbols.children[btn]: insert_btn_txt(x)

