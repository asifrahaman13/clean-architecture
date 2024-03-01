## About the repo

This is a demonstration of clean architecture which should be followed for industry standard code. 

```python
git clone https://github.com/asifrahaman13/clean-architecture.git
```

Next, create a virtual environment. 

```
virualenv .venv
```

Activate the  virtual environment. The following code works for UNIX based system( Linux and Max OS)

```
source .venv/bin/activate
```

Install all the dependencies.

```
pip install -r requirements.txt
```

Change the name of .env.example to .env and enter the env variables.

Next, run the backend server.

```
uvicorn src.main:app --reload
```