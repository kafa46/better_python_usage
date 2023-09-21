'''Parameter & argument 이해
구구단 프로그램 실습 01: sys 모듈 이용하기
'''

import sys

def multiplication_table(dan: int, n_cols: int = 3) -> None:
    '''구구단 출력 프로그램'''
    print(f'{dan}단을 출력합니다.')
    for num in range(1, 10):
        print(f'{dan} x {num} = {dan*num}', end='\t')
        if num % n_cols == 0:
            print()


def arg_parser(args) -> None:
    '''전달인자 해석 및 구구단 실행'''
    # 아무것도 입력하지 않을 경우 default 값 설정
    print('''Usage:
          python arg_practice_sys.py [출력할 열의 개수(양의 정수)] [출력할 구구단]
          아무것도 입력하지 않으면 2단부터 9단까지 3열씩 모두 출력
''')
    if len(args) == 1:
        print('모든 구구단을 출력합니다.')
        for x in range(2, 10):
            multiplication_table(x)
            print()
        return
    
    # 출력할 컬럼(열) 개수 확인
    if not args[1].isdecimal():
        print('출력할 열의 개수는 숫자이어야 합니다.')
        return
    if int(args[1]) < 1:
        print('출력할 열 개수는 양의 정수이어야 합니다.')
        return
    n_cols = int(args[1])
    
    # 문제점: 열 개수를 지정한 것인지, 구구단 단을 지정한 것인지
    # 매우 혼란스러울 수 있음.
    
    # 예외처리: 단(dan) argument 정수인지 검사
    for x in args[2:]:
        if not x.isdecimal():
            print(f'출력을 요청한 구구단: {x}')
            print('구구단 인자는 숫자만 가능합니다.')
            return
    
    # 예외처리: 출력할 단(dan)이 2와 9사이인지 검사
    for x in args[2:]:
        if not (int(x)>=2 and int(x)<=9):
            print(f'출력을 요청한 구구단: {x}')
            print('구구단 인자는 2부터 9까지 입니다.')
            return
        
    # 나머지 경우 -> 입력받은 열 개수 + 입력받은 단을 출력
    for x in args[2:]:
        multiplication_table(int(x), n_cols=n_cols)
        print('\n')
    

if __name__=='__main__':
    print(sys.argv)
    arg_parser(sys.argv)