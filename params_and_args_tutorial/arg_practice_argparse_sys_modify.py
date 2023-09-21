'''Parameter & argument 이해
구구단 프로그램 실습 01: sys 모듈 이용하기
'''

import argparse

def multiplication_table(dan: int, n_cols: int = 3) -> None:
    '''구구단 출력 프로그램'''
    print(f'{dan}단을 출력합니다.')
    for num in range(1, 10):
        print(f'{dan} x {num} = {dan*num}', end='\t')
        if num % n_cols == 0:
            print()


def check_positive(value: int):
    '''양의 정수인지 판별'''
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(
            f'{value} is an invalid int, only accept positive int'
        )
    return int_value


def arg_parse() -> object:
    '''Argument Parsing'''
    parser = argparse.ArgumentParser(description='구구단 프로그램 실행 옵션')
    parser.add_argument(
        '-n', '--n_cols', 
        type=check_positive, 
        default=3, 
        help='출력할 열 개수(양의 정수)'
    )
    
    parser.add_argument(
        '-d', '--dan',
        type=int,
        choices=range(2, 10),
        nargs='+',
        default=list(range(2, 10)),
        help='출력할 구구단 선택(복수 선택 가능)\n만약 선택하지 않으면 모두 출력'
    )
    # nargs
    # '*': 0개 이상 argument
    # '+': 1개 이상 argument
    # '?': 0, 1개의 argument
    
    args = parser.parse_args()
    return args


if __name__=='__main__':
    config = arg_parse()
    for x in config.dan:
        multiplication_table(x, config.n_cols)
        print('\n')