from datetime import datetime
def main(old_total):
    start_date = input('enter the date: ')
    end_date = input('enter the date: ')
    items = input('Enter all items counts with comma seperation: ')
    rates = input('Enter items rates with comma seperation: ')
    old_total = old_total
    splited_items = split_fun(items)
    splited_rates = split_fun(rates)
    total_days = get_number_of_days(start_date, end_date)
    amount = sum(splited_items, splited_rates)
    total_interest, total = interest(total_days, amount, old_total)
    return  {
    "Total_days": total_days,
    "Amount_of_items": amount,
    "Total_interest": total_interest,
    "Total_amount": total
    }

def sum(items, rates):
    amount_list = [items*rates for items,rates in zip(items,rates)]
    amount = 0
    for item in amount_list:
        amount = amount + item
    return amount

def get_number_of_days(start_date, end_date):
    try:
        date_format = "%d/%m/%Y"
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)
        dalta = end_date - start_date
        return dalta.days
    except Exception as e:
        return str(e)
def split_fun(element):
    int_list = []
    ele=(element.split(","))
    for i in ele:
        int_list.append(int(i))
    return int_list
def interest(days, amount, old_amount):
    total = old_amount+amount
    interest_rate=2
    amount_interest = (total*days*interest_rate)/(30*100)
    return amount_interest, total

def repeat_main():
    old_total = 0
    for i in range(3):
        man=main(old_total)
        old_total = man['Total_amount']
        print(man)
repeat_main()
