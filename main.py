def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    get_user_input = input()
    get_user_input = get_user_input.split(",") # split the input string into a list

    # convert the list of STRINGS to a list of FLOATS - basically EVERY num in the list is being converted to float
    num_list = [float(num) for num in get_user_input]

    print(num_list) # print the list of floats
    return num_list  # return the num_list so that all other functions can use in the main funciton

def calc_average(num_list):
    average = sum(num_list) / len(num_list)
    print("Average: " + str(average))

def find_min_max(num_list):
    maximum_value = max(num_list)
    minimum_value = min(num_list)

    print("Max: " + str(maximum_value))
    print("Min: " + str(minimum_value))

def sort_temperature(num_list):
    print("sort_temperature")

def calc_median_temperature(num_list):
    print("calc_median_temperature")

if __name__ == "__main__":
    main()