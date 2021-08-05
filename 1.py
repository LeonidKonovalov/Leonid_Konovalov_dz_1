duration=int(input('Time='))

seconds = duration % 60
minutes = duration % 3600 // 60
hours = duration % 86400 // 3600
days = duration // 86400

if days:
    print(f'{days} days ',end = '')
if hours:
    print(f'{hours} hours ',end = '')
if minutes:
    print(f'{minutes} minutes ',end = '')
if seconds:
    print(f'{seconds} seconds')