#Write a python expression that gets the email address of Ramit.
#Write a python expression that gets the first of Ramit's interests.
#Write a python expression that gets the email address of Jasmine.
#Write a python expression that gets the second of Jan's two interests.

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print ramit.get('email')
#How do I use the get function for the following?:
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][0]['interests'][1]
