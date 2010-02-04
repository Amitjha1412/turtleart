# -*- coding: utf-8 -*-
#Copyright (c) 2010, Walter Bender

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from gettext import gettext as _

#
# sprite layers
#

HIDE_LAYER = 100
CANVAS_LAYER = 500
OVERLAY_LAYER = 525
TURTLE_LAYER = 550
BLOCK_LAYER = 600
CATEGORY_LAYER = 700
TAB_LAYER = 710
STATUS_LAYER = 900
TOP_LAYER = 1000

#
# block palette categories
#

PALETTE_NAMES = ['turtle', 'pen', 'colors', 'numbers', 'flow', 'blocks',
                 'extras', 'portfolio', 'trash']

PALETTES = [['forward', 'back', 'clean', 'left', 'right', 'show', 
             'seth', 'setxy', 'heading', 'xcor', 'ycor', 'setscale',
              'arc', 'scale'],
            ['penup','pendown', 'setpensize', 'fillscreen', 'pensize',
             'settextsize', 'setcolor', 'setshade', 'textsize', 'color',
             'shade'],
            [ 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple'],
            ['plus2', 'minus2', 'product2',
             'division2', 'identity2', 'remainder2', 'sqrt', 'random',
             'number', 'greater2', 'less2', 'equal2', 'not', 'and2', 'or2'],
            ['wait', 'forever', 'repeat', 'if', 'ifelse', 'hspace',
             'vspace', 'stopstack'],
            ['hat1', 'stack1', 'hat', 'hat2', 'stack2', 'stack',
             'storeinbox1', 'storeinbox2', 'string', 'box1', 'box2', 'box',
             'storein', 'start'],
            ['kbinput', 'push', 'printheap', 'keyboard', 'pop', 'clearheap',
             'myfunc',  'nop', 'leftpos', 'toppos', 'width', 'rightpos',
             'bottompos', 'height', 'addturtle', 'print'],
            ['journal', 'audio', 'description', 'templatelist', 'template1x1a',
             'template1x1', 'template1x2', 'template2x1', 'template2x2',
             'hideblocks', 'showblocks'],
            ['restore']]

#
# block style attributes
#

COLORS = [["#00FF00","#00A000"], ["#00FFFF","#00A0A0"], ["#00FFFF","#00A0A0"],
          ["#FF00FF","#A000A0"], ["#FFC000","#A08000"], ["#FFFF00","#A0A000"],
          ["#FF0000","#A00000"], ["#0000FF","#0000FF"], ["#FFFF00","#A0A000"]]

BOX_COLORS = {'red':["#FF0000","#A00000"],'orange':["#FFD000","#AA8000"],
              'yellow':["#FFFF00","#A0A000"],'green':["#00FF00","#008000"],
              'cyan':["#00FFFF","#00A0A0"],'blue':["#0000FF","#000080"],
              'purple':["#FF00FF","#A000A0"]}

PALETTE_HEIGHT = 120
PALETTE_WIDTH = 180
SELECTOR_WIDTH = 55
ICON_SIZE = 55
SELECTED_COLOR = "#0000FF"
SELECTED_STROKE_WIDTH = 1.5
STANDARD_STROKE_WIDTH = 1.0
THUMB_W = 80
THUMB_H = 60
PYTHON_X = 17
PYTHON_Y = 8
MEDIA_X = 37
MEDIA_Y = 6
TEMPLATE_X = 24
TEMPLATE_Y = 18
PIXBUF_X = 17
PIXBUF_Y = 2
BLOCK_SCALE = 2.0
PALETTE_DEFAULT_SCALE = 1.5
PALETTE_SCALE = {'template2x2':1.0, 'template1x2':1.0}

#
# block style definitions
#
BASIC_STYLE_HEAD = ['start', 'hat1', 'hat2', 'restore']
BASIC_STYLE_HEAD_1ARG = ['hat']
BASIC_STYLE_TAIL = ['stopstack']
BASIC_STYLE = ['clean', 'penup', 'pendown', 'stack1', 'stack2', 'vspace',
    'hideblocks', 'showblocks', 'clearheap', 'printheap', 'kbinput']
BASIC_STYLE_1ARG = ['forward', 'back', 'left', 'right', 'seth', 'show',
    'setscale', 'setpensize', 'setcolor', 'setshade', 'print',
    'settextsize', 'settextcolor', 'print', 'wait', 'storeinbox1',
    'storeinbox2', 'wait', 'stack', 'push', 'nop', 'addturtle']
BASIC_STYLE_2ARG = ['arc', 'setxy', 'fillscreen', 'storein']
BOX_STYLE = ['number', 'xcor', 'ycor', 'heading', 'pensize', 'color', 'shade',
    'textcolor', 'textsize', 'box1', 'box2', 'string', 'leftpos', 'scale',
    'toppos', 'rightpos', 'bottompos', 'width', 'height', 'pop', 'keyboard',
    'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
BOX_STYLE_MEDIA =  ['description', 'audio', 'journal']
NUMBER_STYLE = ['plus2', 'product2', 'myfunc']
NUMBER_STYLE_BLOCK = ['random']
NUMBER_STYLE_PORCH = ['minus2', 'division2', 'remainder2']
NUMBER_STYLE_1ARG = ['sqrt', 'identity2']
NUMBER_STYLE_1STRARG = ['box']
COMPARE_STYLE = ['greater2', 'less2', 'equal2']
BOOLEAN_STYLE = ['and2', 'or2']
NOT_STYLE = ['not']
FLOW_STYLE = ['forever', 'hspace']
FLOW_STYLE_1ARG = ['repeat']
FLOW_STYLE_BOOLEAN = ['if']
FLOW_STYLE_ELSE = ['ifelse']
PORTFOLIO_STYLE_2x2 = ['template2x2']
BULLET_STYLE = ['templatelist']
PORTFOLIO_STYLE_1x1 = ['template1x1', 'template1x1a']
PORTFOLIO_STYLE_2x1 = ['template2x1']
PORTFOLIO_STYLE_1x2 = ['template1x2']


#
# Macros (groups of blocks)
#
MACROS = {
    'kbinput':[[0, 'forever', 0, 0, [None, 1, None]],
               [1, 'kbinput', 0, 0, [0, 2]],
               [2, 'vspace', 0, 0, [1, 3]],
               [3, 'if', 0, 0, [2, 4, 7, 8]],
               [4, 'greater2', 0, 0, [3, 5, 6, None]],
               [5, 'keyboard', 0, 0, [4, None]],
               [6, ['number', '0'], 0, 0, [4, None]],
               [7, 'stopstack', 0, 0, [3, None]],
               [8, 'vspace', 0, 0, [3, 9]],
               [9, 'wait', 0, 0, [8, 10, None]],
               [10, ['number', '1'], 0, 0, [9, None]]]
         }

#
# blocks that are expandable
#
EXPANDABLE = ['vspace', 'hspace', 'templatelist', 'identity2']

#
# Old block styles that need dock adjustments
#
OLD_DOCK = ['and', 'or']

#
# blocks that contain media
#
CONTENT_BLOCKS = ['number', 'string', 'description', 'audio', 'journal']

#
# block name dictionary used for labels
#
BLOCK_NAMES = {
    'addturtle':[_('turtle')],
    'and2':[_('and')],
    'arc':[_('arc'),_('angle'),_('radius')],
    'audio':[' '],
    'back':[_('back')],
    'blue':[_('blue')],
    'bottompos':[_('bottom')],
    'box':[_('box')],
    'box1':[_('box 1')],
    'box2':[_('box 2')],
    'clean':[_('clean')],
    'clearheap':[_('empty heap')],
    'color':[_('color')],
    'cyan':[_('cyan')],
    'division2':['/'],
    'equal2':['='],
    'fillscreen':[_('fill screen'),_('color'),_('shade')],
    'forever':[_('forever')],
    'forward':[_('forward')],
    'greater2':[">"],
    'green':[_('green')],
    'hat':[_('action')],
    'hat1':[_('action 1')],
    'hat2':[_('action 2')],
    'heading':[_('heading')],
    'height':[_('height')],
    'hideblocks':[_('hide blocks')],
    'hspace':[' '],
    'identity2':['←'],
    'if':[' ',_('if'),_('then')],
    'ifelse':[' ',_('if'),_('then else')],
    'journal':[' '],
    'kbinput':[_('query keyboard')],
    'keyboard':[_('keyboard')],
    'left':[_('left')],
    'leftpos':[_('left')],
    'less2':['<'],
    'minus2':['–'],
    'myfunc':[_('Python'),_('code'),_('value')],
    'nop':[_(' ')],
    'not':[_('not')],
    'number':['100'],
    'orange':[_('orange')],
    'or2':[_('or')],
    'pendown':[_('pen down')],
    'pensize':[_('pen size')],
    'penup':[_('pen up')],
    'plus2':['+'],
    'pop':[_('pop')],
    'printheap':[_('show heap')],
    'print':[_('print')],
    'product2':['×'],
    'purple':[_('purple')],
    'push':[_('push')],
    'random':[_('random'),_('min'),_('max')],
    'red':[_('red')],
    'remainder2':[_('mod')],
    'repeat':[' ',_('repeat')],
    'restore':[_('restore')],
    'rightpos':[_('right')],
    'right':[_('right')],
    'scale':[_('scale')],
    'setcolor':[_('set color')],
    'seth':[_('set heading')],
    'setpensize':[_('set pen size')],
    'setscale':[_('set scale')],
    'setshade':[_('set shade')],
    'settextsize':[_('set text size')],
    'setxy':[_('set xy'),_('x'),_('y')],
    'shade':[_('shade')],
    'show':[_('show')],
    'showblocks':[_('show blocks')],
    'sqrt':['√'],
    'stack':[_('action')],
    'stack1':[_('action 1')],
    'stack2':[_('action 2')],
    'start':[_('start')],
    'stopstack':[_('stop action')],
    'storein':[_('store in')],
    'storeinbox1':[_('store in box 1')],
    'storeinbox2':[_('store in box 2')],
    'string':[_('text')],
    'template1x1':[' '],
    'template1x1a':[' '],
    'template1x2':[' '],
    'template2x1':[' '],
    'template2x2':[' '],
    'templatelist':[' '],
    'textsize':[_('text size')],
    'toppos':[_('top')],
    'turtle':[_('turtle')],
    'vspace':[' '],
    'wait':[_('wait')],
    'width':[_('width')],
    'xcor':[_('xcor')],
    'ycor':[_('ycor')],
    'yellow':[_('yellow')]}

#
# Logo primitives
#

PRIMITIVES = {
    'addturtle':'turtle',
    'and2':'and',
    'arc':'arc',
    'back':'back',
    'blue':'blue',
    'bottompos':'bpos',
    'box1':'box1',
    'box2':'box2',
    'box':'box',
    'clean':'clean',
    'clearheap':'clearheap',
    'color':'color',
    'cyan':'cyan',
    'division2':'division',
    'equal2':'equal?',
    'fillscreen':'fillscreen',
    'forever':'forever',
    'forward':'forward',
    'greater2':'greater?',
    'green':'green',
    'hat':'nop3',
    'hat1':'nop1',
    'hat2':'nop2',
    'heading':'heading',
    'height':'vres',
    'hideblocks':'hideblocks',
    'hspace':'nop',
    'identity2':'id',
    'if':'if',
    'ifelse':'ifelse',
    'kbinput':'kbinput',
    'keyboard':'keyboard',
    'left':'left',
    'leftpos':'lpos',
    'less2':'less?',
    'templatelist':'bullet',
    'minus2':'minus',
    'myfunc':'myfunc',
    'nop':'userdefined',
    'not':'not',
    'orange':'orange',
    'or2':'or',
    'pendown':'pendown',
    'pensize':'pensize',
    'penup':'penup',
    'plus2':'plus',
    'pop':'pop',
    'printheap':'printheap',
    'print':'print',
    'product2':'product',
    'purple':'purple',
    'push':'push',
    'random':'random',
    'red':'red',
    'remainder2':'mod',
    'repeat':'repeat',
    'rightpos':'rpos',
    'right':'right',
    'scale':'scale',
    'setcolor':'setcolor',
    'seth':'seth',
    'setpensize':'setpensize',
    'setscale':'setscale',
    'setshade':'setshade',
    'settextsize':'settextsize',
    'settextcolor':'settextcolor',
    'setxy':'setxy',
    'shade':'shade',
    'show':'show',
    'showblocks':'showblocks',
    'sqrt':'sqrt',
    'stack':'stack',
    'stack1':'stack1',
    'stack2':'stack2',
    'start':'start',
    'stopstack':'stopstack',
    'storein':'storeinbox',
    'storeinbox1':'storeinbox1',
    'storeinbox2':'storeinbox2',
    'template1x1':'t1x1',
    'template1x1a':'t1x1a',
    'template1x2':'t1x2',
    'template2x1':'t2x1',
    'template2x2':'t2x2',
    'textsize':'textsize',
    'toppos':'tpos',
    'vspace':'nop',
    'wait':'wait',
    'width':'hres',
    'xcor':'xcor',
    'ycor':'ycor',
    'yellow':'yellow'}

#
# block default values
#

DEFAULTS = {
    'addturtle':[1],
    'arc':[90,100],
    'audio':[None],
    'back':[100],
    'box':[_('my box')],
    'description':[None],
    'fillscreen':[60,80],
    'forward':[100],
    'hat':[_('action')],
    'if':[None, None, 'vspace'],
    'ifelse':[None,'vspace', None, 'vspace'],
    'journal':[None],
    'left':[90],
    'media':[None],
    'myfunc':[_('x'),100],
    'nop':[100],
    'number':[100],
    'random':[0,100],
    'repeat':[4, None, 'vspace'],
    'right':[90],
    'setcolor':[0],
    'setheading':[0],
    'setpensize':[5],
    'setscale':[33],
    'setshade':[50],
    'settextsize':[32],
    'setxy':[0,0],
    'show':[_('text')],
    'stack':[_('action')],
    'storeinbox1':[100],
    'storeinbox2':[100],
    'storein':[_('my box'),100],
    'string':[_('text')],
    'template1x1':[_('Title'), 'None'],
    'template1x1a':[_('Title'), 'None'],
    'template1x2':[_('Title'), 'None', 'None'],
    'template2x1':[_('Title'), 'None', 'None'],
    'template2x2':[_('Title'), 'None', 'None', 'None', 'None'],
    'templatelist':[_('Title'), '∙ '],
    'wait':[1]}

#
# Blocks that can interchange strings and numbers for their arguments
#
STRING_OR_NUMBER_ARGS = ['plus2', 'equal2', 'less2', 'greater2', 'box',
                         'template1x1', 'template1x2', 'template2x1',
                         'template2x2', 'template1x1a', 'templatelist', 'nop',
                         'print', 'stack', 'hat']

CONTENT_ARGS = ['show', 'push', 'storein', 'storeinbox1', 'storeinbox2']

#
# Status blocks
#

MEDIA_SHAPES = ['audiooff', 'audioon', 'audiosmall',
                'journaloff', 'journalon', 'journalsmall',
                'descriptionoff', 'descriptionon', 'descriptionsmall',
                'pythonoff', 'pythonon', 'pythonsmall',
                'list', '1x1', '1x1a', '2x1', '1x2', '2x2']

OVERLAY_SHAPES = ['Cartesian', 'polar']

STATUS_SHAPES = ['status', 'info', 'nostack', 'noinput', 'emptyheap',
                 'emptybox', 'nomedia', 'nocode', 'overflowerror',
                 'syntaxerror']

#
# Legacy names
#
OLD_NAMES = {'product':'product2', 'storeinbox':'storein',
             'division':'division2', 'plus':'plus2', 'and':'and2', 'or':'or2',
             'less':'less2', 'greater':'greater2', 'equal':'equal2',
             'remainder':'remainder2', 'identity':'identity2',
             'division':'division2', 'if else':'if', 'audiooff':'audio',
             'descriptionoff':'description','template3':'templatelist',
             'template1':'template1x1', 'template2':'template2x1',
             'template6':'template1x2', 'template7':'template2x2', 
             'template4':'template1x1a', 'hres':'width', 'vres':'height' }

#
# Define the relative size and postion of media objects
#                    (w,   h,   x,      y,     dx, dy)
#
TEMPLATES = {'t1x1': (0.5, 0.5, 0.0625, 0.125, 1.05, 0),
             't2z1': (0.5, 0.5, 0.0625, 0.125, 1.05, 1.05),
             't1x2': (0.45, 0.45, 0.0625, 0.125, 1.05, 1.05),
             't2x2': (0.45, 0.45, 0.0625, 0.125, 1.05, 1.05),
             't1x1a': (0.9, 0.9, 0.0625, 0.125, 0, 0),
             'bullet': (1, 1, 0.0625, 0.125, 0, 0.1),
             'insertimage': (0.333, 0.333)}

#
# Names for blocks without names for popup help
#
SPECIAL_NAMES = {
    'audio':_('audio'),
    'division2':_('divide'),
    'equal2':_('equal'),
    'greater2':_('greater than'),
    'hspace':_('horizontal space'),
    'identity2':_('identity'),
    'if':_('if then'),
    'ifelse':_('if then else'),
    'journal':_('journal'),
    'less2':_('less than'),
    'minus2':_('minus'),
    'myfunc':_('Python code'),
    'nop':_('Python code'),
    'number':_('number'),
    'plus2':_('plus'),
    'product2':_('multiply'),
    'sqrt':_('square root'),
    'template1x1':_('presentation 1x1'),
    'template1x1a':_('presentation 1x1'),
    'template1x2':_('presentation 1x2'),
    'template2x1':_('presentation 2x1'),
    'template2x2':_('presentation 2x2'),
    'templatelist':_('presentation bulleted list'),
    'textsize':_('text size'),
    'vspace':_('vertical space')}

#
# Help messages
#
HELP_STRINGS = {
    'addturtle':_("choose which turtle to command"),
    'and2':_("logical AND operator"),
    'arc':_("move turtle along an arc"),
    'audio':_("Sugar Journal audio object"),
    'back':_("move turtle backward"),
    'blocks':_("palette of variable blocks"),
    'bottompos':_("ycor of bottom of screen"),
    'box1':_("variable 1 (numeric value)"),
    'box2':_("variable 2 (numeric value)"),
    'box':_("named variable (numeric value)"),
    'clean':_("clear the screen and reset the turtle"),
    'clearheap':_("empty FILO"),
    'color':_("holds current pen color (can be used in place of a number block)"),
    'colors':_("a palette of pen colors"),
    'description':_("Sugar Journal description field"),
    'division2':_("divides top numeric input (numerator) by bottom numeric input (denominator)"),
    'equal2':_("logical equal-to operator"),
    'extras':_("palette of extra options"),
    'fillscreen':_("fills the background with (color, shade)"),
    'flow':_("palette of flow operators"),
    'forever':_("loop forever"),
    'forward':_("move turtle forward"),
    'greater2':_("logical greater-than operator"),
    'hat1':_("top of action 1 stack"),
    'hat2':_("top of action 2 stack"),
    'hat':_("top of nameable action stack"),
    'heading':_("holds current heading value of the turtle (can be used in place of a number block)"),
    'hideblocks':_("declutter canvas by hiding blocks"),
    'width':_("the canvas width"),
    'hspace':_("jog stack right"),
    'identity2':_("identity operator used for extending blocks"),
    'ifelse':_("if-then-else operator that uses boolean operators from Numbers palette"),
    'if':_("if-then operator that uses boolean operators from Numbers palette"),
    'journal':_("Sugar Journal media object"),
    'kbinput':_("query for keyboard input (results stored in keyboard block)"),
    'keyboard':_("holds results of query-keyboard block"),
    'leftpos':_("xcor of left of screen"),
    'left':_("turn turtle counterclockwise (angle in degrees)"),
    'less2':_("logical less-than operator"),
    'minus2':_("subtracts bottom numeric input from top numeric input"),
    'myfunc':_("a programmable block: add your own math equation in the block, e.g., sin(x)"),
    'nop':_("runs code found in the tamyblock.py module found in the Journal"),
    'not':_("logical NOT operator"),
    'numbers':_("palette of numeric operators"),
    'number':_("used as numeric input in mathematic operators"),
    'or':_("logical OR operator"),
    'orientation':_("changes the orientation of the palette of blocks"),
    'pendown':_("turtle will draw when moved"),
    'pen':_("palette of pen commands"),
    'pensize':_("holds current pen size (can be used in place of a number block)"),
    'penup':_("turtle will not draw when moved"),
    'plus2':_("adds two alphanumeric inputs"),
    'pop':_("pop value off FILO"),
    'portfolio':_("palette of presentation templates"),
    'print':_("prints value in status block at bottom of the screen"),
    'printheap':_("show FILO in status block"),
    'product2':_("multiplies two numeric inputs"),
    'push':_("push value onto FILO (first-in last-out) heap"),
    'random':_("returns random number between minimum (top) and maximum (bottom) values"),
    'remainder2':_("modular (remainder) operator"),
    'repeat':_("loop specified number of times"),
    'restore':_("restore blocks from trash"),
    'rightpos':_("xcor of right of screen"),
    'right':_("turn turtle clockwise (angle in degrees)"),
    'scale':_("holds current scale value (can be used in place of a number block)"),
    'setcolor':_("set color of the line drawn by the turtle"),
    'seth':_("set the heading of the turtle (0 is towards the top of the screen.)"),
    'setpensize':_("set size of the line drawn by the turtle"),
    'setscale':_("set the scale of media"),
    'setshade':_("set shade of the line drawn by the turtle"),
    'settextcolor':_("set color of text drawn by the turtle"),
    'settextsize':_("set size of text drawn by turtle"),
    'setxy':_("move turtle to position xcor, ycor; (0, 0) is in the center of the screen."),
    'shade':_("holds current pen shade (can be used in place of a number block)"),
    'show':_("draw text or show media from the Journal"),
    'showblocks':_("restores hidden blocks"),
    'sqrt':_("calculate square root"),
    'stack1':_("invoke action 1 stack"),
    'stack2':_("invoke action 2 stack"),
    'stack':_("invoke named action stack"),
    'start':_("connects action to toolbar run buttons"),
    'stopstack':_("do not continue current action"),
    'storeinbox1':_("store numeric value in variable 1"),
    'storeinbox2':_("store numeric value in variable 2"),
    'storein':_("store numeric value in named variable"),
    'string':_("string value"),
    'template1x1':_("presentation template: select Journal object (with description)"),
    'template1x1a':_("presentation template: select Journal object (no description)"),
    'template1x2':_("presentation template: select two Journal objects"),
    'template2x1':_("presentation template: select two Journal objects"),
    'template2x2':_("presentation template: select four Journal objects"),
    'templatelist':_("presentation template: list of bullets"),
    'textcolor':_("holds current text color (can be used in place of a number block)"),
    'textsize':_("holds current text size (can be used in place of a number block)"),
    'toppos':_("ycor of top of screen"),
    'trash':_("a place to throw away blocks"),
    'turtle':_("palette of turtle commands"),
    'height':_("the canvas height"),
    'vspace':_("jog stack down"),
    'wait':_("wait specified number of seconds"),
    'xcor':_("holds current x-coordinate value of the turtle (can be used in place of a number block)"),
    'ycor':_("holds current y-coordinate value of the turtle (can be used in place of a number block)")}


#
# 'dead key' Unicode dictionaries
#

DEAD_KEYS = ['grave','acute','circumflex','tilde','diaeresis','abovering']
DEAD_DICTS = [{'A':192,'E':200,'I':204,'O':210,'U':217,'a':224,'e':232,'i':236,
               'o':242,'u':249},
              {'A':193,'E':201,'I':205,'O':211,'U':218,'a':225,'e':233,'i':237,
               'o':243,'u':250},
              {'A':194,'E':202,'I':206,'O':212,'U':219,'a':226,'e':234,
               'i':238,'o':244,'u':251},
              {'A':195,'O':211,'N':209,'U':360,'a':227,'o':245,'n':241,'u':361},
              {'A':196,'E':203,'I':207,'O':211,'U':218,'a':228,'e':235,
               'i':239,'o':245,'u':252},
              {'A':197,'a':229}]
NOISE_KEYS = ['Shift_L', 'Shift_R', 'Control_L', 'Caps_Lock', 'Pause',
              'Alt_L', 'Alt_R', 'KP_Enter', 'ISO_Level3_Shift', 'KP_Divide',
              'Escape', 'Return', 'KP_Page_Up', 'Up', 'Down', 'Menu',
              'Left', 'Right', 'KP_Home', 'KP_End', 'KP_Up', 'Super_L',
              'KP_Down', 'KP_Left', 'KP_Right', 'KP_Page_Down', 'Scroll_Lock',
              'Page_Down', 'Page_Up']
WHITE_SPACE = ['space','Tab']

CURSOR = '█'
