tasks_list = input("Enter your tasks for today separated by a comma: ").split(",")
done_tasks = []
ongoing_tasks = []
for task in tasks_list:
    print(f"\n{task}\n")
    done = input(f"Did you finish {task} alredy? \n").lower()
    if done == "yes":
        print("Nice job")
        done_tasks.append(task)
    else:
        print("Try not to put it off")
        ongoing_tasks.append(task)
    print("-----------")

see_progress = input("Do youwant to your today's progress?(yes, no)\n").lower()
if see_progress == "yes":
    print("                  ⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕ Done Tasks ⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕")
    print(done_tasks)
    print(" ")
    print("                  ⁕⁕⁕⁕⁕⁕⁕⁕⁕ Ongoing Tasks ⁕⁕⁕⁕⁕⁕⁕⁕⁕")
    print(ongoing_tasks)
else:
    input("Please hit Enter to exit")
