import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')

# 원하는 만큼 argument 추가
parser.add_argument('--print-number', type=int, help='입력 정수값까지 출력할 숫자 입력', required=True)
parser.add_argument('--welcome-msg', type=str, help='숫자 뒤에 붙을 인사말', default='welcome')

args = parser.parse_args()

for i in range(args.print_number):
    print(f'print number {i+1} -- {args.welcome_msg}')