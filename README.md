# QuantPair

## Setting up the workspace 

Make sure you have python installed on your system

* Setting up the virtual environment
  * Create a directory of your choice, for our purposes, we will call it test
  * Navigate to /test and create a virtual environment there by using command
    ```
    py -m venv QuantPair-Server
    ```

  * Now you should see a folder with QuantPair-Server as it description
  * Navigate into `test/QuantPair-Server`

## Cloning and installing libraries
 
* Cloning the repository 
  * Now clone the repository here by using command
    ```
    git@github.com:WebOps-and-Blockchain-Club/QuantPair-Server.git
    ```
  * You should see `QuantPair-Server` folder cloned in `test/QuantPair-Server`
  * Rename the folder to `QuantPair_Server`
 
* Installing required modules and libraries
  * Navigate back to `test/QuantPair-Server`
  * In your terminal, run the virtual environment using the following command
    ```
    Scripts\activate.bat
    ```
  * Now you are in the virtual environment
  * Navigate into `test/QuantPair-Server/QuantPair_Server`
  * Install most of the requirements using the command
    ```
    pip install -r requirements.txt
    ```

  * Due to some issues with synchronization, we will have to manually install some libraries
  * Execute the following commands one after the other
    ```
    pip install djangorestframework
    ```
    ```
    pip install psycopg2
    ```
    ```
    python -m pip install -U matplotlib
    ```
    ```
    pip install -U scikit-learn
    ```
    ```
    pip install tensorflow
    ```
## Django Migrations and testing

* Migrations
  * Navigate into `test/QuantPair-Server/QuantPair_Server`
  * Now into your terminal run the command to migrate changes
    ```
    py manage.py migrate
    ```
  * Create admin and set credentials
    ```
    py manage.py createsuperuser
    ```
  * Make migrations
    ```
    py manage.py makemigrations
    ```
  * Cache migrations
     ```
    py manage.py migrate
    ```
* Run Server
  * Navigate into `test/QuantPair-Server/QuantPair_Server`
  * Type the following command to run the server
    ```
    py manage.py runserver
    ```
  * You should see something like this
    ```
    Watching for file changes with StatReloader
    Performing system checks...
    
    2025-01-25 00:05:49.282524: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
    2025-01-25 00:05:52.336835: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
    System check identified no issues (0 silenced).
    January 25, 2025 - 00:05:57
    Django version 5.1.2, using settings 'QuantPair_Server.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
  * Now you can follow the local-server address and test your api's
  
     

  
  