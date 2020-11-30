def main(n):
    square_sum = 0
    sum_of_sqr = 0
    for i in range(n):
        sum_of_sqr += i * i
        square_sum += i
    square_sum *= square_sum
    return square_sum - sum_of_sqr


if __name__ == '__main__':
    print(main(1000))
