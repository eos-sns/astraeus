# -*- coding: utf-8 -*-


from models.astraeus import Astraeus


def main():
    astraeus = Astraeus()
    my_key = astraeus.save('/home/user/wow/secret.json')  # saves secret stuff

    # some days later ...
    if my_key:
        my_val = astraeus.retrieve(my_key)
        print(my_val)  # will print '/home/user/wow/secret.json'
    else:
        print('Error! Astraeus did not save my secret')


if __name__ == '__main__':
    main()
