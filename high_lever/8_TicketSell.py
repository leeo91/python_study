import prettytable as pt


def show_ticket(row_num):
    tb = pt.PrettyTable()  # create table
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1, row_num):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()  # create table
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(1, row_num + 1):
        if int(row) == i:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)

    print(tb)


if __name__ == '__main__':
    show_ticket(6)
    choose_num = input('请输入坐席：')
    row, column = choose_num.split(',')
    order_ticket(6, row, column)
