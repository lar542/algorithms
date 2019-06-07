# 의사코드 : 문제와 풀이 방법을 간단한 코드 형태로 설명한 것

# 재귀로 나타낼 때
def look_for_key(box):
  for item in box:
      if item.is_a_box():
          look_for_key(item)
      elif item.is_a_key():
          print "열쇠를 찾았어요!"
