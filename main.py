# This program will notify you every hour to drink water

import time
from plyer import notification

if __name__ == '__main__':
    while True: 
        notification.notify(
            title="** Please Drink Water! **",
            message="Do you know ? The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon="C:\\Users\\LENOVO\\Desktop\\DrinkWaterNotificationProgram\\app.ico",
        )
        time.sleep(60*60)

# run pythonw ./main.py command to run for the whole time in your computer