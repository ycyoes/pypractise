import numpy as np
import pandas as pd

def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result

def main():
    y = np.random.randint(2, size=(50, 1))
    x = np.random.randint(10, size=(50, 1))
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    print('data\n', data)
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        # print('i=', i, (data.index != i), '\n', data[data.index != i])
        groupby_result = data[data.index != i].groupby(['x'], as_index=False).agg(['mean', 'count'])
        print('groupby_result: ', groupby_result, ' :end')
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, 'x'], ('y', 'mean')]
        print('i: ', i, result[i])


    result_1 = target_mean_v1(data, 'y', 'x')
    # result_2 = target_mean_v2(data, 'y', 'x')
    print(result_1)
    print(result_1.shape)


if __name__ == '__main__':
    main()







