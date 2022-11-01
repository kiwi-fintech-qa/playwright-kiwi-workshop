## **Playwright workshop readme WIP**

1. Check whether you already have Git installed, by running the command: `git --version` in your terminal.  
   If you see one of the following errors or similar:  
   `'git' is not recognized as an internal or external command, operable program, or batch file.`  
   `command not found`  
   Download and install [Git](https://git-scm.com/downloads) for your OS.


2. Check whether you already have Python installed, by running the command: `python --version` in your terminal.  
   If you see the error:  
   `zsh: command not found: python`  
   Download and install [Python](https://www.python.org/downloads/) (preferably version 3.8 or later)
   and re-run the terminal command: `python --version`  
   If you still see the same error, 
   additionally run the terminal command: `echo "alias python=/usr/bin/python3" >> ~/.zshrc`  


3. Install the [Pycharm Community version](https://www.jetbrains.com/pycharm/download/)  
    Go to the [workshop GitHub repository](https://github.com/ukk0/playwright-kiwi-workshop) and click on the ‘Code’ 
    dropdown button, copy the https-address.  
    Open your Pycharm and in the popup-window click on 'Get from VCS'.  
    Set version control to: Git
    Set the copied address as the URL in Pycharm and hit 'Clone'.


4. Create virtual environment 
    From the top menu in Pycharm, click on:  
    `Pycharm -> Preferences -> Project: {project-name} -> Python Interpreter - Settings / 'gear-button' -> Add...`  
    Create a new virtual environment, using the Python version 3.8 or newer as the base interpreter.


5. Open the terminal within Pycharm (from the bottom menu) and:  
   Run the command `pip install -r requirements.txt` and wait for all the packages to be installed.  
   Run the command `playwright install` and wait for Playwright to install browsers.  
