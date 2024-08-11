# map, filter, zip and reduce
# study reduce later


def multiply_by_two(item): # for map
    return item*2


def is_odd(item): # for filter
    return item % 2 != 0


def main():
    my_list = [1, 2, 5, 21, 30, 45]
    your_list = [10, 30, 60]


    map_list = list(map(multiply_by_two, my_list))
    filter_list = list(filter(is_odd, my_list))
    zip_list = list(zip(my_list, your_list))


    print(f'My List: {my_list}')
    print(f'Map List: {map_list}')
    print(f'Filter List: {filter_list}')
    print(f'Zip List: {zip_list}')
    

if __name__ == "__main__":
    main()