scanner = input("Dart score : ")
len_score = len(scanner) # 입력된 값의 길이
step = 1 # 1: 점수 2:보너스 3:옵션
lenPos = 0 # 입력된 값의 위치
score_pos = 0 # 점수의 좌표
score = [0,0,0]

while lenPos<len_score :
    target = scanner[lenPos]
    if step == 1: #1.1 1단계 점수 처리( 숫자만 올 수 있다.)
        try :
            score[score_pos] = int(target)
            step+=1
        except : # 1.3 3단계 옵션 처리
            if target == "*": # 1.3.1 스타상
                score[score_pos-1] = score[score_pos-1]*2
                if score_pos>1:
                    score[score_pos-2] = score[score_pos-2]*2
            elif target == "#": #1.3.2 아차상
                score[score_pos-1] = score[score_pos-1]*(-1)
            else:
                print('유효한 다트 점수가 아닙니다.')
                        
    elif step == 2: # 1.2. 2단계 보너스 처리
        if target == 'S':#1.2.1 single
            score[score_pos] = pow(score[score_pos],1)
        elif target == 'D': #1.2.2 double
            score[score_pos] = pow(score[score_pos],2)
        elif target == 'T':#1.2.3 triple
            score[score_pos] = pow(score[score_pos],3)
        elif target == '0': #10점 처리
            if score[score_pos] == 1:
                score[score_pos] = 10
                score_pos-=1
                step+=1
        else:
            print('유효한 다트 점수가 아닙니다.')
            
        score_pos+=1
        step-=1
        
    lenPos+=1
    
    
print(score[0]+score[1]+score[2])

