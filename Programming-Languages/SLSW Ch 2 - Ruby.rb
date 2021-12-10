
""""""""""""""""""""""""""""""""
""" # Day 1 Challenge, p. 18 """
""""""""""""""""""""""""""""""""
def day_one()
  # Print the string “Hello, world.”
  puts "Hello, world."

  # For the string “Hello, Ruby,” find the index of the word “Ruby.”
  puts "Hello, Ruby".index("Ruby")

  # Print your name ten times.
  n = 1
  while n < 10
    puts "Seth"
    n = n + 1
  end

  # Print the string “This is sentence number 1,”
  # where the number 1 changes from 1 to 10.
  n = 1
  while n < 10
    puts "This is s number #{n}"
    n = n + 1
  end

  # Run a Ruby program from a file.
  # In Shell: ruby 'C:\Users\sethb\downloads\ruby.txt'
  file = File.open('C:\Users\sethb\downloads\ruby.txt')

end

# Bonus problem
def guessing_game(random_int=rand(10))
  while TRUE
    guess = gets.to_i
    if guess > random_int
      puts "too high"
    elsif guess < random_int
      puts "too low"
    else
      puts "winner!"
      return
    end
  end
end


""""""""""""""""""""""""""""""""
""" # Day 2 Challenge, p. 31 """
""""""""""""""""""""""""""""""""

def day_two()
  # Print the contents of an array of sixteen numbers, four numbers at a
  # time, using just each.
  i = 0
  a = Array(0..15)
  a.each do |item|
    p a[i, 4]
    i = i + 4
  end

  # Now, do the same with each_slice in Enumerable.
  Array(0..15).each_slice(4) {|a| p a}

end

# Let the initializer accept a nested structure of hashes.
# Code borrowed from https://codereview.stackexchange.com/questions/23979/making-a-tree-with-hash-input
class Tree < Struct.new(:name, :children)
  def self.new_from_hash(hash)
    name, children_hash = hash.first
    children = children_hash.map { |k, v| Tree.new_from_hash({k => v}) }
    Tree.new(name, children)
  end

  def visit_all(&block)
    visit &block
    children.each {|c| c.visit_all &block}
  end

  def visit(&block)
    block.call self
  end
end

ruby_tree = Tree.new_from_hash({'grandpa': { 'dad': {'child 1': {},
  'child 2': {} }, 'uncle': {'child 3': {}, 'child 4': {} } } })
puts "visiting entire tree"
ruby_tree.visit_all {|node| puts node.name}

# Write a simple grep that will print the lines of a file having any occurrences
# of a phrase anywhere in that line.
def file_grep(*args)
  lines = File.readlines(args[0])
  line_num = 0
  lines.each do |line|
    p "Line #{line_num}: #{line}" if line.include? args[1]
    line_num = line_num + 1
  end
end


""""""""""""""""""""""""""""""""
""" # Day 3 Challenge, p. 31 """
""""""""""""""""""""""""""""""""

# Modify the CSV application to support an each method to return
# a CsvRow object. Use method_missing on that CsvRow to return the
# value for the column for a given heading.
_csv.rb
class CsvRow
	def initialize(row)
		@row = row
		@numhash = {'one'=>0, 'two'=>1, 'three'=>3, 'four'=>4, 'five'=>5, 'six'=>6}
	end

	def method_missing(m, *args, &block)
		num = @numhash[m.to_s]
		@row[num]
	end

end
module ActsAsCsv
  def self.included(base)
    base.extend ClassMethods
  end

  module ClassMethods
    def acts_as_csv
      include InstanceMethods
    end
  end

  module InstanceMethods
    def read
      @csv_contents = []
      filename = self.class.to_s.downcase + '.txt'
      file = File.new(filename)
      @headers = file.gets.chomp.split(', ')

      file.each do |row|
        @csv_contents << row.chomp.split(', ')
      end
    end

    attr_accessor :headers, :csv_contents
    def initialize
      read
    end

    # def method_missing method
    #   i = method.to_s
    #   if i.is_a? Integer
    #     row = self.headers.find_index(i)
    #   end
    # end
    def method_missing(m, *args, &block)
  		num = m.to_i
  		headers[num]
	  end
  end
end

class RubyCsv # no inheritance! You can mix it in
  include ActsAsCsv
  acts_as_csv
  def each(&block)
    @result.each(&block)
  end
end

csv = RubyCsv.new
csv.each {|row| puts row.one}
