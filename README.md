# Stay-Awake
A small python script to move your mouse, press the shift key, and keep your PC awake when you're away
Uses command line arguments to set the number of minutes between movements and requires Python3 or higher.
Default timer is 3 minutes, but can be 1 or more. 

# Dependencies
This software uses PyAutoGui https://github.com/asweigart/pyautogui as the driver behind the movement. 

# Mac installation

OSX on default comes with python 
Test :
  python3 --version (If not install with HomeBrew brew install python3)

Install PIP package manager for python
  sudo easy_install pip

For Mac OS Sierra, cannot install pip via easy_instal
curl https://bootstrap.pypa.io/get-pip.py | sudo python3

Install Package dependencies
  pip3 install pyautogui


# Run

python3 src/awake.py