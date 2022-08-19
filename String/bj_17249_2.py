TaeBo = input()

left, right = TaeBo.split("(")
print(left.count("@"), right.count("@"), end=" ")
