#!/usr/bin/python3.7

import numpy as np
from statistics import mean
from utils_calculation import rmse

################################################################################################### DATA ###################################################################################################

# day 1
Y_day1_pm25_pred_linear = [7.07738002, 6.93705354, 6.79672706, 6.65640058, 6.5160741, 6.37574762, 6.23542114, 6.09509466, 5.95476817, 5.81444169, 5.6741152, 5.53378872, 5.37517152, 5.2346255, 5.09407947, 4.95353345, 4.81298743, 4.67244141]
Y_day1_pm10_pred_linear = [10.46180272, 10.32512942, 10.18845612, 10.05178282, 9.91510952, 9.77843622, 9.64176292, 9.50508962, 9.36841631, 9.23174301, 9.09506971, 8.9583964, 8.7981636, 8.66152446, 8.52488532, 8.38824618, 8.25160704, 8.1149679]

Y_day1_pm25_pred_dectree = [3.6, 4.9, 5.3, 11.4, 2.4, 1.7, 1.5, 6.5, 2.1, 1.7, 2.3, 2.4, 7.3, 1.8, 4.2, 2.3, 5.7, 2.95]
Y_day1_pm10_pred_dectree = [7.2, 6.6, 11.2, 15.2, 3.9, 4.2, 2.4, 9.2, 5.6, 2.2, 5.3, 4.9, 16.0, 3.0, 8.6, 4.6, 7.5, 4.15]

# random forest
Y_day1_pm25_pred_nonlinear = [5.128, 6.20537778, 4.6172, 9.0108, 2.3136, 2.7896, 1.74528857, 5.06964, 2.0076, 2.4944, 4.37346667, 4.6362, 5.58993333, 1.88886667, 4.4796, 2.57822667, 5.61746667, 2.96672397]
Y_day1_pm10_pred_nonlinear = [8.0448, 9.47766667, 9.6712, 12.2396, 3.9011, 4.79180667, 2.84736, 7.76653333, 4.632, 3.386, 10.3562, 10.7316, 12.14313333, 3.05725714, 8.836, 4.65088, 7.58168, 4.14679905]

Y_day1_pm25_pred_xgboost = [7.1034913, 7.848458, 5.991752, 5.4947248, 4.7517133, 3.8783097, 3.8604732, 3.5188808, 3.0797825, 3.5826602, 5.886508, 4.481119, 4.147929, 3.8067164, 3.8298175, 4.2239895, 4.836, 5.3552303]
Y_day1_pm10_pred_xgboost = [9.352692, 12.668023, 12.120275, 8.5140505, 7.6472745, 6.133692, 6.4205017, 4.7452817, 4.7120724, 6.3773513, 14.465195, 9.811093, 8.043576, 6.675679, 6.675679, 6.8679495, 7.4028645, 7.933125]

Y_day1_pm25_pred_neural = [2.9861991620622574, 3.2529232353102997, 2.833568714222929, 2.8951732306872144, 4.2029388009927064, 5.39739141318787, 2.380998434219509, 2.6273996528369024, 2.254084828532359, 2.30471825144632, 3.376097410859802, 4.6820790976642455, 4.077285380335525, 4.313544887387252, 3.9740960280541913, 4.013168234181649, 4.871020436858089, 6.272368616530002]
Y_day1_pm10_pred_neural = [3.280379967344925, 3.354354615195189, 2.862904220458586, 3.0770178710110487, 5.809402132278774, 24.518235314509365, 3.495281555550173, 3.489517645596061, 3.1096659194794487, 3.2839341510320086, 4.942886079347227, 23.526252885034772, 9.001313446415589, 8.987462423194666, 8.630725143861492, 8.784392232866958, 10.070438171422575, 28.418920774629804]

Y_day1_pm25_real_purifier = [3.6, 2.7, 2.1, 2.0, 3.4, 1.4, 2.4, 2.0, 1.9, 1.6, 2.9, 5.8, 4.0, 2.7, 2.6, 2.9, 3.4, 3.1]
Y_day1_pm10_real_purifier = [4.4, 3.8, 4.9, 2.6, 8.8, 1.6, 3.1, 3.6, 2.3, 1.7, 9.2, 10.2, 8.6, 5.0, 3.4, 3.9, 4.5, 3.7]


