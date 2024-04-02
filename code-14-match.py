# match
match 200:
    case 400:
        print("Bad request")
    case 404:
        print("not found")
    case 418:
        print("I'm a teapot")
    case _:  # 通配符, 确保 match 必定会匹配成功
        print("Something's wrong with the internet")

match 400:
    case 400 | 403 | 404:
        print("4xx error")
    case 500 | 501 | 503:
        print("5xx error")
    case 200 | 2001 | 210:
        print("success")
    case _:  # 通配符, 确保 match 必定会匹配成功
        print("Something's wrong with the internet")
