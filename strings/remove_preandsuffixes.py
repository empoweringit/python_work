
# Example to remove prefixes
nostarch_url = 'https://nostarch.com'
# Using removeprefix to remove 'https://' from the URL
clean_url = nostarch_url.removeprefix('https://')
print("URL after removing prefix:", clean_url)

# Example to remove suffixes
filename = 'document.txt'
# Using removesuffix to remove '.txt' from the filename
base_name = filename.removesuffix('.txt')
print("Filename after removing suffix:", base_name)