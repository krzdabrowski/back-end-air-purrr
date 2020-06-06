#!/usr/bin/python3.7

from matplotlib import pyplot as plt


def plot_airly(type_of_pm, Y_pred, Y_real, filename):
    X = [
    '07:00', '08:00', '09:00', '10:00', '11:00', '12:00',
    '13:00', '14:00', '15:00', '16:00', '17:00', '18:00',
    '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'
    ]
    
    max_y = max(Y_real + Y_pred)
    
    plt.rc('xtick',labelsize=6)
    plt.xlabel("Godzina") 
    plt.ylabel(u"${}\ [\u03bcg/m^3]$".format(type_of_pm)) 
    plt.margins(0,0)
    
    plt.plot(X, Y_real, '-b', linewidth=2, label='Pomiar')
    plt.plot(X, Y_pred, '-r', linewidth=2, label='Predykcja')
    plt.legend()
    
    ax = plt.gca()
    ax.set_xticks(['07:00', '12:00', '13:00', '18:00', '19:00', '24:00'])
    ax.set_ylim(bottom=0, top=max_y+2)   

    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()


if __name__ == '__main__':
    # day 1
    Y_day1_pm25_pred = [11.65, 10.8, 10.41, 9.08, 8.86, 8.44, 6.66, 5.85, 5.66, 5.01, 4.36, 4.25, 5.05, 6.89, 8.66, 10.89, 11.21, 10.94]
    Y_day1_pm10_pred = [17.07, 16.07, 14.91, 13.5, 13.03, 12.26, 9.09, 8.33, 7.5, 6.68, 5.8, 5.38, 6.86, 9.51, 12.81, 15.83, 17.19, 16.49]
    
    Y_day1_pm25_real = [14.39, 9.64, 6.58, 7.05, 6.86, 4.58, 6.35, 5.71, 5.35, 5.21, 5.19, 5.53, 7.44, 7.89, 8.4, 10.34, 11.47, 10.57]
    Y_day1_pm10_real = [19.35, 12.7, 8.63, 9.16, 8.81, 5.94, 8.3, 7.43, 6.94, 6.77, 6.72, 7.16, 9.7, 10.32, 11.0, 13.62, 15.08, 13.99]

    # day 2
    Y_day2_pm25_pred = [10.8, 10.57, 10.29, 9.55, 9.25, 9.55, 11.75, 10.91, 10.67, 10.23, 10.69, 11.04, 10.62, 11.76, 11.93, 12.53, 12.44, 11.68]
    Y_day2_pm10_pred = [16.64, 16.03, 15.21, 14.19, 13.93, 13.96, 17.54, 16.3, 15.96, 15.58, 15.89, 16.11, 16.28, 17.21, 18.09, 18.74, 19.03, 18.02]
    
    Y_day2_pm25_real = [14.53, 16.36, 17.28, 16.16, 16.2, 16.98, 12.42, 12.33, 12.94, 13.84, 14.59, 14.63, 13.66, 9.49, 11.14, 13.52, 15.0, 16.73]
    Y_day2_pm10_real = [19.11, 21.4, 22.5, 21.03, 21.06, 21.99, 16.09, 15.84, 16.67, 18.06, 18.91, 19.44, 17.34, 12.47, 14.87, 17.96, 19.95, 22.44]
    
    plot_airly('PM_{2,5}', Y_day2_pm25_pred, Y_day2_pm25_real, 'day2.png')
    plot_airly('PM_{10}', Y_day2_pm10_pred, Y_day2_pm10_real, 'day2_2.png')