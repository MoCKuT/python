
remote_addr, request_type, requested_resource = "", "", ""
lst_ip = []
number_appeals = []

if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            clean_fp = line.replace('\n', ' ').replace('\r', ' ').replace('"', '')
            divide_fp = clean_fp.split(' ')
            remote_addr = divide_fp[0]
            request_type = divide_fp[5]
            requested_resource = divide_fp[6]
            fp_tuple = (remote_addr, request_type, requested_resource)

            # Добавляю в первый список, ip адреса не повторяясь, а в другой список, сколько раз встретил этот ip
            if remote_addr not in lst_ip:
                lst_ip.append(remote_addr)
                number_appeals.append(1)
            else:
                i = lst_ip.index(remote_addr)
                num = number_appeals[i]
                number_appeals[i] = num + 1

    repeat = 1
    for n in number_appeals:
        if n > repeat:
            repeat = n

    print(lst_ip[number_appeals.index(repeat)], "количество отправленный запросов:", repeat)
