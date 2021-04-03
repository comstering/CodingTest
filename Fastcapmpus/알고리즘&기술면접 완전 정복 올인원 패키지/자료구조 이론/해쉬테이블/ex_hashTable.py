# 파이썬의 딕셔너리가 존재하기에 구현할 필요 없음
# 해쉬테이블의 이해를 위해 간단하게 구현
hash_table = [0 for i in range(10)]
print(hash_table)


# 해쉬 함수
def hash_func(key):
    return key % 5


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# 문자의 아스키 코드값 추출
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))


# 해쉬 테이블 기능 구현
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')


# 해쉬테이블 데이터 출력
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print(get_data('Andy'))

# 리스트 변수를 활용해서 해쉬 테이블 구현하기
hash_table = [0 for i in range(8)]

def get_key(data):
    return hash(data)
def hash_function(key):
    return key % 8
def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '01023015054')
save_data('Andy', '01048536897')
print(read_data('Dave'))
print(hash_table)

# 충돌(Collision) 해결 알고리즘
# 1. Chaining 기법(개방 해싱, open hashing)
hash_table = [0 for i in range(8)]

def get_key_chain(data):
    return hash(data)
def hash_function_chain(key):
    return key % 8
def save_data_chain(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
def read_data_chain(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data_chain('Dave', '01023015054')
save_data_chain('Andy', '01048536897')
print(read_data_chain('Dave'))
print(hash_table)

# 2. Linear Probing 기법(패쇄 해싱, close hashing)
hash_table = [0 for i in range(8)]

def get_key_linear(data):
    return hash(data)
def hash_function_linear(key):
    return key % 8
def save_data_linear(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key, value]
def read_data_linear(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None

save_data_linear('Dave', '01023015054')
save_data_linear('Andy', '01048536897')
print(read_data_linear('Dave'))
print(hash_table)

# 3. 빈번한 충돌을 개선하는 기법
# 1) 해쉬 함수의 재정의 및 해쉬 테이블 저장공간 확대
hash_table = [0 for i in range(16)]
def hash_func(key):
    return key % 16

# 해쉬함수와 키 생성 함수
import hashlib

# SHA-1
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# SHA-256
hash_object = hashlib.sha256()
hash_object.update(b'test')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Chain 기법 키생성을 SHA-256으로 변경
hash_table = [0 for i in range(8)]

def get_key_chain_sha256(data):
    hash_obj = hashlib.sha256()
    hash_obj.update(data.encode())
    return int(hash_obj.hexdigest(), 16)
def hash_function_chain_sha256(key):
    return key % 8
def save_data_chain_sha256(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
def read_data_chain_sha256(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data_chain_sha256('Dave', '01023015054')
save_data_chain_sha256('Andy', '01048536897')
print(read_data_chain_sha256('Dave'))
print(hash_table)