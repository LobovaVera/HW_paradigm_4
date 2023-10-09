import math
from statistics import mean

def pearson_corr(array_x, array_y):
    x_mean = mean(array_x)
    y_mean = mean(array_y)
    return (
                sum(list(map(lambda x,y: (x - x_mean) * (y - y_mean), array_x, array_y)))/
                (
                    math.sqrt(sum(list(map(lambda x: (x - x_mean)**2, array_x)))) *
                    math.sqrt(sum(list(map(lambda y: (y - y_mean)**2, array_y))))
                )
            )

array_x = [1,2,4,5,6]
array_y = [2,4,8,10,12]







def main():
    print('Коэффициент корреляции: %f' % pearson_corr(array_x, array_y))


if __name__ == '__main__':
    main()