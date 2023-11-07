import sys

from PySide6.QtWidgets import QApplication

from pose_match_window import PoseMatchWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PoseMatchWindow()
    main_window.show()
    sys.exit(app.exec())
