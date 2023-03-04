base_url = 'http://localhost:8000'
data = {
    "register": {'username': 'TestUser123',
                 'email': 'testing@test.com',
                 "password": "TopSecret111",
                 "email_invalid_1": "testing@testing",
                 "email_invalid_2": "testing.com"},
    "login": {"username": "TestUser001",
              "password": "TopSecret000"},

    "blog": {"title": "My Blog Post 1",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tincidunt lorem nisl, non iaculis quam efficitur vitae. Aliquam erat volutpat. Aliquam ut vulputate metus, eget suscipit elit."}
}
