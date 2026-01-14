"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#asking the user for their age
text = input("Enter your age: ")

#makes the text an integer instead of a word
age = int(text)

#Calcuclating the target heart rate range

#calculating the maximum heart rate
max_heart_rate = 220 - age
#calculating the lower limit of the target heart rate range
lower_limit = max_heart_rate * 0.65
#calculating the upper limit of the target heart rate range
upper_limit = max_heart_rate * 0.85

#f-string to print the calculated values
print("When you excercise to stregthen your heart, you should")
print(f"keep your heart rate between {lower_limit:.0f} and {upper_limit:.0f} beats per minute.")