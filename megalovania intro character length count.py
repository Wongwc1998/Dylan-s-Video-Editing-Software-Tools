#This is the code used to generate the megalovania sound effects. It counts the amount of characters in a line and how much sound effects I should use
line="It's a beautiful lamp oil outside;Ropes are singing;Bombs are blooming;On days like this, heroes like you;Should come back when you're a little richer"
line=line.split(";")
print(line)
for i in line:
    print(len(i))
line="Should come back when you're a little richer"
line=line.split()
print(len(line))
