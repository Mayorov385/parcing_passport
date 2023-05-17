text = "/n /nabracadabra 1 item"
sub_string = '/n'
result_str = ''

array_text = text.split(' ')

for item in array_text:
    if isinstance(item, str):
        if sub_string in item:
            result_str += f"{item.replace(sub_string, ' ')} "
        else: result_str += f"{item} "
        
        
print(result_str)