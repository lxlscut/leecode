def get_num_date(date):
    split_date = date.split("-",-1)
    for i in range(len(split_date)):
        split_date[i] = int(split_date[i])
    start_date = [31,28,31,30,31,30,31,31,30,31,30,31]
    start_date_run = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (split_date[0]%4 == 0 and split_date[0]%100!=0) or (split_date[0]%400==0):
        num=0
        for i in range(split_date[1]-1):
            num = num+start_date_run[i]
        num = num+split_date[2]
        return num

    else:
        num=0
        for i in range(split_date[1]-1):
            num = num+start_date[i]
        num = num+split_date[2]
        return num

if __name__ == '__main__':
    date = "1900-03-25"
    print(get_num_date(date))