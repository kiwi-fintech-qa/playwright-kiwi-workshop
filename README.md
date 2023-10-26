## **Playwright workshop readme**

1. Check whether you already have Git installed by running the command: `git --version` in your terminal/console.  
   If you see one of the following errors or similar:  
   `'git' is not recognized as an internal or external command, operable program, or batch file.`  
   `command not found`  
   Download and install the correct version of [Git](https://git-scm.com/downloads) for your OS.


2. Check whether you already have Python installed by running the command: `python --version` in your terminal/console.  
   If you see the error:  
   `zsh: command not found: python` or similar:  
   Download and install [Python](https://www.python.org/downloads/) (preferably version 3.8 or later)
   and re-run the terminal command: `python --version`  
   If you still see the same error, 
   additionally run the terminal command: `echo "alias python=/usr/bin/python3" >> ~/.zshrc`  


3. Install the [Pycharm Community version](https://www.jetbrains.com/pycharm/download/)  
    Go to the [workshop GitHub repository](https://github.com/kiwi-fintech-qa/playwright-kiwi-workshop) and click 
    on the **Code** dropdown button, copy the https-address.  
    Open Pycharm and in the popup-window click on **Get from VCS**.  
    Set version control to: **Git**  
    Set the copied https-address as the URL in Pycharm and hit **Clone**.


4. Create virtual environment  
   From the top menu in Pycharm, click on:  
   (macOS) `Pycharm -> Preferences -> Project: {project-name} -> Python Interpreter - Settings / 'gear-button' -> Add...`  
   (Windows) `File - Settings - Project: {project-name} -> Python Interpreter - Add interpreter - Add local interpreter`  
   Create a new virtual environment, using the Python version 3.8 or newer as the base interpreter.


5. Open the terminal within Pycharm (from the bottom menu) and:  
   Run the command `pip install -r requirements.txt` and wait for all the requirements to be installed.  
   On Windows, you may see here an error installing. If this happens, additionally download and install 
   [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).  
   During the installation, when prompted to choose the ‘workloads’, include the ‘Desktop development with C++’


6. Run the command `playwright install` and wait for Playwright to install the browsers.  

test
