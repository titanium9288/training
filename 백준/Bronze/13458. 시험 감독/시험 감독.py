# 시험장의 갯수 N
N = int(input())

people_list = list(map(int, input().split()))
main_manager, sub_manager = map(int, input().split())

total_manager = 0
for people in people_list:
    # 메인 매니저 수를 더하고
    total_manager += 1
    # 총감독관이 감시할 수 있는 인원을 빼고
    people = people - main_manager
    # 마이너스 미리 예외처리
    if people <= 0:
        continue
    # 부감독관이 감시할 수 있는 인원을 나눠서 더하고
    total_manager += int(people / sub_manager)
    # 나머지가 있으면 부감독관 한 명 더 추가
    total_manager += 1 if people % sub_manager != 0 else 0

print(total_manager)