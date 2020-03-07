## url
markov-chain-j-g.surge.sh

Flask api hosted by heroku, and React frontend hosted with surge

## Markov Chain Algorithm Site

#### To start the python application please setup a python virtual environment like this. 

1. Type this into your terminal
```
virtualenv -p /path/to/python venv
```

2. Then type this
```
source venv/bin/activate
```
3. then this
```
pip3 install -r requirements.txt
```
4. Then the final step to getting it running
```
export FLASK_ENV=development; flask run
```

## Now how to run the React development locally...

1. Make sure you are in the markov-chain-jg folder

2. they type this into your terminal
```
npm install
```

3. then type this into terminal
```
npm start
```

### tips for future self

1. to find flask app running in the background. Second item is the id
```
ps -fA | grep python
```

2. then kill it
```
kill id
```