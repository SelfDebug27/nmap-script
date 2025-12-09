import subprocess 


print("\n" + "="*50)
print("     Starting NMAP scan...")
print("="*50)
print()


ip = input("IP address : ")

print("This scan is going to use -sC, -sS, -sV, -O, -Pn as arguments")
 
print("the scan output will be saved in output.txt\n")

comando = [

"nmap",
ip,
"-sC",
"-sS",
"-sV",
"-O",
"-Pn",
"-oN", "output.txt"
]

subprocess.run(comando)