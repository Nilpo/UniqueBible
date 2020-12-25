from PySide2.QtGui import QPalette, QColor

class Themes():

    @staticmethod
    def getPalette(name):
        if name == "dark":
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(50, 50, 50))
            palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
            palette.setColor(QPalette.Background, QColor(50, 50, 50))
            palette.setColor(QPalette.Base, QColor(50, 50, 50))
            palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
            palette.setColor(QPalette.ToolTipBase, QColor(50, 50, 50))
            palette.setColor(QPalette.ToolTipText, QColor(200,200,200))
            palette.setColor(QPalette.Text, QColor(200, 200, 200))
            palette.setColor(QPalette.Button, QColor(50, 50, 50))
            palette.setColor(QPalette.ButtonText, QColor(200, 200, 200))
            palette.setColor(QPalette.BrightText, QColor(255,255,255))
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, QColor(50, 50, 50))
            return palette
        else:
            palette = QPalette()
            # palette.setColor(QPalette.Background, QColor("white"))
            return palette