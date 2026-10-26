# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem


K = int(input())
room_list = list(map(int, input().split()))

room_set = set(room_list)

captain_room = (sum(room_set) * K - sum(room_list)) // (K - 1)

print(captain_room)
