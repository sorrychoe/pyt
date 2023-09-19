def solution(phone_book):
    # 전화번호를 정렬
    phone_book.sort()

    # 인접한 두 번호를 비교하면서 접두어 여부 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
