arch = open("test_github_actions.txt", "w")

for i in range(10):
    arch.write(f"esta es la linea {i}\n")
arch.close()