#coding=utf-8
#val = ((0, 1), (0.5, 0.5), (1, 0))


def mean_and_var(*val):
#val is tuple of tuples - vector[x][y]
#for loop - mean
    x_val = 0
    y_val = 0
    for i in range(len(val)):
        x_val += val[i][0]
        y_val += val[i][1]
    m_x = x_val / len(val)
    m_y = y_val / len(val)
    m = (m_x, m_y)

    #variance is square of deviation from each vec to mean value
    #for loop - variance
    #  each vector x axis - mean x , y axis - mean y
    x_sqDev = 0
    y_sqDev = 0
    for i in range(len(val)):
        x_sqDev += (m_x - val[i][0])**2
        y_sqDev += (m_y - val[i][1])**2
    var_x = (x_sqDev) / len(val)
    var_y = (y_sqDev) / len(val)

    var = (var_x, var_y)
    return m, var


def main():
    v1=(0, 1)
    v2=(0.5, 0.5)
    v3=(1, 0)

    m, var = mean_and_var(v1, v2, v3)
    print("Mean:", m, "Variance:", var)

#run main function
#main()
if __name__=='__main__':
    main()