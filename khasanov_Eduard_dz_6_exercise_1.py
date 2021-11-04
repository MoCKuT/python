
remote_addr, request_type, requested_resource = "", "", ""
i = 1
if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            clean_fp = line.replace('\n', ' ').replace('\r', ' ').replace('"', '')
            divide_fp = clean_fp.split(' ')
            remote_addr = divide_fp[0]
            request_type = divide_fp[5]
            requested_resource = divide_fp[6]
            fp_tuple = (str(i), (remote_addr, request_type, requested_resource))
            print(fp_tuple)
            i += 1
