# Outline of running and benchmarking the app in Oracle Virtualbox (Virtualization)

## Installation of Virtualbox and creation of virtual machine

1. Install Oracle VirtualBox
2. Download Fedora ISO (follow the steps mentioned [here](https://itsfoss.com/install-fedora-in-virtualbox/))
3. Instantiate Fedora OS with parameters CPU = 1 and Memory = 2048 MB
4. Run the Fedora OS inside Virtualbox 

## Cloning the repository

1. Fedora comes pre-installed with git, Clone the repository:
   ```bash
   git clone -depth 1 https://github.com/akaash897/TravelSathi-Travel-Companion-App.git
   ```

## Running the app 

1. Go inside the TravelSathi-Travel-Companion-App folder, Install python requirements :
   ```bash
   cd TravelSathi-Travel-Companion-App
   python -m pip install -r requirements.txt
   ```
2. Run to start the server, this will listen on port https://localhost:5000 :
   ```bash
   python app.py
   ```

## Benchmarking using Apache bench
1. In new terminal, run benchmarking with 100 connection with 1000 requests:
   ```bash
   ab -c 100 -n 1000 http://localhost:5000/
   ```




