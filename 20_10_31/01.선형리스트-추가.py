# 선형 리스트 구현
# 카톡 친구들의 선형 리스트

katok = []  # 빈 배열


# 배열의 제일 뒤에 친구를 추가하는 함수
def add_data(friend):
    katok.append(None)  # 빈칸 추가
    KLen = len(katok)  # 배열의 현재 크기 확인
    katok[KLen - 1] = friend  # 배열 제일 뒤에 친구 추가


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)