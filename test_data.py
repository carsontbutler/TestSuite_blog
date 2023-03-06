import os
base_url = 'http://localhost:8000'
base_dir = os.path.dirname(os.path.abspath(__file__))
data = {
    "profile": {'username': 'TestUser123',
                'username_changed': 'TestUser456',
                'username_invalid_1': 'MyUsername#',
                'username_invalid_2': 'HereIsAUsernameThatIsLongerThan150CharactersImNotSureWhyAnyoneWouldNeedAUsernameThisLongHereIsAUsernameThatIsLongerThan150CharactersImNotSureWhyAnyoneWouldNeedAUsernameThisLong',
                'email': 'testing@test.com',
                'email_changed': 'changed@test.net',
                "password": "TopSecret111",
                "email_invalid_1": "testing@testing",
                "email_invalid_2": "testing.com",
                "new_profile_image_name": "bob.jpg"
                },
    "blog": {"title": "My Blog Post 1",
             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tincidunt lorem nisl, non iaculis quam efficitur vitae. Aliquam erat volutpat. Aliquam ut vulputate metus, eget suscipit elit."}
}
