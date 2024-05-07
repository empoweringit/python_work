# how to effectively remove prefixes from a string (view name_cases to see how to remove suffix)
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)