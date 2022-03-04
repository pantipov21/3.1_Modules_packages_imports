import sys
sys.path.append("./db/")
sys.path.append("./application/")
import datetime
from people import get_employees
from salary import calculate_salary

if __name__ == '__main__':
    print(f'Current date is {datetime.date.today()}')
    calculate_salary()
    get_employees()
