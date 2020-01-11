def recur(num):
    if num > 100:
        return num-10
    else:
        return recur(recur(num+11))

print(recur(98))

# const factorial = (n) => {
#   if(n<=1){
#     return 1
#   }
#   console.log(n, n-1)
#   return n*factorial(n-1)
# }

# console.log(factorial(5))

# const factorialLoop = (n) => {
#   let result = 1

#   for(let i = 2; i<=num;i++){
#     console.log(`result = ${result} * ${i} (${rusult*i})`)
#     result *=i
#   }
#   return result
# }