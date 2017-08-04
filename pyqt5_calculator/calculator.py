if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    from gui.button import Button
    
    app = QApplication(sys.argv)
    
    main = Button()
    main.show()
    
    sys.exit(app.exec_())
