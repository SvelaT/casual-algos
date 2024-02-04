def tryNTimes(try_func, max_tries, ret_value = False):
    success = False
    tries = 0
    while not success and tries < max_tries:
        tries += 1
        try:
            if ret_value:
                return try_func()
            else:
                try_func()
                success = True
        except:
            continue

    if success == False:
        raise Exception("Tried too many times")
