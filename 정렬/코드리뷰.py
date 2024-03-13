# (x, y , mode- number)형태

if __name__=="__main__":
    try: 
        test_track = pm() # pm이라는 클래스의 객체 선언 

# pm클래스의 생성자 
    def __init__(self):
        rospy.init_node("path_maker")
        now = datetime.now() # 현재 시간 받음
        # read file (Input mode)
    
        self.f = open(ROS_HOME + "/paths/{}-{}-{}_{}-{}-{}.txt".format(now.year, now.month, now.day, now.hour, now.minute), 'w')
        #text 형태의 파일을 열게 됨 
        # ROS_HOME이라는 변수에 저장된 pure_pursuit하위 경로인 paths 안에 
        # year-month-day-hour-minute이라는 이름을 가지게 됨 

        rospy.Subscriber('utmk_coordinate',Point,self.callback) 
        #앞에 wgs84_to_utmk.py에서 발행하는 토픽을 받아 클래스 내부의 콜백함수 실행 

        def callback(self, msg): 
            self.is_status = True 
            self.status_msg = msg 

        #여기서 정의된 is_status 다음에 씀
        # 아래는 생성자에 있는 while문 
        while not rospy.is_shutdown():
            if self.is_status:
                self.path_make()    
            rate.sleep()

    def path_make(self):
        x= self.status_msg.x
        y= self.status_msg.y
        distance = sqrt(pow(x - self.prev_x, 2)+ pow(y - self.prev_y,2))
    
        if distance >0.2:
            self.f.write(str(x) +" " + str(y) + " "+ " 9" + "\n")#9번은 모드인가뭐지? 
            self.prev_x=  x 
            self.prev_y= y 
            self.idx +=1
            print(self.idx, x, y ) 


    # 모드 변경은 언제하는가?path속 모드 번호를 변경해줘야함 
    # 이때 사용되는 노드느 waypoing_changer 라는 파이썬 파일 
    # path 폴더 안에 path 들과 함꼐 위치 
    # 해당 노드 속 코드가 동일한 디렉토리에 위치해 있는 path만 인식하도록 경로를고정해 두었기 때문 