from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ChartCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

class ChartsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("Data Visualization")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        main_layout.addWidget(title)
        
        # Scroll area for charts
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        charts_container = QWidget()
        self.charts_layout = QVBoxLayout(charts_container)
        self.charts_layout.setSpacing(20)
        
        scroll.setWidget(charts_container)
        main_layout.addWidget(scroll)
        
        # Placeholder
        self.placeholder = QLabel("No data to visualize. Please upload a CSV file.")
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setStyleSheet("color: #999; font-size: 14px; padding: 100px;")
        self.charts_layout.addWidget(self.placeholder)
    
    def update_charts(self, data, summary):
        # Clear existing charts
        while self.charts_layout.count():
            child = self.charts_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if not data or not summary:
            self.placeholder = QLabel("No data to visualize")
            self.placeholder.setAlignment(Qt.AlignCenter)
            self.charts_layout.addWidget(self.placeholder)
            return
        
        # Chart 1: Equipment Type Distribution (Pie Chart)
        type_chart = self.create_type_distribution_chart(summary)
        self.charts_layout.addWidget(type_chart)
        
        # Chart 2: Average Parameters (Bar Chart)
        avg_chart = self.create_average_params_chart(summary)
        self.charts_layout.addWidget(avg_chart)
        
        # Chart 3: Parameter Ranges (Grouped Bar Chart)
        range_chart = self.create_parameter_ranges_chart(summary)
        self.charts_layout.addWidget(range_chart)
        
        self.charts_layout.addStretch()
    
    def create_type_distribution_chart(self, summary):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Title
        title = QLabel("Equipment Type Distribution")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        # Chart
        canvas = ChartCanvas(widget, width=8, height=5)
        
        type_dist = summary.get('type_distribution', {})
        labels = list(type_dist.keys())
        sizes = list(type_dist.values())
        
        colors = ['#ff6384', '#36a2eb', '#ffce56', '#4bc0c0', '#9966ff', '#ff9f40']
        
        canvas.axes.pie(sizes, labels=labels, autopct='%1.1f%%', 
                       colors=colors[:len(labels)], startangle=90)
        canvas.axes.set_title('Equipment Type Distribution', pad=20, fontsize=12, fontweight='bold')
        canvas.draw()
        
        layout.addWidget(canvas)
        return widget
    
    def create_average_params_chart(self, summary):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Title
        title = QLabel("Average Parameters")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        # Chart
        canvas = ChartCanvas(widget, width=8, height=5)
        
        params = ['Flowrate', 'Pressure', 'Temperature']
        values = [
            summary.get('avg_flowrate', 0),
            summary.get('avg_pressure', 0),
            summary.get('avg_temperature', 0)
        ]
        
        colors = ['#36a2eb', '#ff6384', '#ffce56']
        bars = canvas.axes.bar(params, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        canvas.axes.set_ylabel('Value', fontsize=10, fontweight='bold')
        canvas.axes.set_title('Average Parameter Values', pad=20, fontsize=12, fontweight='bold')
        canvas.axes.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            canvas.axes.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height:.2f}',
                           ha='center', va='bottom', fontweight='bold')
        
        canvas.draw()
        layout.addWidget(canvas)
        return widget
    
    def create_parameter_ranges_chart(self, summary):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Title
        title = QLabel("Parameter Ranges (Min vs Max)")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        # Chart
        canvas = ChartCanvas(widget, width=8, height=5)
        
        params = ['Flowrate', 'Pressure', 'Temperature']
        min_values = [
            summary.get('min_flowrate', 0),
            summary.get('min_pressure', 0),
            summary.get('min_temperature', 0)
        ]
        max_values = [
            summary.get('max_flowrate', 0),
            summary.get('max_pressure', 0),
            summary.get('max_temperature', 0)
        ]
        
        x = range(len(params))
        width = 0.35
        
        bars1 = canvas.axes.bar([i - width/2 for i in x], min_values, width, 
                               label='Minimum', color='#4bc0c0', alpha=0.8, edgecolor='black')
        bars2 = canvas.axes.bar([i + width/2 for i in x], max_values, width,
                               label='Maximum', color='#ff6384', alpha=0.8, edgecolor='black')
        
        canvas.axes.set_ylabel('Value', fontsize=10, fontweight='bold')
        canvas.axes.set_title('Parameter Ranges', pad=20, fontsize=12, fontweight='bold')
        canvas.axes.set_xticks(x)
        canvas.axes.set_xticklabels(params)
        canvas.axes.legend()
        canvas.axes.grid(axis='y', alpha=0.3, linestyle='--')
        
        canvas.draw()
        layout.addWidget(canvas)
        return widget