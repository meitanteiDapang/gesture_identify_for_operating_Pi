import socket

IP = "192.168.191.2"
PORT = 8081

def main_control(choice, udp_socket):
    if 1 == choice:
        import pwm_led as target
    elif 2 == choice:
        import moto as target
    try:
        while(True):
            # 3. 接收数据
            recv_data = udp_socket.recvfrom(1)                
            data = recv_data[0].decode("utf-8")
            
            #data = input("please input:")
    
            #4. 打印接收到的数据
            print(data)
            cmd = int(data) 
        
            if(0 == cmd):
                #0手势 蓝灯闪烁/前向加速/后向减速
                target.cmd0()
                pass
            elif(1 == cmd):
                #1手势 绿灯闪烁/后向加速/前向减速
                target.cmd1()
                pass           
            elif(2 == cmd):
                #5手势 红灯闪烁/停止
                target.cmd2()
                pass
            else:
                #空手势 不亮灯/保持速度
                target.cmd3()
                pass
    except KeyboardInterrupt:
        pass
        
def main():
    
    choice = int(input("1 for led_control,\n2 for moto_control,\n0 for exit.\nplease input your choice:"))
    # 1. 创建套接字(ipv4地址，udp协议)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. 绑定一个本地信息
    localaddr = (IP, PORT)
    udp_socket.bind(localaddr)    
   
    main_control(choice, udp_socket)
      
    # 5. 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
