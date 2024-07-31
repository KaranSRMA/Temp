"""
Conver tempreature
"""


def main():
    # This should start and launch your app!
    def celcius():
    	try:
    		temp = float(input("Enter temperature in celcius : "))
    		temp_cel = (temp*9/5)+32
    		print(f"{temp}°C in Fahrenheit : {temp_cel}°F")
    	except ValueError as e:
    		print("Invalid input Enter, only number.", e)
    def fahrenheit():
    	try:
    		temp = float(input("Enter temperature in Fahrenheit : "))
    		temp_far = (temp-32)*5/9
    		print(f"{temp}°F in Celcius : {temp_far}°C")
    	except:
    		print("Invalid input Enter, only number.")
    while True:
    	print("\nOptions:")
    	print("Enter 1 to change celcius into Fahrenheit : ")
    	print("Enter 2 to change Fahrenheit to celcius : ")
    	print("Enter 3 to exit : ")
    	
    	try:
    		choice = int(input("Enter number here : "))
    		if choice == 1:
    			celcius()
    		elif choice == 2:
    			fahrenheit()
    		elif choice == 3:
    			print("Exiting program.")
    			break
    		else:
    			print("Invalid, input !")
    	except ValueError as e:
    			print(e)
