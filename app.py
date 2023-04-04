# import random
# import string


# def function_one(length):
#     characters = string.ascii_letters + string.digits + string.punctuation

#     print(''.join(random.choice(characters) for _ in range(length)))


# function_one(20)

# it's give as a random of characters
# like : Wgy>[?wTgup}G`n:Q/IO

# ============= 2 ====================
# import os
# import re
# import datetime


# def function_two(directory):

#     date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
#     for filename in os.listdir(directory):
#         if os.path.isfile(os.path.join(directory, filename)):
#             match = date_pattern.search(filename)
#             if match:
#                 date_str = match.group()
#                 file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
#                 year = str(file_date.year)
#                 month = file_date.strftime('%B')
#                 new_directory = os.path.join(directory, year, month)
#                 os.makedirs(new_directory, exist_ok=True)
#                 old_path = os.path.join(directory, filename)
#                 new_path = os.path.join(new_directory, filename)
#                 os.rename(old_path, new_path)


# this function takes a argument directoryn to proved a path files in that directory pased  date.
# the function it takes the path and rename it based on there date pattren.

# =============ex 3==================

# import asyncio
# from datetime import datetime, timedelta
# from collections import defaultdict


# async def is_w(date):
#     return date.weekday() >= 5


# async def is_h(date):
#     holidays = [datetime(2023, 1, 1), datetime(2023, 4, 15), datetime(2023, 5, 1),
#                 datetime(2023, 6, 7), datetime(2023, 9, 16)]
#     return date in holidays


# async def generater(start_date, end_date):
#     dates = defaultdict(list)
#     current_date = start_date
#     while current_date <= end_date:
#         if not await is_w(current_date) and not await is_h(current_date):
#             dates[current_date.year].append(current_date)
#     current_date += timedelta(days=1)
#     return dates


# async def main():
#     start_date = datetime(2023, 1, 1)
#     end_date = datetime(2023, 12, 31)
#     dates = await generater(start_date, end_date)
#     year_counts = {year: len(dates[year]) for year in dates}
#     print('Number of workdays in 2023:', sum(year_counts.values()))
# if __name__ == '__main__':
#     asyncio.run(main())


# the function is_w chek if the day is weekend day and returns bool true.
# the function is_h also cheks if it is a holday and returns true or false.
# the generater function is used to a list of workingdays and cheks wether if it is a holyday of not.


# Part 2: Debugging your code


# import os
# import random
# from collections import Counter, defaultdict
# from datetime import datetime


# def create_file():
#     """Create a new file with a random filename and some random contents."""
#     filename = f'file_{datetime.now().strftime("%Y%m%d%H%M%S%f")}.txt'
#     with open(filename, 'w') as f:
#         for i in range(10):
#             f.write(f'Line {i}: {random.randint(1, 100)}\n')
#     return filename


# def read_file(filename):
#     """Read the contents of a file and return as a string."""
#     with open(filename, 'r') as f:
#         return f.read()


# def count_numbers(text):
#     lines = text.splitlines()
#     counts = defaultdict(int)
#     for line in lines:
#         words = line.split()
#         for word in words:
#             if word.isdigit():
#                 counts[int(word)] += 1
#     return Counter(counts)


# if __name__ == '__main__':
#     filename = create_file()
#     text = read_file(filename)
#     counts = count_numbers(text)
#     print(f'Counts for file {filename}: {counts}')
#     os.remove(filename)
#     print(f'Total count: {sum(counts)}')


# import webbrowser
# import re


# def search_google(query):
#     """Search for the given query on Google and open the first result in a web
#    browser."""
#     url = f'https://www.google.com/search?q={query}'
#     response = webbrowser.open(url)
#     if not response:
#         return 'Unable to open web browser'
#     html = webbrowser.get().open(url).read().decode('utf-8')
#     pattern = re.compile(r'<a href="(https://.*?)"')
#     match = pattern.search(html)
#     if not match:
#         return 'No search results found'
#     result_url = match.group(1)
#     response = webbrowser.open(result_url)
#     if not response:
#         return 'Unable to open web browser'
#     return 'Success'


# if __name__ == '__main__':
#     query = None
#     result = search_google(query)
#     print(result)
# the match.group(2) should be replaced with match.group(1)
