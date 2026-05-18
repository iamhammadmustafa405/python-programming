# 93: write a function to convert USD into PKR./ Currency Converter
def converter(usd):
    pkr= usd*282
    print(f"The price of {usd}$ is {pkr} Rupees.")

usd= float(input("Enter Amount in USD: "))

converter(usd)