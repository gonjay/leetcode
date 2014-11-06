fin = File.open("B-large-practice.in", "r")
index = fin.first.strip.to_i
fout = File.open("B-large-practice.out", "w")

i = 1
fin.each_line do | line|
	fout.puts "Case ##{i}: " + line.strip.split(" ").reverse.join(" ")
	i+=1
end
