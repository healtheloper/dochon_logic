cur_time = input()
cur_h, cur_m, cur_s = map(int, cur_time.split(":"))

th_time = input()
th_h, th_m, th_s = map(int, cur_time.split(":"))
time = 0
while cur_time != th_time:
    cur_s += 1
    if cur_s >= 60:
        cur_m += 1
        cur_s = 0
    if cur_m >= 60:
        cur_h += 1
        cur_m = 0
    if cur_h >= 24:
        cur_h = 0
    cur_h_s = f"{cur_h if cur_h >= 10 else f'0{cur_h}'}"
    cur_m_s = f"{cur_m if cur_m >= 10 else f'0{cur_m}'}"
    cur_s_s = f"{cur_s if cur_s >= 10 else f'0{cur_s}'}"
    cur_time = cur_h_s+":"+cur_m_s+":"+cur_s_s
    time += 1

if time != 0:
    time_h = time // 3600
    time -= 3600*time_h
    time_m = time // 60
    time -= 60*time_m
    time_s = time

    time_h_s = f"{time_h if time_h >= 10 else f'0{time_h}'}"
    time_m_s = f"{time_m if time_m >= 10 else f'0{time_m}'}"
    time_s_s = f"{time_s if time_s >= 10 else f'0{time_s}'}"
    time_string = time_h_s+":"+time_m_s+":"+time_s_s
    print(time_string)
else:
    print("24:00:00")