# day 2
Y_day2_pm25_pred_linear = [6.99779842, 6.8600974, 6.72239639, 6.58469537, 6.44699436, 6.30929334, 6.15038296, 6.01449705, 5.87861114, 5.74272523, 5.60683931, 5.4709534, 5.33378578, 5.19817217, 5.06255856, 4.92694495, 4.79133134, 4.65571774]
Y_day2_pm10_pred_linear = [10.34120426, 10.20726497, 10.07332569, 9.9393864, 9.80544712, 9.6715078, 9.5104224,  9.37874502, 9.24706763, 9.11539024, 8.98371285, 8.85203546, 8.74334873, 8.61319288, 8.48303704, 8.35288119, 8.22272535, 8.0925695]

Y_day2_pm25_pred_dectree = [3.6, 4.9, 5.3, 11.4, 2.4, 1.7, 1.5, 6.5, 2.1, 1.7, 2.3, 2.4, 7.3, 1.8, 4.2, 2.3, 5.7, 2.95]
Y_day2_pm10_pred_dectree = [7.2, 6.6, 11.2, 15.2, 3.9, 4.2, 2.4, 9.2, 5.6, 2.2, 5.3, 4.9, 16.0, 3.0, 8.6, 4.6, 7.5, 4.15]

Y_day2_pm25_pred_nonlinear = [4.8144, 6.0666, 4.5636, 9.1516, 2.3268, 2.69512, 1.79058, 5.06116, 1.91950667, 2.63, 4.41763333, 4.80486667, 5.9688, 2.00416667, 4.10338667, 2.55148381, 5.33557778, 2.92067286]
Y_day2_pm10_pred_nonlinear = [7.9884, 9.98766667, 9.71, 12.1204, 3.8004, 4.89423333, 2.95744, 7.34545238, 4.43523333, 3.2712, 10.95812, 10.1196, 12.979, 3.1015, 7.77879333, 4.56956333, 7.11956444, 4.19956745]

Y_day2_pm25_pred_xgboost = [7.2182436, 7.975764, 6.2945237, 5.5242014, 4.775362, 3.9038806, 3.370165, 3.0427558, 3.0427558, 3.53001, 5.792881, 4.5473194, 4.134843, 3.7832344, 3.800364, 4.1716905, 4.7858286, 5.2527733]
Y_day2_pm10_pred_xgboost = [9.512809, 12.824872, 12.301364, 8.58495, 7.7226086, 6.175265, 5.534, 4.6709156, 4.6244106, 6.295763, 14.075347, 9.655915, 8.03818, 6.591613, 6.591613, 6.7810187, 7.303623, 7.7938514]

Y_day2_pm25_pred_neural = [2.5892248516902328, 2.889826251579507, 2.4128410788616748, 2.4847557217944996, 4.054938334727922, 5.118677819369623, 2.796317005780293, 3.386169384433015, 2.5112652069321486, 2.725867218071653, 5.857263833785692, 5.8768431945129125, 2.695370784663828, 3.236617465330346, 2.4196690762779327, 2.619203544514312, 5.51161800617192, 5.730525927281269]
Y_day2_pm10_pred_neural = [3.180379967344925, 3.2543546151951888, 2.7629042204585854, 2.977017871011048, 5.709402132278774, 24.418235314509367, 4.8488859558245165, 5.413546690030489, 4.306912569340784, 4.79760740948841, 12.060359597450589, 28.591634089371656, 3.4488859558245166, 4.0135466900304895, 2.9069125693407845, 3.39760740948841, 10.660359597450588, 27.191634089371654]

Y_day2_pm25_real_purifier = [2.6, 4.0, 3.9, 4.7, 4.2, 3.7, 2.4, 3.9, 7.7, 3.4, 27.2, 3.8, 2.6, 2.0, 2.4, 2.7, 2.5, 3.4]
Y_day2_pm10_real_purifier = [3.1, 7.8, 6.9, 5.8, 5.7, 5.3, 3.9, 8.6, 14.5, 6.9, 83.4, 8.8, 3.9, 3.0, 3.7, 3.3, 3.5, 3.8]


