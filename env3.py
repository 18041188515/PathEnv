


class Env:
    def __init__(self):
        self.x_range = (0, 30)
        self.y_range = (0, 30)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 30, 1],
            [1, 0, 30, 1],
            [30, 1, 1, 30]
        ]
        return obs_boundary


    @staticmethod
    def obs_rectangle():
        obs_rectangle = [
            [1,23,4,2],
            [4.9,6.5,12.5,2],
            [8,8,2.5,11],
            [8,23,2,7],
            [9,19.5,13,1.5],
            [18,7,1,6],
            [3,14.5,5,2],



            [11, 3.5, 4, 4.5],
            # [5, 17, 4, 4],


            # [13.1, 6.5, 1.8, 7],
            # 在左下角点（12，12）处 障碍物矩形为 长8 宽2
            [16, 17, 2, 3],
            [14, 22, 3, 5],
            [14, 22, 4, 4],
            # [14, 14, 5.5, 3],

            [18, 7, 10, 2],
            [17, 22, 8, 3],

            [24, 9, 3, 9],
            [26, 18, 2, 6],
            [25,1,5,2],

            [2.5, 2, 15.5, 2]

        ]
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = [
            #[7, 12, 2],
            #[46, 20, 2],
            #[15, 5, 2],
            #[17, 7, 3],
            #[27, 23, 3]
        ]

        return obs_cir
