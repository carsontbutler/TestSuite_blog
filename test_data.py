import os
# base_url = 'http://localhost:8000'
base_url = 'https://blog.carsonbutler.dev'
base_dir = os.path.dirname(os.path.abspath(__file__))
data = {
    "profile": {'username': 'TestUser123',
                'username_changed': 'TestUser456',
                'email': 'testing@test.com',
                'email_changed': 'changed@test.net',
                "password": "TopSecret111",
                "email_invalid_1": "testing@testing",
                "email_invalid_2": "testing.com",
                "invalid_file_name": "invalid_file.txt",
                "new_profile_image_name": "bob.jpg",
                },
    "profile2": {"username": "ExistingUser",
                 "email": "ExistingUser@mywebsite.com"},
    "blog": {"title": "My Blog Post 1",
             "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tincidunt lorem nisl, non iaculis quam efficitur vitae. Aliquam erat volutpat. Aliquam ut vulputate metus, eget suscipit elit."}
}
