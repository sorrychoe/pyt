import pytest
from hash_level2 import solution


# 주어진 테스트 케이스
def test_case_1():
    phone_book1 = ["119", "97674223", "1195524421"]
    assert solution(phone_book1) == False

# 모든 전화번호가 다른 번호의 접두어가 아닌 경우


def test_case_2():
    phone_book2 = ["123", "456", "789"]
    assert solution(phone_book2) == True

# 일부 번호가 다른 번호의 접두어인 경우


def test_case_3():
    phone_book3 = ["12", "123", "1235", "567", "88"]
    assert solution(phone_book3) == False

# 모든 전화번호가 다른 번호의 접두어인 경우


def test_case_4():
    phone_book4 = ["911", "97674223", "1195524421"]
    assert solution(phone_book4) == True

# 모든 전화번호가 동일한 경우


def test_case_5():
    phone_book5 = ["12345", "12345", "12345", "12345"]
    assert solution(phone_book5) == False


# 모든 전화번호가 한 자리 숫자인 경우
def test_case_6():
    phone_book7 = ["1", "2", "3", "4", "5"]
    assert solution(phone_book7) == True

# 모든 전화번호가 20자리인 경우


def test_case_7():
    phone_book8 = ["12345678901234567890",
                   "23456789012345678901", "34567890123456789012"]
    assert solution(phone_book8) == True

# 일부 번호가 다른 번호의 접두어인 경우


def test_case_8():
    phone_book9 = ["1", "11", "2", "22", "111"]
    assert solution(phone_book9) == False


if __name__ == "__main__":
    pytest.main()
