-- Ways to print:
  -- print(x)
  -- print x
  -- return x
  -- =x

-- Strings
  -- tab is \t
  -- concatenate is ..
  -- length is #

-- Expressions
  -- exp is ^
  -- mod is %

-- Boolean
  -- and, or, not
  -- ex. not ((true or false) and false)

-- FUNCTIONS
function triple(num)
  return 3 * num
end
-- without the name:
print(
(function(num) return 3 * num end)(2)
)

function call_twice(f)
  ff = function(num)
    return f(f(num))
  end
  return ff
end

times_nine = call_twice(triple)

-- Flexible arguments - extra perams are ignored
function print_characters(friend, ...) -- ... is ellipsis
  print('*Friend*')
  print(friend)

  print('*Foes*')
  foes = {...}
  print(foes[1])
end

print_characters('Marcus', 'Belloq')

-- Tail Calls
function reverse(s, t)
  if #s < 1 then return t end
  first = string.sub(s, 1, 1)
  rest = string.sub(s, 2, -1)
  return reverse(rest, first .. t)
end

large = string.rep('hello ', 5000)
print(reverse(large, ''))

-- Multiple Returns
function weapons()
  return 'bullwhip', 'revolver'
end

w1, w2 = weapons()
print(w1, "\t", w2)

-- Keyword Arguments
-- Passing in a table is as efficient as keywords in python
function popcorn_prices(table)
  print('A medium popcorn costs ' .. table.medium)
end

popcorn_prices{small=5.00,
               medium=7.00,
               jumbo=15.00}

-- CONTROL FLOW (if and for statements)
film = 'Skull'

if film == 'Raiders' then
  print('Good')
elseif film == 'Temple' then print('Great')
else print('Huh?')
end

for i = 1, 5 do
  print(i)
end

for i = 1, 10, 3 do print(i) end

while math.random(100) < 50 do
  print('Tails; flipping again')
end

-- VARIABLES - global by default
function hypotenuse(a, b)
  local a2 = a * a -- this will be callable if not local
  local b2 = b * b
  return math.sqrt(a2 + b2)
end

hypotenuse(5, 7)
