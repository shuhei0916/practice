def is_palindrome(str):
    # for s in str:
          
    # print(str[:-1])
    return str == str[::-1]


def main():
    s1 = ['k', 'e', 'i', 'o']
    s2 = ['m', 'a', 'd', 'a', 'm']
    s3 = 'Python'
    
    # print(type(s1))
    # print(type(s3))
    
    # print(s3[:-1])
    # print(s1[:-1])
    
    # num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(num[::2])
    # print(num[1::2])
    
    
    
    print(s1)    
    print(is_palindrome(s1))
    
    print(s2)
    print(is_palindrome(s2))
    
    
    
if __name__ == "__main__":
    main()   
