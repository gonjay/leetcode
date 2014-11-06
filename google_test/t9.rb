@t9 = {
  'a'=>'2', 'b'=>'22', 'c'=>'222',
  'd'=>'3', 'e'=>'33', 'f'=>'333',
  'g'=>'4', 'h'=>'44', 'i'=>'444',
  'j'=>'5', 'k'=>'55', 'l'=>'555',
  'm'=>'6', 'n'=>'66', 'o'=>'666',
  'p'=>'7', 'q'=>'77', 'r'=>'777', 's'=>'7777',
  't'=>'8', 'u'=>'88', 'v'=>'888',
  'w'=>'9', 'x'=>'99', 'y'=>'999', 'z'=>'9999',
  ' '=>'0'
}

s = " "

def getT9(str)
  result = ''
  index = 0

  while index < str.length do
    n = @t9[str[index]]
    if result == '' or result[-1,1] != n[-1,1]
      result += n
    else
      result += (' ' + n)
    end
    index += 1
  end
  result
end

# puts getT9(s)

fin = File.open("C-large-practice.in", "r")
index = fin.first.strip.to_i
fout = File.open("C-large-practice.out", "w")

i = 1
fin.each_line do | line|
  puts line
  fout.puts "Case ##{i}: " + getT9(line.sub!("\n", ''))
  i+=1
end
