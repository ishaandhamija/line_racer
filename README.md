# line_racer

## Requirements
 - Install Python 3.6+
 - Install Redis
 - Install MongoDB
 
 ## Setup Commands
  - Run mongodb on port `27017` in a separate terminal window
  - Run redis server with the command `redis-server` on a separate terminal window
  - `cd` into `line_racer` and run the command `pip install -r requirements.txt` (You can choose to do it in virtual environment)
  - Open a new terminal window and execute `cd line_racer/racer_process`. Then run the command `celery -A racer_process worker -l info`
  - Open a new terminal window and execute `cd line_racer/racer_process`. Then run the command `python manage.py runserver 8001`
  - Open a new terminal window and execute `cd line_racer/racer_process`. Then run the command `python manage.py runserver 8002`
  
## Start Flow
 - Open a new terminal window and execute `cd line_racer/master_process`. Then run the command `python manage.py runserver`
 
## Assumptions
 - Assumed m and c values for every lap message to be a random integer between 1 and 50.
 - Made sure on code level that m1 is never equal to m2 so that there is always am intersection point between the lines.
