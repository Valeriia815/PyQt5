from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
mw = QWidget()
mw.setWindowTitle("Memory Card")
mw.resize(600, 500)

lb_question = QLabel("Яблуко")
btn_answer = QPushButton("Відповісти")

box_radio_group = QGroupBox("Варіанти відповідей")
radio_group = QButtonGroup()

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_question, alignment= Qt.AlignCenter)
layout_line2.addWidget(box_radio_group)
layout_line3.addWidget(btn_answer, alignment= Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)
mw.setLayout(layout_main)

mw.show()
app.exec_()