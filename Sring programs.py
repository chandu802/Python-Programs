# Write a program for reverse a string without using any built in method. Use only loop
str1="This is Python class"
new_str1=''
for i in range(-1,-len(str1)-1,-1):
    new_str1+=str1[i]
print(new_str1)

#Write a program for get below output without using any built in method. Use only loop
# o/p: "class Python is This"
str1="This is Python class"
res_str=''
out_str=''
str_cnt=1
for i in range(-1,-len(str1)-1,-1):
    if str1[i]==' ':
        if str_cnt==1:
            res_str+=out_str
            str_cnt+=1
            out_str=''

        else:
            res_str=res_str+' '+out_str
            out_str=''

    else:
        out_str=str1[i]+out_str
res_str=res_str+' '+out_str
print(res_str)


