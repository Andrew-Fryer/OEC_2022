# Administration
## Creators
Kyle Singer
| Andrew Fryer
| Jamie Won
| Tristan Lawson

## Emails
kylesinger@rogers.com
| andrewtfryer@gmail.com
| Tristan.lawson99@gmail.com
| jamie.won.2000@gmail.com

## Group
Team Sonic

## Project Title
Waste Map-Tracker

# Project Structure
- data
(contains input data for the algorithm)
- src
  - app.py
  - main.py
  - parse.py
  - alg.py
  - plot.py
- output
  - plot.svg
- client (contains the web application) 
  - .env (some environment variables used in the web application)
  - src (where the majority of the code is run)
    - Pages (contains the two pages made for the web application)
    - Components (contains the components used throughout the web application)

# Running code
To run the backend server, please issue the following commands in bash/sh/cmd.
```
python -V # must be version 3.*.*
git clone git@github.com:Andrew-Fryer/OEC_2022.git
cd OEC_2022
pip install -r requirements.txt
cd src
export FLASK_APP=app
python -m flask run # runs backend
```
Please view output files in the `./output` directory.

In a separate terminal, navigate to the OEC_2022 directory, then run the following commands.
```
cd client
npm install
npm run start
```
This will spin up the front end at http://localhost:3000/#/

## Working with the Front End
Please enter the algorithm parameters and select the desired csv file. Once you click submit, wait for the algorithm to run.

When the algorithm is complete, an interactive 3D map will appear. You can drag to move the globe, scroll to zoom and hover over a point for more information. The results of the algorithm can be found below the map.

To scroll to the next/previous sections, move your cursor to the blue bar across the top (otherwise, the zoom action will be triggered).

