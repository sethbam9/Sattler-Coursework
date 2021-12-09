spans = []
quotes = [5, 20, 50, 10, 100]
day = 0
while day < len(quotes):
  k = 1
  span_end = False
  while span_end == False:
    if (day - k) < 0 or quotes[day - k] > quotes[day]:
      span_end = True
      day += 1
    else:
      k += 1
  spans.append(k)

print(spans)
