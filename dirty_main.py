import sys
sys.path.append("./db/")
sys.path.append("./application/")
import datetime
from people import *
from salary import *

if __name__ == '__main__':
    print(f'Current date is {datetime.date.today()}')
    calculate_salary()
    get_employees()