# day 3
Y_day3_pm25_pred_linear = [6.79894119, 6.6669243, 6.53490741, 6.40289052, 6.27087363, 6.13885673, 5.98140418, 5.85166067, 5.72191716, 5.59217365, 5.46243014, 5.33268664, 5.1956882, 5.06602627, 4.93636434, 4.8067024, 4.67704047, 4.54737854]
Y_day3_pm10_pred_linear = [10.05279973, 9.92535354, 9.79790736, 9.67046118, 9.543015, 9.41556881, 9.24847379, 9.12457559, 9.00067739, 8.87677918, 8.75288098, 8.62898278, 8.49588673, 8.37239347, 8.24890021, 8.12540696, 8.0019137, 7.87842045]

Y_day3_pm25_pred_dectree = [3.6, 4.9, 5.3, 11.4, 2.4, 1.7, 1.5, 6.5, 2.1, 1.7, 2.3, 2.4, 7.3, 1.8, 4.2, 2.3, 5.7, 2.95]
Y_day3_pm10_pred_dectree = [7.2, 6.6, 11.2, 15.2, 3.9, 4.2, 2.4, 9.2, 5.6, 2.2, 5.3, 4.9, 16.0, 3.0, 8.6, 4.6, 7.5, 4.15]

Y_day3_pm25_pred_nonlinear = [5.0844, 6.03346667, 4.5548, 8.6056, 2.2756, 2.55793333, 1.72882762, 5.02219, 1.92937333, 2.556, 4.42283333, 4.79046667, 5.87573333, 1.9053, 4.12512, 2.44630381, 5.29205333, 2.93727651]
Y_day3_pm10_pred_nonlinear = [7.8856, 9.74427429, 9.5904, 12.0124, 3.9184, 5.57814, 2.86716889, 7.47311143, 4.28666667, 3.171, 11.61482667, 10.33836667, 12.8846, 3.03794286, 7.42032667, 4.2594581, 7.02677714, 4.08657841]

Y_day3_pm25_pred_xgboost = [6.9881535, 7.7023273, 5.840645, 5.3938494, 4.7039685, 3.8122482, 3.2821496, 3.0222178, 3.0222178, 3.4844248, 6.0045433, 4.447092, 4.004608, 3.685241, 3.7008796, 4.034871, 4.640937, 5.0711703]
Y_day3_pm10_pred_xgboost = [9.201234, 12.403847, 12.273071, 8.361192, 7.6512585, 6.010355, 5.374178, 4.659411, 4.659411, 6.1496143, 14.869055, 9.41091, 7.74273, 6.378452, 6.378452, 6.5928884, 7.0863795, 7.444259 ]

Y_day3_pm25_pred_neural = [1.790256951516494, 2.1330234810840922, 1.5897927115103814, 1.68914009930013, 3.520697838196793, 4.445109260304162, 3.2902569515164943, 3.6330234810840922, 3.0897927115103814, 3.18914009930013, 5.020697838196793, 5.945109260304162, 5.2488977394998075, 5.5075127866250115, 5.245332743939071, 5.2564422300449225, 5.439443888760434, 7.037868411432282]
Y_day3_pm10_pred_neural = [3.4549034120049327, 3.7022324350313283, 3.00665718727978, 3.293433965276927, 7.487284040695522, 25.89971274199197, 4.454903412004933, 4.702232435031329, 4.00665718727978, 4.293433965276927, 8.487284040695522, 26.89971274199197, 7.456236062198878, 7.496903063298669, 7.181711659219582, 7.288072952511721, 7.621741934365128, 23.866671540460082]

Y_day3_pm25_real_purifier = [1.6, 1.5, 2.0, 2.9, 4.1, 3.6, 3.3, 3.3, 3.4, 3.2, 3.5, 8.9, 5.9, 4.4, 2.7, 2.7, 2.7, 2.8]
Y_day3_pm10_real_purifier = [1.9, 1.6, 2.2, 3.2, 7.2, 5.2, 4.3, 4.0, 4.6, 4.3, 5.1, 17.0, 9.8, 6.9, 5.8, 6.6, 5.9, 4.2]


