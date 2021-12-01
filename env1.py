


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
            [0, 21, 7, 1.5],
            [4, 6, 2, 7],
            [8, 26, 7, 1.5],
            [6, 14, 12, 1.5],
            [10, 5, 6, 1.5],
            [10, 23, 2, 7],
            [16, 8, 4, 4],
            [18, 22, 7, 2.5],
            [23, 0, 2, 7],
            [23, 18.5, 7, 2]

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
