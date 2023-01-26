import time

class TrafficLight():

    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.wait_period = None
        self.__color = color
        print()

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color=''):

        if not color:
            loc_color = self.__color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()