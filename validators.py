def validate_credit_card(card_number):
    card_number_list = []
    for num in card_number.replace(' ',''):
        card_number_list.append(int(num))
    check_digit = card_number_list.pop()
    card_number_list.reverse()
    card_number_list[::2] = [num*2 for num in card_number_list[::2]]
    sum_list = []
    for num in card_number_list:
        if num>9:
            sum_list.append(num-9)
        else:
            sum_list.append(num)
    return str(sum(sum_list))[1]==str(check_digit)
