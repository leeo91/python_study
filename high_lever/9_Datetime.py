import datetime


def input_date():
    inputdate = input('输入日期（如20220120）：')
    dateStr = inputdate[0:4] + '-' + inputdate[4:6] + '-' + inputdate[6:]
    dt = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    return dt


if __name__ == '__main__':
    date = input_date()
    print(date, type(date))
    in_num = eval(input('输入间隔天数：'))
    date = date + datetime.timedelta(days=in_num)
    print(date)
