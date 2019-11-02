import json
from emoji import UNICODE_EMOJI
import collections
import pandas as pd
import string
import math

from bokeh.palettes import PuBu
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, ranges, LabelSet,FactorRange
from bokeh.plotting import figure
from bokeh.layouts import gridplot

def is_emoji(s):
  return s in UNICODE_EMOJI

with open('result.json', 'r') as JSON:
	chat = json.load(JSON)

 # Now you can use it like dictionary
 # For example:

#print(chat['chats']['list'][1]['messages'][8].get('text'))


table = str.maketrans(dict.fromkeys(string.punctuation))  # OR {key: None for key in string.punctuation}
  

Murilo = 0
Valeria = 0
palavras = []
palavras_murilo = []
palavras_valeria = []


for x in range(len(chat['chats']['list'][1]['messages'])):
	try:
		texto = chat['chats']['list'][1]['messages'][x].get('text')
		new_texto = texto.translate(table) 
		a = new_texto.split()	
		if	chat['chats']['list'][1]['messages'][x].get('from') == "Murilo Martins":
			Murilo += 1
			for y in a:
				palavras_murilo.append(y.lower())
		if	chat['chats']['list'][1]['messages'][x].get('from') == "Meu Bem":
			Valeria += 1
			for y in a:
				palavras_valeria.append(y.lower())
	except:
		continue

print("Numero de Mensagens: Murilo:",Murilo," Valéria:", Valeria)

palavras = palavras_murilo + palavras_valeria
unicas_murilo = (set(palavras_murilo))
unicas_valeria = (set(palavras_valeria))

print(len(unicas_murilo))
print(len(unicas_valeria))

def check_emoji(arr):
	temp = []
	for pal in arr:
		for letter in pal:
			if is_emoji(letter):
				temp.append(letter)
	cont_emojis = dict.fromkeys(set(temp), 0)
	for keys in cont_emojis.keys():
		cont_emojis[keys] = temp.count(keys)
	sorted_emojis = sorted(cont_emojis.items(), key=lambda x: x[1], reverse=True)	
	return sorted_emojis

def check_palavras(arr):
	cont_palavras = dict.fromkeys(set(arr), 0)
	for keys in cont_palavras.keys():
		cont_palavras[keys] = arr.count(keys)
	sorted_palavras = sorted(cont_palavras.items(), key=lambda x: x[1], reverse=True)	
	return sorted_palavras

def proc_palavra(palavra_procurada,arr):
	x = arr.count(palavra_procurada)
	return x


murilo_emojis = check_emoji(palavras_murilo)
valeria_emojis = check_emoji(palavras_valeria)
murilo_dict = check_palavras(palavras_murilo)
valeria_dict = check_palavras(palavras_valeria)

print("Numero de palavras:",len(palavras))
print("Numero de Palavras Únicas:",len(unicas_murilo))
print("Quantidade de Emojis =):", 'murilo: ',len(murilo_emojis), 'valéria: ' ,len(valeria_emojis))

print('Valéria: ', valeria_dict[:100])
print('Valéria: ',valeria_emojis[:10])
print('Murilo: ',murilo_dict[:100])
print('Murilo: ',murilo_emojis[:10])


# building the graph


output_file("bars.html")

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

for i in range(20):
	x1.append(valeria_dict[i][0])
	y1.append(valeria_dict[i][1])
	x2.append(valeria_emojis[i][0])
	y2.append(valeria_emojis[i][1])
	x3.append(murilo_dict[i][0])
	y3.append(murilo_dict[i][1])
	x4.append(murilo_emojis[i][0])
	y4.append(murilo_emojis[i][1])




############################################



source1 = ColumnDataSource(dict(x=x1,y=y1))
x_label1 = "Palavras"
y_label1 = "qtd"
title1 = "Palavras mais utilizadas pela Valéria."
plot1 = figure(plot_width=800, plot_height=600, tools="save", x_axis_label = x_label1,
        y_axis_label = y_label1,
        title=title1,
        x_minor_ticks=2,
        x_range = source1.data["x"],
        y_range = ranges.Range1d(start=0,end=max(y1)+300))

labels1 = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=-10, y_offset=0, source=source1, render_mode='canvas')

plot1.vbar(source=source1,x='x',top='y',bottom=0,width=0.8,color=PuBu[7][2])
plot1.xaxis.major_label_orientation = math.pi/2
plot1.add_layout(labels1)

########################################

source2 = ColumnDataSource(dict(x=x2,y=y2))
x_label2 = "Palavras"
y_label2 = "qtd"
title2 = "Emojis mais utilizadas pela Valéria."
plot2 = figure(plot_width=600, plot_height=600, tools="save",
        x_axis_label = x_label2,
        y_axis_label = y_label2,
        title=title2,
        x_minor_ticks=2,
        x_range = source2.data["x"],
        y_range= ranges.Range1d(start=0,end=max(y2)+300))

labels2 = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-10, y_offset=0, source=source2, render_mode='canvas')

plot2.vbar(source=source2,x='x',top='y',bottom=0,width=0.8,color=PuBu[7][2])
plot2.add_layout(labels2)

###############################################

source3 = ColumnDataSource(dict(x=x3,y=y3))
x_label3 = "Palavras"
y_label3 = "qtd"
title3 = "Palavras mais utilizadas pelo Murilo."
plot3 = figure(plot_width=800, plot_height=600, tools="save",
        x_axis_label = x_label3,
        y_axis_label = y_label3,
        title=title3,
        x_minor_ticks=2,
        x_range = source3.data["x"],
        y_range= ranges.Range1d(start=0,end=max(y3)+300))

labels3 = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-10, y_offset=0, source=source3, render_mode='canvas')

plot3.vbar(source=source3,x='x',top='y',bottom=0,width=0.8,color=PuBu[7][2])
plot3.xaxis.major_label_orientation = math.pi/2
plot3.add_layout(labels3)

########################################

source4 = ColumnDataSource(dict(x=x4,y=y4))
x_label4 = "Palavras"
y_label4 = "qtd"
title4 = "Palavras mais utilizadas pelo Murilo."
plot4 = figure(plot_width=600, plot_height=600, tools="save",
        x_axis_label = x_label4,
        y_axis_label = y_label4,
        title=title4,
        x_minor_ticks=2,
        x_range = source4.data["x"],
        y_range= ranges.Range1d(start=0,end=max(y4)+300))

labels4 = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-10, y_offset=0, source=source4, render_mode='canvas')

plot4.vbar(source=source4,x='x',top='y',bottom=0,width=0.8,color=PuBu[7][2])
plot4.add_layout(labels4)

###############################################

x5 = ['amor', 'meu', 'bem', 'amo', 'love']
for palavra in x5:
	y5.append(proc_palavra(palavra,palavras_murilo))
	y6.append(proc_palavra(palavra,palavras_valeria))


nomes = ['Murilo', 'Valéria']

data = {'Palavras' : x5,
        'Murilo'   : y5,
        'Valéria'   : y6}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (palavra, nome) for palavra in x5 for nome in nomes ]
counts = sum(zip(data['Murilo'], data['Valéria']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

plot5 = figure(x_range=FactorRange(*x), plot_height=250, title="Quem disse mais?",
           toolbar_location=None, tools="")

plot5.vbar(x='x', top='counts', width=0.9, source=source)

plot5.y_range.start = 0
plot5.x_range.range_padding = 0.1
plot5.xaxis.major_label_orientation = 1
plot5.xgrid.grid_line_color = None



###############################################


grid = gridplot([[plot1, plot2], [plot3, plot4], [plot5]])
show(grid)
