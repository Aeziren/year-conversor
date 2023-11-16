months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

month = day = year = 0
while True:
    date = input("Date: ")

    if "/" in date:
        month, day, year = date.split("/")
        try:
            int(month)
        except ValueError:
            pass
        else:
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
    elif "," in date:
        month_name, day_string, year = date.split(" ")
        day = day_string[:-1]
        if month_name in months and 1 <= int(day) <= 31:
            month = months.index(month_name) + 1
            break

day = int(day)
month = int(month)
year = int(year)

print(f"{year}-{month:02}-{day:02}")
