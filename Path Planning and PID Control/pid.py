class PIDController:
    def __init__(self, target_pos):
        self.target_pos = target_pos
        self.Kp = 0.0
        self.Ki = 0.0
        self.Kd = 0.0
        self.bias = 0.0
        self.error_cumm = 0
        self.error_prev = 0
        return

    def reset(self):
        return

#TODO: Complete your PID control within this function. At the moment, it holds
#      only the bias. Your final solution must use the error between the 
#      target_pos and the ball position, plus the PID gains. You cannot
#      use the bias in your final answer. 
    def get_fan_rpm(self, vertical_ball_position):
        
        error = self.target_pos - vertical_ball_position
        self.error_cumm += (error * (1/120)) 
        
        error_derivative = (error - self.error_prev) / (1/120)
        
        output = (self.Kp * error) + (self.Ki * self.error_cumm) + (self.Kd * error_derivative) + self.bias
        
        if output < 0:
            output = 0
        
        self.error_prev = error
        return output
