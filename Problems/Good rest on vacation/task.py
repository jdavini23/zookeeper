# put your python code here
days = int(input())
food_cost = int(input()) * days
flight_cost = int(input()) * 2
hotel_night = int(input()) * (days - 1)

print(food_cost + flight_cost + hotel_night)