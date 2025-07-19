from utilities import getter, timer

import time

if __name__ == "__main__":
    obj = getter.choose_request()
    print(obj)
    getter.construct_request(obj)
