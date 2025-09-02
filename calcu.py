import sys
import cupy as cp
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QGridLayout, QLabel, QFrame, QSizePolicy
)
from PyQt5.QtGui import QFont, QSurfaceFormat
from PyQt5.QtCore import Qt


# ---------------- RTX CALCULATOR APP ----------------
class RTXCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RTXCALC 🚀")
        self.setMinimumSize(400, 550)
        self.setStyleSheet("background-color: #0c0c0c; color: white;")

        layout = QVBoxLayout()
        layout.setSpacing(12)

        # GPU Label (top header)
        gpu_name = cp.cuda.runtime.getDeviceProperties(0)["name"].decode("utf-8")
        self.gpu_label = QLabel(f"⚡ RTXCALC running on {gpu_name}")
        self.gpu_label.setAlignment(Qt.AlignCenter)
        self.gpu_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.gpu_label.setStyleSheet("color: #00ff88; padding: 10px;")
        layout.addWidget(self.gpu_label)

        # Display (calculator screen)
        self.display = QLineEdit()
        self.display.setFont(QFont("Consolas", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("""
            QLineEdit {
                background: rgba(30,30,30,0.9);
                border: 2px solid #00ff88;
                border-radius: 12px;
                padding: 15px;
                color: #00ff88;
            }
        """)
        self.display.setFocusPolicy(Qt.StrongFocus)
        layout.addWidget(self.display)

        # Button grid
        grid = QGridLayout()
        grid.setSpacing(10)

        buttons = [
            ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
            ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
            ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
            ('0',3,0), ('.',3,1), ('=',3,2), ('+',3,3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Segoe UI", 14, QFont.Bold))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setMinimumHeight(60)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #1e1e1e;
                    border: 2px solid #00ff88;
                    border-radius: 12px;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #00ff88;
                    color: black;
                }
                QPushButton:pressed {
                    background-color: #00cc66;
                    color: black;
                }
            """)
            button.clicked.connect(lambda _, t=text: self.on_click(t))
            grid.addWidget(button, row, col)

        frame = QFrame()
        frame.setLayout(grid)
        layout.addWidget(frame)

        self.setLayout(layout)

    # ---------------- EVENTS ----------------
    def on_click(self, char):
        if char == '=':
            self.evaluate()
        else:
            self.display.setText(self.display.text() + char)

    def keyPressEvent(self, event):
        key = event.key()
        text = event.text()

        if key in (Qt.Key_Return, Qt.Key_Enter):
            self.evaluate()
        elif key == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        elif key == Qt.Key_Escape:
            self.display.clear()
        elif text in "0123456789+-*/().":
            self.display.setText(self.display.text() + text)

    # ---------------- GPU CALC ----------------
    def evaluate(self):
        try:
            expr = self.display.text()
            safe_dict = {"cp": cp}
            result = eval(expr, {"__builtins__": None}, safe_dict)
            if isinstance(result, cp.ndarray):
                result = float(result.get())
            else:
                result = float(result)
            self.display.setText(f"{result}  [GPU]")
        except Exception as e:
            self.display.setText("Error")
            print("Calculation error:", e)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    # Enable hardware-accelerated rendering with OpenGL
    fmt = QSurfaceFormat()
    fmt.setRenderableType(QSurfaceFormat.OpenGL)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setVersion(3, 3)
    QSurfaceFormat.setDefaultFormat(fmt)

    app = QApplication(sys.argv)
    window = RTXCalc()
    window.show()
    sys.exit(app.exec_())
