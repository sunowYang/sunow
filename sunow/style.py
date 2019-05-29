# -*- coding: utf-8 -*-#


_STYLE = """
        QLabel{color: #2A7A7E;}
        QLabel:hover{color: #4BAEB3;}

        QProgressBar{background-color:#FFFFFF;text-align:center;}
        QProgressBar::chunk{Background-color:#4BAEB3;}

        QCheckBox { spacing: 10px; height: 35px;}
        QCheckBox::indicator{ width: 20px; height: 20px;}
        QCheckBox::indicator:unchecked{ image:url(res/check_unsel.png);}
        QCheckBox::indicator:checked{ image:url(res/check_sel.png);}
        
        
        QRadioButton { spacing: 10px;}
        QRadioButton::indicator {width: 20px;height: 20px;}
        QRadioButton::indicator:unchecked {image:url(res/radio_unchecked.png);}
        QRadioButton::indicator:checked {image:url(res/radio_checked.png);}

        QPushButton {height: 30px;
                     background-color:#FFFFFF;
                     border:1px solid #A5A5A5;
                     padding-left:25px;
                     padding-right:25px;
        }   
        QPushButton:hover {color: #4BAEB3;}

        QLineEdit {height: 30px;
                   font: 15px;
                   border:1px solid #D7D7D7;
                   selection-color: white;
                   margin: 2px;}
        
        QComboBox {height:30px;
                   width:120px;
                   color:black;
                   selection-color: black;
                   selection-background-color: #FFFFFF;
                   border:1px solid #D7D7D7;
                   background-color:#FFFFFF;
        }
        QComboBox::drop-down {
                    image:url(res/task_expand.png);
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 20px;
        }
        QComboBox QAbstractItemView{
                   color:black;
                   background-color:#FFFFFF;
                   selection-color: black;
                   selection-background-color: green;
                   border: 1px solid #666666;
        }
        QComboBox QAbstractItemView::item{height: 30px;}
                        
        QSpinBox {height: 30px;width: 100px;border: 1px solid #D7D7D7;}             
        QSpinBox::down-button{image:url(res/icon_arrow_down.png);}
        QSpinBox::up-button{image:url(res/icon_arrow_up.png);}
        
        QSplitter::handle {background-color: #F1F1F1; border: 1px solid #AFAFAF;}

        QScrollBar{
                    height:11px;
                    background:#CDCDCD;
                    margin:0px,0px,0px,0px;
                    padding-top:0px;
                    padding-bottom:0px;
        }
        QScrollBar::handle{height:11px;background:#B3B3B3;}
        QScrollBar::handle:hover{background:#999999;}
        
        QTreeView{border: 0px;color: red;}
        
        QTreeView::item{
                        height: 36px;
                        border: 1px solid #DDDDDD;
                        border-style: solid none solid none;
                        color: black;
                        padding: 0px;
        }
        QTreeView::item:hover{
                        background: #EDF7F8;
                        border: 1px solid #BCE0E2;
                        border-style: solid none solid none;
        }
        QTreeView::item:selected{
                        background: #E2F2F3;
                        border: 1px solid #4BAEB3;
                        border-style: solid none solid none;
                        
        }
        QTreeView::branch:selected{outline: none;}
        
        QHeaderView{font-size: 14px;Font: Roman times;color: black;}
        QHeaderView::section:hover{background-color:#FFFFFF;border: none;padding: 4px;}
        
"""
