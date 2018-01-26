def digitProduct(product):
    original_product = product
    result = ''
    if product == 0:
        return 10
    if product < 10:
        return product

    for i in range(2, 10)[::-1]:
            while product % i == 0:
                result += str(i)
                product /= i 
    # interchangable with for-loop code above             
    # def recursion(prod, iteration):
        
    #     while prod % iteration == 0:
    #         global result += str(iteration)
    #         prod /= iteration
    #         if iteration >= 2:
    #             return result = result + recursion(prod, iteration-1)
    #     iteration -= 1      
    # recursion(product, 9)
                               
    if len(result) == 0 or len(result) < len(str(original_product)):
        return -1
    return int(result[::-1]) 
# Test Cases:
for x in range(0, 40):
    print('X:{0}, result:{1}'.format(x, digitProduct(x)))
# input: 243 Output: 399
# input: 576 output: 889
# input: 360 output: 589
print('X:{0}, result:{1}'.format(243, digitProduct(243)))
print('X:{0}, result:{1}'.format(576, digitProduct(576)))
print('X:{0}, result:{1}'.format(360, digitProduct(360)))