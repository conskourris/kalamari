from Tkinter import *
from tkFileDialog import *

import ply.lex as lex
import ply.yacc as yacc 
import sys
import os

filename = None;


######################################
###              Lexer             ###
######################################


tokens = [
	'NUM',
    'ACT',
	'DIVIDER',
    'SPACE',
    'NLINE',
    'BAR',
    'NSTRNG',
	]

t_DIVIDER = r'\;'
t_SPACE = r'\-'
t_NLINE = r'\n'
t_BAR = r'\/'
t_NSTRNG = r'\,'

t_ignore =r' '

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ACT(t):
        r'[sphb]'
        t.type = 'ACT'
        return t

def t_error(t):
	print("Illegal Character", t)
	t.lexer.skip(1)


######################################
###             Parser             ###
######################################


def p_out(p):
    '''
    out : note
        | action
        | gap
    '''
    run(p[1])

def p_note(p):
	'''
	note : NUM DIVIDER NUM
         | chord DIVIDER chord
	'''
	p[0] = (p[1], p[3])

def p_action(p):
    '''
    action : NUM DIVIDER NUM ACT NUM
    '''
    p[0] = (p[1], str(p[3])+str(p[4])+str(p[5]))

def p_chord(p):
    '''
    chord : chord NSTRNG NUM
    '''
    if type(p[1]) is tuple:
        temp = list(p[1])
        temp.append(p[3])
        p[0] = tuple(temp)
    else:
        p[0] = (p[1], p[3])

def p_chord_num(p):
    '''
    chord : NUM
    '''
    p[0] = p[1]

def p_gap(p):
    '''
    gap : SPACE 
        | BAR
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error found!", p)

def run(p):
    global output
    if p[0]:
        if p[0] == '-':
            output = ['--','--','--','--','--','--']

        elif p[0] == '/':
            output = ['|-', '|-', '|-', '|-', '|-', '|-']

        elif p[0] == 1:
            output = [
            str(p[1])+'-', 
            '{}'.format('-'*(len(str(p[1]))+1)), 
            '{}'.format('-'*(len(str(p[1]))+1)), 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1))
                ]
        elif p[0] == 2:  
            output = [ 
            '{}'.format('-'*(len(str(p[1]))+1)),
            str(p[1])+'-',
            '{}'.format('-'*(len(str(p[1]))+1)), 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1))
            ]
        elif p[0] == 3:      
            output = [ 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            str(p[1])+'-',
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1))
            ]
        elif p[0] == 4:      
            output = [ 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            str(p[1])+'-',
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1))
            ]
        elif p[0] == 5:      
            output = [ 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            str(p[1])+'-',
            '{}'.format('-'*(len(str(p[1]))+1))
            ]
        elif p[0] == 6:      
            output = [ 
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            '{}'.format('-'*(len(str(p[1]))+1)),
            str(p[1])+'-',
            ]
        elif type(p[0]) is tuple:
            max_len = len(str(max(p[1])))
            pot_out = []
            
            if 1 in p[0]:
                ind = p[0].index(1)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            if 2 in p[0]:
                ind = p[0].index(2)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            if 3 in p[0]:
                ind = p[0].index(3)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            if 4 in p[0]:
                ind = p[0].index(4)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            if 5 in p[0]:
                ind = p[0].index(5)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            if 6 in p[0]:
                ind = p[0].index(6)
                fret = p[1][ind]
                diff = max_len - len(str(fret)) + 1
                pot_out.append(str(fret)+('-'*diff))
            else:
                pot_out.append('-'*(max_len+1))

            output = pot_out


lexer = lex.lex()

parser = yacc.yacc()


######################################
###            Tkinter             ###
######################################


def new_file():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

# def save_file():
# 	global filename
# 	t = text.get(0.0, END)
# 	f = open(filename, 'w')
# 	f.write(t)
# 	f.close()

def save_source():
	f = asksaveasfile(mode='w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Oops!", message="Unable to save file...")

def save_tabs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = out.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")

def open_file():
	f = askopenfile(mode='r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)


def compile_text():
    global output, out

    output = []
    all_text = ['', '', '', '', '', '']

    source = text.get(0.0, END)
    print(source)

    print('\nTokens \n-----------------------')

    for char in source:
        lexer.input(char)
        tok = lexer.token()
        print(tok)

    source = source.replace(" ", "")
    lines = source.split('\n')

    out_file = open("output.txt", 'w')

    for line in lines:
        if line:
            parser.parse(line)
            for item in range(len(output)):
                all_text[item] += output[item]

    empty = False
    while not empty:
        string = 0
        out_file.write('\n\n\n')
        for line in all_text:
            if len(line) <= 68:
                out_file.write(line)
                empty = True

            else:
                out_file.write(line[0:68])
                all_text[string] = line[68:]
                string += 1

            out_file.write('\n')

    print('\n--- Compiled Succesfully! ---')

    
    try:
        out_file = open("output.txt", 'r')
        t = out_file.read()
        out.delete(0.0, END)
        out.insert(0.0, t)

    except TclError:
        sroot = Toplevel(root)
        sroot.title("Tabs")
        sroot.minsize(width=600, height=500)
        sroot.maxsize(width=600, height=500)

        out = Text(sroot, width=600, height=500)
        out.pack()

        out_file = open("output.txt", 'r')
        t = out_file.read()
        out.delete(0.0, END)
        out.insert(0.0, t)




######################################
###              Main              ###
######################################


root = Tk()
root.title("Source")
root.geometry('300x500+200+200')
root.resizable(True, True)

text = Text(root, width=50, height=1000)
text.pack()

sroot = Toplevel(root)
sroot.title("Tabs")
sroot.geometry('600x500+500+200')
sroot.resizable()

out = Text(sroot, width=100, height=1000)
out.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
# filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save Source...", command=save_source)
filemenu.add_command(label="Save Tabs...", command=save_tabs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

buildmenu = Menu(menubar)
buildmenu.add_command(label="Compile", command=compile_text)
menubar.add_cascade(label="Build", menu=buildmenu)

root.config(menu=menubar)
root.mainloop()




