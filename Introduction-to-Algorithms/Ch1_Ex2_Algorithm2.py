spans = [1]
quotes = [5, 20, 50, 10, 100]
stack = [0]
day = 1
top = len(stack) - 1
while day < len(quotes):
    while len(stack) != 0 \
    and quotes[stack[top]] <= quotes[day]:
        stack.pop(top)
    if len(stack) == 0:
        spans.append(day + 1)
    else:
        spans.append(day - stack[top])
    stack.append(day)
    day += 1
print(spans)