# day 4
Y_day4_pm25_pred_linear = [6.66618991, 6.54573189, 6.42527388, 6.30481587, 6.18435786, 6.06389984, 5.95852216, 5.83679148, 5.71506079, 5.5933301, 5.47159942, 5.34986873, 5.25210546, 5.13108155, 5.01005763, 4.88903371, 4.76800979, 4.64698587]
Y_day4_pm10_pred_linear = [9.81416281, 9.70001828, 9.58587375, 9.47172922, 9.35758469, 9.24344016, 9.13318891, 9.01871113, 8.90423334, 8.78975555, 8.67527777, 8.56079998, 8.4651785, 8.35163217, 8.23808583, 8.12453949, 8.01099316, 7.89744682]

Y_day4_pm25_pred_dectree = [3.6, 4.9, 5.3, 11.4, 2.4, 1.7, 1.5, 6.5, 11.3, 1.7, 6.4, 2.4, 7.3, 1.8, 4.2, 2.3, 3.0, 2.95]
Y_day4_pm10_pred_dectree = [7.2, 6.6, 11.2, 15.2, 3.9, 4.2, 2.4, 9.2, 14.7, 2.2, 11.85, 4.9, 16.0, 3.0, 8.6, 4.6, 4.1, 4.15]
    
Y_day4_pm25_pred_nonlinear = [5.18830667, 6.1214, 4.5416, 8.9512, 2.3424, 2.7864, 2.5814, 5.10242, 7.96217333, 2.6175, 6.44088095, 5.10193333, 7.002, 1.8645, 4.19014667, 2.41907429, 5.01192, 2.91764405]
Y_day4_pm10_pred_nonlinear = [7.7456, 9.71826667, 9.85, 11.4484, 3.8542, 5.40706667, 4.00930667, 7.44249333, 10.5332, 3.218, 12.91300048, 12.26486667, 13.4294, 3.0049, 7.53336667, 4.35537143, 6.18122857, 4.19609762]

Y_day4_pm25_pred_xgboost = [6.697977, 7.438152, 5.46001, 5.2620587, 4.673912, 3.825478, 3.2969935, 3.139881, 3.139881, 3.539701, 5.948592, 4.6087437, 4.104252, 3.778085, 3.778085, 4.0607195, 4.6510816, 4.9711795]
Y_day4_pm10_pred_xgboost = [8.814346, 12.434882, 11.355644, 8.137886, 7.565974, 5.9405913, 5.3385153, 4.756832, 4.7663307, 6.177214, 14.529797, 9.543498, 7.759013, 6.451571, 6.451571, 6.540318, 7.03628, 7.3609056]

Y_day4_pm25_pred_neural = [9.389224851690233, 9.689826251579507, 9.212840744516871, 9.284755387449696, 10.854938000383118, 11.91867748502482, 9.57140566023445, 9.521873419395707, 9.429535443069472, 8.991136874946097, 10.29995488975037, 10.671520254750067, 10.246580585524498, 10.26419282428833, 10.130206330599322, 9.648861373530963, 10.906647696381697, 11.45728093384605]
Y_day4_pm10_pred_neural = [10.570525627350435, 10.725148713274393, 10.136773849662859, 10.365337408613414, 13.809176099544857, 32.40063957037637, 10.175755112653132, 10.191292287420946, 10.109537527360953, 9.963310133537743, 18.19335537018487, 16.459804750850893, 12.285266885941382, 12.83847620227607, 12.50384009044501, 12.278658352268394, 14.472295436135028, 22.1597132338793]

Y_day4_pm25_real_purifier = [9.9, 9.8, 7.9, 8.2, 9.8, 10.1, 8.1, 7.9, 9.1, 8.7, 11.0, 10.1, 11.3, 9.7, 9.4, 5.3, 2.0, 2.4]
Y_day4_pm10_real_purifier = [11.0, 14.1, 8.8, 9.0, 10.8, 12.6, 8.9, 8.7, 9.9, 9.6, 12.8, 15.6, 18.7, 10.7, 10.5, 8.1, 3.7, 3.1]


################################################################################################### COEFF R2 ###################################################################################################

