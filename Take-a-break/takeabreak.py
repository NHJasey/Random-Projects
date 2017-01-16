import time
import webbrowser

total_breaks = 3
break_count = 0

print("This break started on "+time.ctime())
while(break_count < total_breaks):
	time.sleep(7200)
	webbrowser.open("https://www.youtube.com/watch?v=oYQ18wBC0uw")
	break_count = break_count + 1
