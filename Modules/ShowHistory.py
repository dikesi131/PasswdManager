# 读取log文件
def read_history(num_lines:str):
    with open('access.log', 'r', encoding='utf-8') as file:
        try:
            for _ in range(int(num_lines)):
                line = file.readline()
                if not line:
                    break

                print(line.strip())
        except Exception as e:
            print(f'error: {e}')