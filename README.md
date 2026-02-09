
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
 # Chemical Equipment Parameter Visualizer
## Hybrid Web + Desktop Application

A comprehensive data visualization and analytics application for chemical equipment parameters, featuring both web and desktop interfaces connected to a common Django backend.

---

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Demo Video](#demo-video)

---

## ✨ Features

### Core Features
- ✅ CSV file upload (Web & Desktop)
- ✅ Data parsing and validation using Pandas
- ✅ Summary statistics calculation
- ✅ Interactive data visualization with charts
- ✅ Sortable data table display
- ✅ Dataset history (last 5 uploads)
- ✅ Shared REST API backend

### Extra Features
- ✅ PDF report generation with ReportLab
- ✅ Responsive web design
- ✅ Native desktop GUI with PyQt5
- ✅ Real-time data synchronization

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django 4.2 + DRF | REST API & Business Logic |
| **Database** | SQLite | Data Storage |
| **Data Processing** | Pandas | CSV parsing & analytics |
| **Web Frontend** | React.js 18 + Chart.js | Web visualization |
| **Desktop Frontend** | PyQt5 + Matplotlib | Desktop visualization |
| **PDF Generation** | ReportLab | Report creation |

---

## 📁 Project Structure

```
chemical-equipment-visualizer/
│
├── backend/                          # Django Backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── config/                       # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── api/                          # Django REST API app
│       ├── __init__.py
│       ├── models.py                 # Dataset model
│       ├── views.py                  # API views
│       ├── serializers.py            # DRF serializers
│       ├── urls.py                   # API routes
│       └── migrations/
│
├── frontend-web/                     # React Web Application
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   │
│   └── src/
│       ├── index.js
│       ├── App.jsx
│       ├── App.css
│       │
│       └── components/
│           ├── UploadForm.jsx
│           ├── UploadForm.css
│           ├── DataTable.jsx
│           ├── DataTable.css
│           ├── Charts.jsx
│           ├── Charts.css
│           ├── Summary.jsx
│           ├── Summary.css
│           ├── DatasetHistory.jsx
│           └── DatasetHistory.css
│
├── frontend-desktop/                 # PyQt5 Desktop Application
│   ├── main.py                       # Application entry point
│   ├── api_client.py                 # Backend API client
│   ├── requirements.txt
│   │
│   └── ui/                           # GUI components
│       ├── __init__.py
│       ├── main_window.py            # Main application window
│       ├── upload_widget.py          # Upload interface
│       ├── table_widget.py           # Data table view
│       ├── charts_widget.py          # Charts with Matplotlib
│       ├── summary_widget.py         # Summary statistics
│       └── history_widget.py         # Dataset history
│
├── sample_equipment_data.csv         # Sample data for testing
└── README.md                         # This file
```

---

## 📖 Usage Guide

### Uploading CSV Files

#### Web Application
1. Open http://localhost:3000
2. Drag and drop CSV file or click "Browse Files"
3. Click "Upload and Process"
4. View results in Summary, Charts, and Data Table sections

#### Desktop Application
1. Launch the desktop app
2. Go to "Upload" tab
3. Drag and drop CSV or click "Browse Files"
4. Click "Upload and Process"
5. Navigate through tabs to view data

### CSV File Format
Your CSV must include these columns:
- `Equipment Name` - Name of the equipment
- `Type` - Equipment type (Reactor, Pump, etc.)
- `Flowrate` - Flowrate value (numeric)
- `Pressure` - Pressure value (numeric)
- `Temperature` - Temperature value (numeric)

**Example:**
```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Reactor-A,Reactor,150.5,2.5,350
Pump-B,Pump,200.0,5.0,80
```

Use the provided `sample_equipment_data.csv` for testing.

### Viewing Data

**Summary Tab:**
- Total equipment count
- Average flowrate, pressure, temperature
- Equipment type distribution

**Charts Tab:**
- Equipment type pie chart
- Average parameters bar chart
- Parameter ranges comparison

**Data Table Tab:**
- Sortable columns
- Paginated view (10 rows per page in web)
- Complete dataset display

**History Tab:**
- View last 5 uploaded datasets
- Click any dataset to load it
- See upload date and equipment count

### Downloading PDF Reports

1. Upload or select a dataset
2. Go to Summary tab
3. Click "📄 Download PDF Report"
4. Choose save location
5. PDF includes summary statistics and data table

---

## 🔌 API Documentation

### Base URL
```
http://localhost:8000/api/
```

## 📊 Sample Data

The project includes `sample_equipment_data.csv` with 20 equipment entries for testing. This includes:
- 4 Reactors
- 4 Pumps
- 4 Heat Exchangers
- 4 Columns
- 4 Compressors

---


## 🎓 Learning Resources

- **Django**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **React**: https://react.dev/
- **PyQt5**: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- **Pandas**: https://pandas.pydata.org/docs/
- **Chart.js**: https://www.chartjs.org/
- **Matplotlib**: https://matplotlib.org/

---

## 📝 License

This project is created for educational purposes as part of an internship screening task.

---

## 👤 Author

**Aditi Mishra**
- GitHub: [@Aditi-1413](https://github.com/Aditi-1413)
- Email: aditi.040613@gmail.com

---

## 🙏 Acknowledgments

- Sample data generated for demonstration purposes
- Built with modern web and desktop technologies
- Designed for chemical engineering applications

---

**Happy Coding! 🚀**
=======
# Chemical Equipment Parameter Visualizer
## Hybrid Web + Desktop Application

A comprehensive data visualization and analytics application for chemical equipment parameters, featuring both web and desktop interfaces connected to a common Django backend.

 ✨ Features

Core Features
- ✅ CSV file upload (Web & Desktop)
- ✅ Data parsing and validation using Pandas
- ✅ Summary statistics calculation
- ✅ Interactive data visualization with charts
- ✅ Sortable data table display
- ✅ Dataset history (last 5 uploads)
- ✅ Shared REST API backend

Extra Features
- ✅ PDF report generation with ReportLab
- ✅ Responsive web design
- ✅ Native desktop GUI with PyQt5
- ✅ Real-time data synchronization

---

 🛠 Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django 4.2 + DRF | REST API & Business Logic |
| **Database** | SQLite | Data Storage |
| **Data Processing** | Pandas | CSV parsing & analytics |
| **Web Frontend** | React.js 18 + Chart.js | Web visualization |
| **Desktop Frontend** | PyQt5 + Matplotlib | Desktop visualization |
| **PDF Generation** | ReportLab | Report creation |

---

 📁 Project Structure

```
chemical-equipment-visualizer/
│
├── backend/                          # Django Backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── config/                       # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── api/                          # Django REST API app
│       ├── __init__.py
│       ├── models.py                 # Dataset model
│       ├── views.py                  # API views
│       ├── serializers.py            # DRF serializers
│       ├── urls.py                   # API routes
│       └── migrations/
│
├── frontend-web/                     # React Web Application
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   │
│   └── src/
│       ├── index.js
│       ├── App.jsx
│       ├── App.css
│       │
│       └── components/
│           ├── UploadForm.jsx
│           ├── UploadForm.css
│           ├── DataTable.jsx
│           ├── DataTable.css
│           ├── Charts.jsx
│           ├── Charts.css
│           ├── Summary.jsx
│           ├── Summary.css
│           ├── DatasetHistory.jsx
│           └── DatasetHistory.css
│
├── frontend-desktop/                 # PyQt5 Desktop Application
│   ├── main.py                       # Application entry point
│   ├── api_client.py                 # Backend API client
│   ├── requirements.txt
│   │
│   └── ui/                           # GUI components
│       ├── __init__.py
│       ├── main_window.py            # Main application window
│       ├── upload_widget.py          # Upload interface
│       ├── table_widget.py           # Data table view
│       ├── charts_widget.py          # Charts with Matplotlib
│       ├── summary_widget.py         # Summary statistics
│       └── history_widget.py         # Dataset history
│
├── sample_equipment_data.csv         # Sample data for testing
└── README.md                         # This file
```

---
 📖 Usage Guide

Uploading CSV Files

 Web Application
1. Open http://localhost:3000
2. Drag and drop CSV file or click "Browse Files"
3. Click "Upload and Process"
4. View results in Summary, Charts, and Data Table sections

 Desktop Application
1. Launch the desktop app
2. Go to "Upload" tab
3. Drag and drop CSV or click "Browse Files"
4. Click "Upload and Process"
5. Navigate through tabs to view data

CSV File Format
Your CSV must include these columns:
- `Equipment Name` - Name of the equipment
- `Type` - Equipment type (Reactor, Pump, etc.)
- `Flowrate` - Flowrate value (numeric)
- `Pressure` - Pressure value (numeric)
- `Temperature` - Temperature value (numeric)

**Example:**
```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Reactor-A,Reactor,150.5,2.5,350
Pump-B,Pump,200.0,5.0,80
```

Use the provided `sample_equipment_data.csv` for testing.

 Viewing Data

**Summary Tab:**
- Total equipment count
- Average flowrate, pressure, temperature
- Equipment type distribution

**Charts Tab:**
- Equipment type pie chart
- Average parameters bar chart
- Parameter ranges comparison

**Data Table Tab:**
- Sortable columns
- Paginated view (10 rows per page in web)
- Complete dataset display

**History Tab:**
- View last 5 uploaded datasets
- Click any dataset to load it
- See upload date and equipment count

Downloading PDF Reports

1. Upload or select a dataset
2. Go to Summary tab
3. Click "📄 Download PDF Report"
4. Choose save location
5. PDF includes summary statistics and data table

---

🔌 API Documentation

Base URL
```
http://localhost:8000/api/
```

 📊 Sample Data

The project includes `sample_equipment_data.csv` with 20 equipment entries for testing. This includes:
- 4 Reactors
- 4 Pumps
- 4 Heat Exchangers
- 4 Columns
- 4 Compressors

---


 🎓 Learning Resources

- **Django**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **React**: https://react.dev/
- **PyQt5**: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- **Pandas**: https://pandas.pydata.org/docs/
- **Chart.js**: https://www.chartjs.org/
- **Matplotlib**: https://matplotlib.org/

---

📝 License

This project is created for educational purposes as part of an internship screening task.

---

👤 Author

**Aditi Mishra**
- GitHub: [@Aditi-1413](https://github.com/Aditi-1413)
- Email: aditi.040613@gmail.com

---
 🙏 Acknowledgments

- Sample data generated for demonstration purposes
- Built with modern web and desktop technologies
- Designed for chemical engineering applications

---

**Happy Coding! 🚀**
>>>>>>> c0b7d7ccec0ffef531be1510b0786d73c5ed519b
>>>>>>> 64d14422d577c7324c609929f1402833b0b8b01b
