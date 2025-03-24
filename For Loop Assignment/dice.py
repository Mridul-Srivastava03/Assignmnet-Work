dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
count_6 = 0
count_1 = 0
count_66 = 0
for i in dice_result:
    if i == 6:
        count_6 += 1
        if(dice_result[i+1] == 6):
            count_66 += 1
    elif i == 1:
        count_1 += 1
print("Times of getting 6: ", count_6)
print("Times of getting 1: ", count_1)
print("Times of getting 6 after getting 6: ", count_66)