r2_day1_pm25_linear = [0.028, 0.029, 0.029]
r2_day1_pm10_linear = [0.009, 0.009, 0.009]
r2_day1_pm25_nonlinear = [0.666, 0.675, 0.674]
r2_day1_pm10_nonlinear = [0.646, 0.655, 0.651]
r2_day1_pm25_xgboost = [0.088, 0.093, 0.094]
r2_day1_pm10_xgboost = [0.079, 0.080, 0.081]
#r2_day1_pm25_neural = []
#r2_day1_pm10_neural = []


r2_day2_pm25_linear = [0.028, 0.028, 0.028]
r2_day2_pm10_linear = [0.009, 0.009, 0.008]
r2_day2_pm25_nonlinear = [0.672, 0.668, 0.668]
r2_day2_pm10_nonlinear = [0.651, 0.644, 0.647]
r2_day2_pm25_xgboost = [0.090, 0.089, 0.089]
r2_day2_pm10_xgboost = [0.079, 0.078, 0.080]
#r2_day2_pm25_neural = []
#r2_day2_pm10_neural = []


r2_day3_pm25_linear = [0.027, 0.026, 0.026]
r2_day3_pm10_linear = [0.008, 0.008, 0.008]
r2_day3_pm25_nonlinear = [0.661, 0.657, 0.657]
r2_day3_pm10_nonlinear = [0.643, 0.635, 0.631]
r2_day3_pm25_xgboost = [0.085, 0.083, 0.083]
r2_day3_pm10_xgboost = [0.077, 0.075, 0.075]
#r2_day3_pm25_neural = []
#r2_day3_pm10_neural = []


r2_day4_pm25_linear = [0.024, 0.024, 0.024]
r2_day4_pm10_linear = [0.007, 0.007, 0.007]
r2_day4_pm25_nonlinear = [0.642, 0.641, 0.639]
r2_day4_pm10_nonlinear = [0.621, 0.621, 0.620]
r2_day4_pm25_xgboost = [0.074, 0.074, 0.071]
r2_day4_pm10_xgboost = [0.070, 0.069, 0.069]
#r2_day4_pm25_neural = []
#r2_day4_pm10_neural = []

################################################################################################### TIME ###################################################################################################

times_day1_linear = [0.058, 0.023, 0.124]
times_day1_nonlinear = [73.363, 68.391, 68.452]
times_day1_xgboost = [9.308, 5.182, 9.079]
times_day1_neural = [45.100, 31.961, 31.961]


times_day2_linear = [0.112, 0.104, 0.079]
times_day2_nonlinear = [71.771, 71.308, 72.300]
times_day2_xgboost = [9.625, 9.226, 9.737]
times_day2_neural = [45.930, 35.970, 35.576]


times_day3_linear = [0.110, 0.072, 0.099]
times_day3_nonlinear = [76.851, 75.843, 77.224]
times_day3_xgboost = [9.925, 9.694, 9.653]
times_day3_neural = [50.932, 42.827, 45.674]


