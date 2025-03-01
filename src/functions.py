import sympy
import re
from widgets import *
from tkinter import filedialog as fd


#   Decides what action to take depending on the input
def submit():
    exprs = txt_box.get('1.0', tk.END)

    if '=' in exprs:
        compute('solve_equality')
    elif '<' in exprs or '>' in exprs or '≥' in exprs or '≤' in exprs:
        compute('solve_inequality')
    else:
        if has_symbol(exprs):
            plot_expression()
        else:
            compute('calculate_expression')


#   Creates a graph from the input provided, might as well create numerous graphs
def plot_expression():
    exprs = process_input()
    if txt_box.index(tk.INSERT)[0] == '1':
        sympy.plot(sympy.sympify(exprs[0]), xlabel='x', ylabel='f(x)')
    if txt_box.index(tk.INSERT)[0] == '2':
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]), xlabel='x', ylabel='f(x)')
    if txt_box.index(tk.INSERT)[0] == '3':
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]), sympy.sympify(exprs[2]), xlabel='x', ylabel='f(x)')


#   Find the index of the last digit after char ex: √
def digit_index(expr, char): 
	start_index = expr.index(char) + 1
	index = 0
	while True:
		if expr[start_index].isdigit() or expr[start_index].isalpha():
			index = start_index
		else:
			return index
		start_index += 1


#   Remove all terms to the left side and change their signs with the equal sign removed
def process_equation(equation):
	equal_index = equation.index('=')

	expr1 = sympy.sympify(equation[:equal_index])
	expr2 = sympy.sympify(equation[equal_index + 1:])
	return expr1 - expr2


#   Remove all terms to the left side and change their signs with the inequal sign removed
def process_inequality(inequality, char):
    inequality_index = inequality.index(char)
    expr1 = sympy.sympify(inequality[:inequality_index])
    expr2 = sympy.sympify(inequality[inequality_index + 1:])
    final_expr = expr1 - expr2
    coeff = int(final_expr.coeff([x for x in final_expr.free_symbols][0]))
    if coeff < 0:
        if char == '>':
            return final_expr, '<'
        elif char == '<':
            return final_expr, '>'
        elif char == '≥':
            return final_expr, '≤'
        elif char == '≤':
            return final_expr, '≥'
    else:
        return final_expr, char


#   Adds numbers into a list and return that list
def extract_numbers(expr):
	numbers = []
	for char in expr:
		if char.isdigit():
			numbers.append(char)
	return float(''.join(numbers))


#   If the expression has a symobl say x it returns true otherwise false
def has_symbol(expr):
    try:
        right_parentheses = expr.index('(')
        left_parentheses = expr.index(')')

        for char in expr[right_parentheses + 1:left_parentheses]:
            if char.isalpha() and char != 'Ⲡ' and char != 'e':
                return True
        return False
    except:
        for char in expr:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                return True
        return False


#   Seperates numbers and symbols by adding a multiplication sign 
#   so python can understand it for exapmle: (2x) becomes (2*x)
def add_star(expr):
    if 'sin' not in expr and 'cos' not in expr and 'tan' not in expr and 'cot' not in expr and 'log' not in expr:
        for i in range(len(expr)):
            if expr[i].isdigit() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
                expr = expr[:i+1] + '*' + expr[i+1:]
            if expr[i].isalpha() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
                if str(sympy.pi) not in expr:
                    expr = expr[:i+1] + '*' + expr[i+1:]
    return expr


#   Takes the raw input from the user and convert it to sympy epxression
#   so the input can be processed
def process_input():
    exprs = []

    for i in range(1, int(txt_box.index(tk.INSERT)[0]) + 1):
        expr = txt_box.get(f'{i}.0', f'{i+1}.0')
        expr = expr.replace('Ⲡ', str(sympy.pi))
        expr = expr.replace('e', str(sympy.E))
        expr = expr.replace('²', '** 2 ')
        expr = expr.replace('³', '** 3 ')
        expr = add_star(expr)
        if '(' in expr and expr[0] != '(':
            parentheses_indexes = [m.start() for m in re.finditer("\(", expr)]
            for parentheses_index in parentheses_indexes:
                if not expr[parentheses_index - 1].isalpha():
                    expr = expr[:parentheses_index] + '*' + expr[parentheses_index:]
        if '√' in expr:
            square_root_index = digit_index(expr, '√') 
            expr = expr.replace('√', '')
            expr = expr[:square_root_index] + '** 0.5 ' + expr[square_root_index:]
        if '∛' in expr:
            cube_root_index = digit_index(expr, '∛')
            expr = expr.replace('∛', '')
            expr = expr[:cube_root_index] + '** (1/3) ' + expr[cube_root_index:]
        if '°' in expr:
            deg = extract_numbers(expr)
            func = expr[:3]
            expr = f'{func}({sympy.rad(deg)})'
        if '=' in expr:
            expr = process_equation(expr)

        if '>' in str(expr):
            expr = process_inequality(expr, '>')
        elif '≥' in str(expr):
            expr = process_inequality(expr, '≥')
        elif '<' in str(expr):
            expr = process_inequality(expr, '<')
        elif '≤' in str(expr):
            expr = process_inequality(expr, '≤')

        exprs.append(expr)
    return exprs   


