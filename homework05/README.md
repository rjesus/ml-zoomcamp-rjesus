# Setup
```bash
pipenv install
pipenv shell
bash download-model.sh
```

# Running predictions on the terminal
Edit the input features on `predict.py` then run the file with python
```bash
python predict.py
```

# Running predictions as a development web server locally 
```bash
flask --app server_predict run --reload --debug --debugger
```

# Running the client
The script `client_predict.py` is a python client compatible with the `server_predict.py` use it to test the server.
```bash
python client_predict.py
```

# Setup Docker
```bash
docker build -t credit-prediction .
```

# Running Docker
```bash
docker run -it -p 9696:9696 credit-prediction
```

On `client_predict.py`, set the `url="http://127.0.0.1:9696/predict"` to use this server 