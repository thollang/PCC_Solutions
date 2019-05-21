from privileges import Admin

eric = Admin('eric' , 'matthes', 'e_matthes', 'e_matthes@example', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accoutnts',
    ]
eric.privileges.privileges = eric_privileges

print("\nThe admin {} has these privileges: ".format(eric.username))
eric.privileges.show_privileges()