#   Performs a computation given the operation required then returns the result
def compute(operation):
    txt_box.config(state='normal')
    exprs = process_input()

    if operation == 'calculate_expression':
        result = f'{round(float(sympy.sympify(exprs[0])), 2)}'
    elif operation == 'solve_equality':
        solutions = None
        if len(exprs) == 1:
            solutions = sympy.solve(sympy.sympify(exprs[0]))
            if len(solutions) == 1:
                solutions = solutions[0]
        elif len(exprs) == 2:
            solutions = sympy.solve((sympy.sympify(exprs[0]), sympy.sympify(exprs[1])))
        
        result = solutions
    elif operation == 'solve_inequality':
        symbol = [symbol for symbol in sympy.solve(exprs[0][0], dict=True)[0].items()][0][0]
        solution = [symbol for symbol in sympy.solve(exprs[0][0], dict=True)[0].items()][0][1]
        result = f'{symbol}{exprs[0][1]}{solution}'
    elif operation == 'factor_expression':
        result = sympy.sympify(exprs[0]).factor()
    elif operation == 'expand_expression':
        result = sympy.sympify(exprs[0]).expand()
    elif operation == 'absolute':
        result = abs(int(sympy.sympify(exprs[0])))    
    elif operation == 'limit':
        value = ent_limit_value.get()
        value = value.replace('∞', str(sympy.S.Infinity))
        limit = sympy.Limit(sympy.sympify(exprs[0]), sympy.Symbol('x'), sympy.sympify(value)).doit()
        result = limit
    elif operation == 'derivative':
        derivative = sympy.Derivative(sympy.sympify(exprs[0]), sympy.Symbol('x')).doit()
        result = derivative
    elif operation == 'integral':
        integral = sympy.Integral(sympy.sympify(exprs[0]), sympy.Symbol('x')).doit()
        result = integral
    elif operation == 'summation':
        x = sympy.Symbol('x')
        summation = sympy.summation(sympy.sympify(exprs[0]), (x, sympy.sympify(ent_summation_start.get()), sympy.sympify(ent_summation_n.get())))
        result = summation

    txt_box.insert(tk.END, f'\n{result}')
    txt_box.config(state='disabled')


#   Removes a char from text box
def remove_char():
    txt_box.config(state='normal')
    txt_box.delete('end-2c', tk.END)
    txt_box.config(state='disabled')


#   Clears all text from text box
def clear_txt():
    txt_box.config(state='normal')
    txt_box.delete('1.0', tk.END)
    txt_box.config(state='disabled')


#   Deletes 'Type here your math problem ...' to let the user add input
def delete_paceholder():
    if txt_box.get(1.0, "end-1c") == 'Type here your math problem ...':
        clear_txt()


#   Adds to the text-box what the button contains in it
def insert_btn_txt(btn):
    delete_paceholder()
    txt_box.config(state='normal')
    txt_box.insert(tk.END, btn['text'])
    txt_box.config(state='disabled')


#   Adds a new line to the text-box
def insert_new_line():
    delete_paceholder()
    txt_box.config(state='normal')
    txt_box.insert(tk.END, '\n')
    txt_box.config(state='disabled')


#   Triggers the symobls panel
#   Ex: If it is visible it will hide it
def show_hide_symbols():
    if frm_symbols.winfo_ismapped():
        frm_standard.pack()
        frm_symbols.pack_forget()
        frm_sci.pack_forget()
    else:
        frm_symbols.pack()
        frm_standard.pack_forget()
        frm_sci.pack_forget() 


#   Triggers the functions panel
#   Ex: If it is visible it will hide it
def show_hide_sci_functions():
    if frm_sci.winfo_ismapped():
        frm_standard.pack()
        frm_sci.pack_forget()
        frm_symbols.pack_forget()
    else:
        frm_standard.pack_forget()
        frm_symbols.pack_forget()
        frm_sci.pack()


#   Opens a filedialog that asks the user for a file path then reutrn the file path
def open_file():
    filetypes = (
        ('Images files', '*.png'),
        ('All files', '*.*')
    )
    file_path = fd.askopenfile(filetypes=filetypes).name
    return file_path


#   Read text from image given the image path
#   If text is clear then returns the text as string
def read_from_image(image_path):
    from PIL import Image 
    from pytesseract import pytesseract 
    # Defining paths to tesseract.exe 
    # and the image we would be using 
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # image_path = r"test.png"
    
    # Opening the image & storing it in an image object 
    img = Image.open(image_path) 
    
    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(img) 
    
    delete_paceholder()
    # Displaying the extracted text
    txt_box.config(state='normal')
    txt_box.insert(tk.END, text[:-1])
    txt_box.config(state='disabled')
