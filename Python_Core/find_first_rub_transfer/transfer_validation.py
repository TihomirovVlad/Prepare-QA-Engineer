def find_first_rub_transfer(transfers_list):
    for transfer in transfers_list:
        if transfer["currency"] =="RUB":
            return transfer
    return None