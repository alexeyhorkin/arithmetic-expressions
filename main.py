from calculator import calc


def main():
    print("Press 'q' for quit")
    while True:
        try:
            input_str_for_calc = input(">>> ")
            if input_str_for_calc == 'q':
                break
            res = calc(input_str_for_calc)
            print(res)
        except Exception as err:
            print(f"An exception was found: {err}")


if __name__ == "__main__":
    main()
