#Write the content
f = open("myfile.txt", 'w')
f.write("B \nA \nC")
f.close

#Read the content
f = open("myfile.txt", 'r')
lines = f.readlines()
f.close()

#Sort the content in the order of alphabet
lines.sort()

#Write the content after descending
f = open("myfile.txt", 'w')
f.writelines(lines)
f.close()