times_day4_linear = [0.082, 0.063, 0.115]
times_day4_nonlinear = [83.056, 82.230, 83.165]
times_day4_xgboost = [10.385, 10.544, 10.239]
times_day4_neural = [75.103, 48.491, 57.294]

    
if __name__ == '__main__':
    ### RMSE ###
    rmse_val1_pm25 = rmse(np.array(Y_day1_pm25_pred_xgboost), np.array(Y_day1_pm25_real_purifier))
    rmse_val1_pm10 = rmse(np.array(Y_day1_pm10_pred_xgboost), np.array(Y_day1_pm10_real_purifier))
    rmse_val2_pm25 = rmse(np.array(Y_day2_pm25_pred_xgboost), np.array(Y_day2_pm25_real_purifier))
    rmse_val2_pm10 = rmse(np.array(Y_day2_pm10_pred_xgboost), np.array(Y_day2_pm10_real_purifier))
    rmse_val3_pm25 = rmse(np.array(Y_day3_pm25_pred_xgboost), np.array(Y_day3_pm25_real_purifier))
    rmse_val3_pm10 = rmse(np.array(Y_day3_pm10_pred_xgboost), np.array(Y_day3_pm10_real_purifier))
    rmse_val4_pm25 = rmse(np.array(Y_day4_pm25_pred_xgboost), np.array(Y_day4_pm25_real_purifier))
    rmse_val4_pm10 = rmse(np.array(Y_day4_pm10_pred_xgboost), np.array(Y_day4_pm10_real_purifier))
    
    rmse_val_mean_pm25 = mean([rmse_val1_pm25, rmse_val2_pm25, rmse_val3_pm25, rmse_val4_pm25])
    rmse_val_mean_pm10 = mean([rmse_val1_pm10, rmse_val2_pm10, rmse_val3_pm10, rmse_val4_pm10])
    
    #print(f'RMSE day 1 PM2.5: {rmse_val1_pm25:.3f}')
    #print(f'RMSE day 1 PM10: {rmse_val1_pm10:.3f}\n')
    #print(f'RMSE day 2 PM2.5: {rmse_val2_pm25:.3f}')
    #print(f'RMSE day 2 PM10: {rmse_val2_pm10:.3f}\n')
    #print(f'RMSE day 3 PM2.5: {rmse_val3_pm25:.3f}')
    #print(f'RMSE day 3 PM10: {rmse_val3_pm10:.3f}\n')
    #print(f'RMSE day 4 PM2.5: {rmse_val4_pm25:.3f}')
    #print(f'RMSE day 4 PM10: {rmse_val4_pm10:.3f}')
    
    #print(f'RMSE mean PM2.5: {rmse_val_mean_pm25:.3f}')
    #print(f'RMSE mean PM10: {rmse_val_mean_pm10:.3f}')
    
    ### R2 ###
    r2_val1_pm25 = mean(r2_day1_pm25_nonlinear)
    r2_val1_pm10 = mean(r2_day1_pm10_nonlinear)
    r2_val2_pm25 = mean(r2_day2_pm25_nonlinear)
    r2_val2_pm10 = mean(r2_day2_pm10_nonlinear)
    r2_val3_pm25 = mean(r2_day3_pm25_nonlinear)
    r2_val3_pm10 = mean(r2_day3_pm10_nonlinear)
    r2_val4_pm25 = mean(r2_day4_pm25_nonlinear)
    r2_val4_pm10 = mean(r2_day4_pm10_nonlinear)
    
    r2_val_mean_pm25 = mean([r2_val1_pm25, r2_val2_pm25, r2_val3_pm25, r2_val4_pm25])
    r2_val_mean_pm10 = mean([r2_val1_pm10, r2_val2_pm10, r2_val3_pm10, r2_val4_pm10])
    
    #print(f'R2 day 1 PM2.5: {r2_val1_pm25:.3f}')
    #print(f'R2 day 1 PM10: {r2_val1_pm10:.3f}\n')
    #print(f'R2 day 2 PM2.5: {r2_val2_pm25:.3f}')
    #print(f'R2 day 2 PM10: {r2_val2_pm10:.3f}\n')
    #print(f'R2 day 3 PM2.5: {r2_val3_pm25:.3f}')
    #print(f'R2 day 3 PM10: {r2_val3_pm10:.3f}\n')
    #print(f'R2 day 4 PM2.5: {r2_val4_pm25:.3f}')
    #print(f'R2 day 4 PM10: {r2_val4_pm10:.3f}')
    
    #print(f'R2 mean PM2.5: {r2_val_mean_pm25:.3f}')
    #print(f'R2 mean PM10: {r2_val_mean_pm10:.3f}')
    
    ### times ###
    times_val1 = mean(times_day1_neural)
    times_val2 = mean(times_day2_neural)
    times_val3 = mean(times_day3_neural)
    times_val4 = mean(times_day4_neural)
    
    times_val_mean = mean([times_val1, times_val2, times_val3, times_val4])
    
    #print(f'Times day 1: {times_val1:.3f}')
    #print(f'Times day 2: {times_val2:.3f}')
    #print(f'Times day 3: {times_val3:.3f}')
    #print(f'Times day 4: {times_val4:.3f}')
    
    #print(f'Times mean: {times_val_mean:.3f}')