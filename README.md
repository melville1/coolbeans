# CoolBeans - An example ecommerce website built on Django. 

## A JTC Project built by The Undefined Variables: 
-Mel Morel
-Christopher Schreiber
-Jon Wrenn

### To start building the project

#### 1. Create a virtual environment

At the root folder of the repo, execute:

```bash
python3 -m venv venv
```

(Your python executable may be called something different depending on your installation.)

#### 2. Run virtual environment

- If Using Windows Powershell

```powershell
venv\Scripts\activate.ps1
```

- If Using Windows Command Prompt

```CMD
venv\Scripts\activate.bat
```
- If Using Mac or Linux Terminal

```bash
. venv/bin/activate
```
#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Test the Server & Migrate to your sqlite Database

```bash
cd coolbeans
python manage.py runserver
```
By default the server will run on :
http://172.0.0.1:8000 if neither the ip or the port are set.
Use Control-C to exit the server
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Import Mock Data from a Fixture

```bash
python manage.py loaddata coolbeansapp.json
```

#### 6. Run the Server Again and Test Drive the App!

```bash
python manage.py runserver ipv4:port
```
By default the server will run on :
http://172.0.0.1:8000 if neither the ip or the port are set. 
