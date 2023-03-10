from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees


def result():
    get_employees()
    calculate_salary()

def main():
    current_date = date.today()
    result()
    print(current_date)

if __name__ == '__main__':
    main()
