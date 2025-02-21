import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    # Cria a aplicação Qt
    app = QApplication(sys.argv)
    
    # Inicializa e mostra a janela principal
    window = MainWindow()
    window.show()
    
    # Inicia o loop da aplicação Qt
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()