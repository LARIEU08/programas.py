import wpilib
import wpilib.drive
import ctre

class MyRobot(wpilib.TimedRobot):
     def robotInnit(self):
     # os 4 motores da tração
       self.m_left_front = ctre.WPI_victorSPX(22)
       self.m_right_front = ctre.WPI_victorSPX(33)
       self.m_left_rear = ctre.WPI_victorSPX(11)
       self.m_right_rear = ctre.WPI_victorSPX(44)
     # motores dos mecanismos
       self.shooter = ctre.WPI_VictorSPX(9)
       self.track_ball = ctre.WPI_VictorSPX(8)
       self.ball_catcher = ctre.WPI_VictorSPX(55)
     # lado esquendo e lado direito da tração 
       self.m_left = wpilib.SpeedControllerGroup(self.m_left_front,self.m_left_rear)
       self.m_right = wpilib.SpeedControllerGroup(self.m_right_front,self.m_right_rear)
     # criando tração com objeto
       self.MyRobot = wpilib.drive.DifferentialDrive(self.m_left,self.m_right)
       self.myRobot.setExpiration(0.1)
     #criando um joystick
       self.stick = wpilib.joystick(0)
     #criar uma camera
     wpilib.CameraServer.launch('vision.py:main')
     #criando um relogio para contar o tempo
       self.timer = wpilib.Timer()
#criando o teleoperado
def teleopInit(self):
    self.MyRobot.setSafetyEnabled(True)

#criar o periodo teleoperado
def teleopPeriodic(self):
    if self.stick.getRawButton(5)  == True:
        self.MyRobot.arcadeDrive( 
            -self.stick.getRawAxis(1),self.stick.getRawAxis(0)1.15,True
        )
    else:
        self.MyRobot.arcadeDrive(self.stick.getRawAxis(1),self.stick.getRawAxis(0)1.15, True

        )