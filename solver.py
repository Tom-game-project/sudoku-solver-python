from pprint import pprint
import copy
import datetime

import logging

logging.basicConfig(filename="v1.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def possibility(x:int,y:int,arr:list):
    _x=(x//3)*3
    _y=(y//3)*3
    complete_set = set(range(0,10))

    remove_set=set(
        arr[y]+#横
        [i[x] for i in arr]+#縦
        #四角範囲
        arr[_y] [_x:_x+3]+
        arr[_y+1][_x:_x+3]+
        arr[_y+2][_x:_x+3]
    )
    return complete_set-remove_set


def find_zero(arr)->tuple[int,int]:
    # 最も若いzeroを探す
    for y,row in enumerate(arr):
        for x,d in enumerate(row):
            if d==0:
                return x,y

def solver(arr:list[list[int]])->list[list[int]]:
    if True in [0 in i for i in arr]:
        # 0がまだ残っている
        # 0の残る場所を探す
        x,y = find_zero(arr)
        plist=possibility(x,y,arr)
        if len(plist)==0:
            return False
        for i in plist:
            new_arr = copy.deepcopy(arr)
            new_arr[y][x]=i
            if (s:=solver(new_arr)):
                return s
            else:
                pass
    else:
        # 0がもう残っていない
        return arr


if __name__=="__main__":
    arr = [
        [0,0,5,3,0,0,0,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,7,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]
    ]
    t1=datetime.datetime.now()
    pprint(
        solver(arr)
    )
    t2=datetime.datetime.now()

    logging.debug(t2-t1)
