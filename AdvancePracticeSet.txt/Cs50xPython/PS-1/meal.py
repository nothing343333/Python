def main():
    # Prompt user for the time
    time_str = input("What time is it? ")
    # Convert the time to a float representing hours
    time_in_hours = convert(time_str)
    # Check what meal time it is and print the appropriate response
    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")

def convert(time):
    # Split the input time into hours and minutes
    hours, minutes = time.split(":")
    # Convert hours and minutes to floats and calculate the total hours
    total_hours = float(hours) + float(minutes) / 60
    return total_hours

if __name__ == "__main__":
    main()


