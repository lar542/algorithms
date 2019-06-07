# 의사코드 : 문제와 풀이 방법을 간단한 코드 형태로 설명한 것

# while 반복문으로 나타낼 때
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "열쇠를 찾았어요!"
