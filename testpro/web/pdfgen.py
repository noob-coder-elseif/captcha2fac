from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc = SimpleDocTemplate("simple_table_grid.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []

data= [
    ['Security Questions', 'Compliance / Non-Compliance', 'Remarks'],
    ['10', '11', '12'],
    ['20', '21', '22'],
    ['30', '31', '32']
    ]
# t=Table(data,5*[1.4*inch], 4*[0.4*inch])
t=Table(data)
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
('TEXTCOLOR',(1,1),(-2,-2),colors.red),
('VALIGN',(0,0),(0,-1),'TOP'),
('TEXTCOLOR',(0,0),(0,-1),colors.blue),
('ALIGN',(0,-1),(-1,-1),'CENTER'),
('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
]))

elements.append(t)
# write the document to disk
doc.build(elements)