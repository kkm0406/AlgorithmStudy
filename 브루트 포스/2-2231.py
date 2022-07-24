n = int(input())
sum = 0
for i in range(1, n + 1):
    tmpSum = 0
    for j in str(i):
        tmpSum += int(j)
    if tmpSum+i == n:
        sum = i
        break
print(sum)


# 브루트포스-분해합, 브론즈2



num = int(input()) # 값을 입력받음

sum_list = int(0) #list의 합을 초기화
final_sum = int(0) #최종 결과 초기화
changenum = (num) # num을 직접 바꾸지 않음

count = int(0) # count를 설정
min = int(0) # 최소합
for i in range(num):
    changenum = changenum-1 #모든 수를 다 구한다
    num_list = list(map(int, str(changenum))) # num의 자릿수를 배열로 저장
    sum_list = sum(num_list) # list의 자릿수별로 합침
    final_sum = sum_list + changenum #최종 값은 자릿수 + 원래 수
    if(num == final_sum): # 만약 최종값이 num과 같다면 분해합이다
        if(count == 0): # 만약 count가 0이라면
            min = changenum #min의 값을 changenum값으로 설정
        elif(changenum < min): #만약 분해합이 여러개라면 작은 값을 min으로 설정
            min = changenum
        count += 1 # count를 설정
    else: # 다르다면 그냥 진행
        continue
if(count == 0): # 분해합이 존재하지 않는다면 0을 print
    print(0)
else: # 분해합이 존재하면 가장 작은 분해합을 print
    print(min)



