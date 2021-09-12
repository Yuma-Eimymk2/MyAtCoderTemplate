#参考：https://qiita.com/KoyanagiHitoshi/items/3286fbc65d56dd67737c

###標準出力###
print()   #←カッコ内は変数名、数字、"文字列"

#list
x = [1,2,3,4,5]
print(x)   #←リストを表示する

#listの各要素を出力する
for i in x:
    print(i)

###入力###
#1行１列(整数)
x = int(input())

#文字列を１つの変数に入力する
x = input()
print(x)

#文字列を複数の変数に格納する
#変数名A,B,C = input()
x, y, z = input()
print(x,y,z)   #入力123 出力1 2 3となる

#整数を複数の変数に格納する
x,y = map(int, input().split())

#文字列を複数の変数に格納する
A, B = input().split()

#リストに整数を格納する
#リスト名 = list(map(int, input().split()))
x = list(map(int, input().split()))

#リストに整数を格納する(改行あり)
#リスト名 = [int(input()) for 変数 in range(変数の数)]
x = [int(input()) for i in range(n)]

#リストに文字列を格納する(改行あり)
#リスト名 = [input() for 変数 in range(変数の数)]
x = [input() for i in range(n)]

#複数行・複数列の入力
#リスト名 = [list(map(int, input().split())) for 変数 in range(入力行数)]
rows = int(input())
x = [list(map(int, input().split())) for i in range(rows)]
print(x)








