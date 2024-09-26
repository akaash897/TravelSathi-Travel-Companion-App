
# SDE Project - TravelSathi 

This is a web application built using **Flask**, a lightweight WSGI web framework in Python.

## Technologies Used

- **Flask**: The primary web framework used to build this application.
- **Python**: The programming language used for development.
- **HTML/CSS**: For the frontend structure and styling.

## Setup and Installation

### Prerequisites

- Python 3.8+ must be installed on your system.
- You may use a virtual environment to manage dependencies.

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (for development):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development  # Enables debug mode
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Access the app at: `http://127.0.0.1:5000/`

## Project Structure

```
.
├── app.py               # Main application file
├── requirements.txt     # List of dependencies
├── static/              # Static files (CSS, JavaScript, images)
├── templates/           # HTML templates rendered by Flask
└── README.md            # Project documentation
```

## Features

- Feature 1: 
- Feature 2: 

## Contribution

Feel free to open issues and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
