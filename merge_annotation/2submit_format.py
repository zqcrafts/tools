import pickle
import numpy as np

pickle_file = open('..\\..\\submit\\dryrun_out.pkl', 'rb')

root_path = 'E:\\Contest\\CVPR_UG2_Challenge\\submit\\res\\'
# pickle.dump(my_list, pickle_file) # 用于保存pkl文件
my_list = pickle.load(pickle_file)
pickle_file.close()

#print(my_list)


#print(np.array(my_list).shape)  # (100, 1, 100, 5) 100张图 每张图一个大的二维数组[[],[],[],[]] 每个大数组里有100个框 每个框有5个lable

#print(my_list[1][0][:][:])
'''[[4.90732666e+02 4.13277557e+02 5.01122650e+02 4.25051697e+02
  5.94111145e-01]
 [6.97390823e+01 3.64878876e+02 9.11068954e+01 3.98298950e+02
  5.70797265e-01]
 [5.72144836e+02 4.13776672e+02 5.80847412e+02 4.23311615e+02
  5.50071180e-01]
 [5.29930176e+02 4.16783295e+02 5.42289001e+02 4.30448730e+02
  5.46356201e-01]
 [5.11651520e+02 4.04505188e+02 5.24270752e+02 4.18196014e+02
  5.44874668e-01]
 [9.89615784e+02 3.66680206e+02 1.00126434e+03 3.79594391e+02
  5.23909211e-01]]'''
#print(my_list[1][0][0][:])
#[490.73267    413.27756    501.12265    425.0517       0.59411114]

#print(my_list[1][0][:][4])
#li = [ True, True, True, True, False]

#print(my_list[1][0][1][4])
#print(my_list[1][0][:][4] > 0.5)
#print(len(my_list[1][0]))
file_name = 0
for j in range(100):#range(len(my_list)):
    print(j)
    r = open(root_path + str(j) + '.txt', 'w', encoding='utf-8')
    for i in range(len(my_list[j][0])):

        if my_list[j][0][i][4] > 0.01:
            print(i)
            x_min = my_list[j][0][i][0]
            y_min = my_list[j][0][i][1]
            w = my_list[j][0][i][2]
            h = my_list[j][0][i][3]
            score = my_list[j][0][i][4]

            r.writelines(str(('%.6f' % x_min)) + ' ')
            r.writelines(str(('%.6f' % y_min)) + ' ')
            r.writelines(str(('%.6f' % w)) + ' ')
            r.writelines(str(('%.6f' % h)) + ' ')
            r.writelines(str(('%.6f' % score)) + '\n')







