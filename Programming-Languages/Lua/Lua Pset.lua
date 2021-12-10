-- https://stackoverflow.com/a/27028488
function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

--[==[
DAY 1 -- EASY
--]==]

-- Write a function called ends_in_3(num) that returns
-- true if the final digit of num is 3, and false otherwise.
function ends_in_3(num)
  strnum = tostring(num)
  if tonumber(string.sub(strnum, #strnum, #strnum)) == 3 then
    return true
  else return false
  end
end

-- print(ends_in_3(1384573))

-- Now, write a similar function called is_prime(num) to test
-- if a number is prime (that is, it’s divisible only by itself and 1).
function is_prime(num)
  for i = 2, num - 1 do
    if num % i == 0 then return false end
  end
  return true
end

-- Create a program to print the first n prime numbers that end in 3.
function primes_ending_in_3(n)
  local primes = {}
  local num = 1
  while true do
    if is_prime(num) and ends_in_3(num) then
      table.insert(primes, num)
    end
    if #primes == n then
      print("The first " .. n .. " primes that end in 3 are:")
      for i=1, #primes do print(primes[i]) end
      break
    end
    num = num+1
  end
end

-- print("PRIMES")
-- primes_ending_in_3(10)



--[==[
DAY 2 -- EASY
--]==]

-- Write a function called concatenate(a1, a2) that takes two arrays and returns
-- a new array with all the elements of a1 followed by all the elements of a2.
function concatenate(array1, array2)
  while #array2 ~= 0 do
    local item = table.remove(array2, 1)
    table.insert(array1, item)
  end
  return array1
end

numlist = concatenate({1, 2, 3}, {4, 5, 6})
alphalist = concatenate({"a", "b", "c"}, {"d", "e", "f"})

function print_array(array)
  for i=1, #array do print(array[i]) end
end

-- print_array(numlist)
-- print_array(alphalist)


-- Our strict table implementation in Reading and Writing, on page 19 doesn’t
-- provide a way to delete items from the table. If we try the usual approach,
-- treasure.gold = nil, we get a duplicate key error. Modify strict_write() to allow
-- deleting keys (by setting their values to nil).
local _private = {}

function strict_read(table, key)
  if _private[key] then
    return _private[key]
  else
    error("Invalid key: " .. key)
  end
end

function strict_write(table, key, value)
  if _private[key] ~= nil and value ~= nil then
    error("Duplicate key: " .. key)
  else
    _private[key] = value
  end
end

local mt = {
  __index = strict_read,
  __newindex = strict_write
}

treasure = {}
setmetatable(treasure, mt)

treasure.gold = 50
treasure.gold = nil



--[==[
DAY 3 -- EASY
--]==]

-- Find the music for your favorite adventure movie’s theme song, and
-- translate it to Lua. Play it with the music player you wrote.

-- The way it stands, we have to put require 'notation' at the beginning of every
-- song and song.go() at the end. Modify play.cpp to do this for you so that songs
-- can just contain the tempo and parts.
