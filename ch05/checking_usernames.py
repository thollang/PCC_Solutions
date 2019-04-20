current_users=['Thollang','Jack','Ann','Bob','David']
new_users=['Emma','Frank','Inn','Bob','Ann']

for new_user in new_users:
    if new_user in current_users:
        print("This username -"+new_user+" existed.Please input another name")
    else:
        print("This username -"+new_user+" hasn't been used")
