from exa_py import Exa

exa = Exa('c77f3895-694b-4cd9-94fa-1f2c1bbf9a7a')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()