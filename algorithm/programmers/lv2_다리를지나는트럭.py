
## 간신히 시간 통과하긴했는데, 
## 다음에는 ing_t_l길이를 굳이 맞춰줄 필요가 없을것같고, while 비교문에 ing_t_l이 없다면 종료 `while ing_t_l:` 이런식으로 하면 보기가 좀 더 나을듯 
## 변수명도 좀 신경 쓸것 

def solution(bridge_length, weight, truck_weights):
    cnt=0
    ing_t_l =[0]*bridge_length
    f_num= len(truck_weights)
    ck_num=0
    while ck_num<f_num:
        if ing_t_l[0]>0:
            ck_num+=1
        ing_t_l.pop(0)
        b=0
        
        if truck_weights:
            if sum(ing_t_l)<=weight - truck_weights[0]:
                ing_t_l.extend([truck_weights[0]])
                truck_weights.pop((0))    
            else:
                ing_t_l.extend([0])
        else:
            ing_t_l.extend([0])
        cnt+=1
    return cnt