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
    for i in range(len(result)):
        print(f'{i:02d} {result[i]}')

    # it's more complex but you could use a comprehension
    # print('\n'.join(f'{i:02d} {result[i]}' for i in range(len(result)))