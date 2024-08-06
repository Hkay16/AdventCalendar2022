unless ARGV.length == 2
    puts "Incorrect number of command line arguments."
    puts "Usage: ruby MyScript.rb [input.txt] [part]"
    exit
end

input_file = ARGV[0]
part = ARGV[1].to_i

# Function to split string into two halves
def halves(str)
    mid = str.size / 2
    [str[0...mid], str[mid..-1]]
end

# Define priorities for each letter
priorities = {}
('a'..'z').each_with_index { |char, index| priorities[char] = index + 1 }
('A'..'Z').each_with_index { |char, index| priorities[char] = index + 27 }

# Initialize an array to store common letters' priorities
common_letters_priorities = []

# Read the file line by line
lines = File.readlines(input_file).map(&:chomp)

if part == 1
    # Part 1: Find common items in each rucksack's compartments
    lines.each do |line|
        first, second = halves(line)
        common_item = (first.chars & second.chars).first
        if common_item
            common_letters_priorities.push(priorities[common_item])
        end
    end
elsif part == 2
    # Part 2: Find common items among each group of three rucksacks
    lines.each_slice(3) do |group|
        if group.size == 3
            first, second, third = group
            common_item = (first.chars & second.chars & third.chars).first
            if common_item
                common_letters_priorities.push(priorities[common_item])
            end
        end
    end
else
    puts "Invalid part number. Please specify 1 or 2."
    exit
end

# Calculate the sum of the priorities
sum = common_letters_priorities.sum

# Output the result
puts sum