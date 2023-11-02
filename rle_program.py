import console_gfx
from console_gfx import ConsoleGfx

#ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

#creates the menu
def menu_display():

    print("RLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String \n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data ")

#turns hexadecimal to string
def to_hex_string(data):
    hexstring = ''
    hexval = 0
    for value in data:
        hexval = hex(value)
        hexstring += hexval
    hexstring = hexstring.replace("0x", "")
    return hexstring





def count_runs(flat_data):
    #creates variable to count the amount of consecutive numbers
    consecutive = 0
    #creates variable to count the amount of runs
    runs = 1
    #for loop iterates through the whole list (-1 becasue I am addign 1 to i)
    for i in range(len(flat_data) - 1):
        #adds one to consecutive if two adjacent numbers are the same
        if flat_data[i] == flat_data [i + 1]:
            consecutive += 1
            #incriments runs if theres 15 or more consecutive and resets cons counter to 0
            if consecutive >= 15:
                runs += 1
                consecutive = 0
        #adds one to run counter and resets cons counter if adjacent numbers are different
        if flat_data[i] != flat_data[i + 1]:
            consecutive = 0
            runs += 1
    #returns runs
    return runs

def encode_rle(flat_data):
    #creates a counter for cons numbers
    consecutive = 1
    #creates a list that will be returned
    numlist = []
    #iterates through the list starting at second element (using - 1 in the code to check first element)
    for i in range(1, len(flat_data)):
        #when theres 15 cons numbers, add the 15 and the number to numlist, and reset the counter
        if flat_data[i] == flat_data [i-1]:
            consecutive += 1
            if consecutive == 15:
                numlist.append(consecutive)
                numlist.append(flat_data[i - 1])
                consecutive = 0
        #other cases add the current cons and number, and reset cons counter
        else:
            numlist.append(consecutive)
            numlist.append(flat_data[i - 1])
            consecutive = 1
    #add the last element of the list
    numlist.append(consecutive)
    numlist.append(flat_data[-1])
    #return the list
    return numlist

def get_decoded_length(flat_data):
    #creates varibale that will be returned
    length = 0
    #iterates through list, but only checks the odd indices and adds them to length
    for i in range(0, len(flat_data),2):
        length += flat_data[i]
    #returns length
    return length

def decode_rle(rle_data):
    #creates list that will be returned
    numlist = []
    #loops through the even indices of the array
    for i in range(0, len(rle_data) - 1, 2):
        #prints the encoded number i amount of times (i is the first number, j is the second number)
        for j in range(rle_data[i]):
            numlist.append(rle_data[i + 1])
    #returns the arrray
    return numlist


def string_to_data(data_string):
    #creates int list that iterates through hex list changing hex to ints
    intlist = [int(i, 16) for i in data_string]
    #returns this list
    return intlist


def to_rle_string(rle_data):
    #creates the string that it will return
    returnstring = ""
    #loops through the array
    for i in range (len(rle_data)):
        #if the index is even, it adds it to the string
        if i % 2 == 0:
            returnstring += str((rle_data[i]))
        #if the index is odd, it adds it to the string and adds a colon
        if i % 2 != 0:
            returnstring += hex(rle_data[i])
            returnstring += ":"
    #deletes the colon at the end of the list
    returnstring = returnstring[:-1]
    #takes out the 0x prefix that the hex command adds
    return returnstring.replace("0x", "")



def string_to_rle(rle_string):
    data = rle_string.split(":")
    newlist = []
    for element in data:
        current = int(element[0:-1])
        next = element[-1]
        next = int(next, 16)
        newlist.append(current)
        newlist.append(next)

    return newlist


#Begins the code
if __name__ == '__main__':
    #sets variable for while loop
    run = True
    #sets various variables for the program
    choice = 0
    image_name = 0
    image_data = ""
    #prints beginning messages
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)











    while run:
        #prints the menu and takes care of edge cases for wrong inputs
        menu_display()
        choice = int(input("Select a Menu Option:"))
        if choice < 0 or choice > 9:
            print("Error! Invalid input.")
        if choice == 0:
            run = False




        #takes the preset image and loads it to image data variable
        if choice == 1:
            image_name = (input("Enter name of file to load:"))
            image_data = ConsoleGfx.load_file(image_name)

        #takes the test image and loads it to image data
        if choice == 2 :
            image_data = console_gfx.ConsoleGfx.test_image
            print("Test image data loaded.")
        #takes in an RLE string, turns it into a shortened list, and decodes it to a full lengthed list
        if choice == 3:
            input_data = (input("Enter an RLE string to be decoded:"))
            image_data = decode_rle(string_to_rle(input_data))

        #Reads RLE data from the user in hexadecimal notation without delimeters
        if choice == 4:
            input_data = input("Enter the hex string holding RLE data:")
            image_data = decode_rle(string_to_data(input_data))

        #Reads data from the user and turns it into an array of ints
        if choice == 5:
            input_data = input("Enter the hex string holding flat data:")
            string_to_data(input_data)

        #Displays the image
        if choice == 6:
            print("Displaying image...")
            console_gfx.ConsoleGfx.display_image(image_data)

        #takes the current data and changes it into a RLE representation with delimeters
        if choice == 7:
           #checks if theres any image data
           if len(image_data) == 0:
               print("RLE representation: (no data)")
           else:
               image_data = to_rle_string(encode_rle(image_data))
               print(f"RLE representation:{image_data}")
        #Changes the data to RLE hex representation without delimeters
        if choice == 8:
            # checks if theres any image data
            if len(image_data) == 0:
                print("RLE hex values: (no data)")
            else:
                image_data = encode_rle(image_data)
                image_data = to_hex_string(image_data)


                print(f"RLE hex values:{image_data}")

        #displays current flat data in hex representation
        if choice == 9:
            # checks if theres any image data
            if len(image_data) == 0:
                print("Flat hex values: (no data)")
            else:
                image_data = to_hex_string(image_data)
                print(f"Flat hex values: {image_data}")
