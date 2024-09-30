
# SDE Project - TravelSathi 

## Abstract
The project aims to create a secure online platform that facilitates shared transportation for college students, starting with autorickshaw rides between key locations like IIT Jodhpur and Jodhpur Junction. Users can post when they are looking for companions for a ride, and others can search for available rides to join. To ensure privacy and safety, the platform offers gender-specific pairing options—female users can choose to travel with female partners only, and the same applies to male users, with an additional co-ed option available. No personal details are shared among users. The platform will also include a database of trusted autorickshaw drivers operating within the IITJ campus. Future plans involve expanding the service to other nearby institutions like NIFT and incorporating a broader range of transportation options. The final aim is to apply containerization using Docker and virtualisation based on a Fedora VM using
VirtualBox and compare the performance metrics of our website on both using Apache Benchmarks.

## Evaluation rubrics
- [ ] Pick two or more architectural pattern, implement and compare them critically.

- [x] Compare the effect of containerisation and virtualisation by generating experimental results from the system implemented by you. [more details here](benchmarks.md)

- [ ] Implement any cloud computing related aspect and show the performance improvement over non-cloud setup by generating experimental results from the system implemented by you. 

Submission Artefacts: 
1. Design document 
2. Source code repository
3. [Readme file](README.md) 
4. Code documentation 
5. Presentation slides
6. Recorded demo
7. Recorded presentation (optional)

## Technologies Used

- **Flask**: The primary web framework used to build this application.
- **Python**: The programming language used for development.
- **HTML/CSS**: For the frontend structure and styling.

## Setup and Installation

This is a web application built using **Flask**, a lightweight WSGI web framework in Python.

### Prerequisites

- Python 3.8+ must be installed on your system.
- You may use a virtual environment to manage dependencies.

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/akaash897/TravelSathi-Travel-Companion-App.git
   cd TravelSathi-Travel-Companion-App
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

## Virtualization 

Virtual machine based on Fedora OS was instatiated in Oracle [Virtualbox, details here](virtualbox.md)

## Containerization 

This was implmented using [Docker containers, more details here](docker.md)

## Contribution

Feel free to open issues and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
