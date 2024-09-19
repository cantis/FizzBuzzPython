def main():
    result = list()

    for x in range(1, 100):
        if x%3 == 0 and x%5 == 0:
            result.append('FizzBuzz')
            continue
        if x%3 == 0:
            result.append('Fizz')
            continue
        if x%5 == 0:
            result.append('Buzz')
            continue
        result.append(str(x))

    return result


if __name__ == '__main__':
    result = main()
    line_no = 0
    for value in result:
        line_no += 1
        print(f'{line_no:02d} {value}')P