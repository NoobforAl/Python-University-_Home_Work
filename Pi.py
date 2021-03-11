import random
def estimate_pi(n):
  num_point_cricle = 0
  num_point_total = 0
  for _ in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    dis = x**2 + y**2

    if dis<=1:
      num_point_cricle +=1
    num_point_total +=1

  return 4 * num_point_cricle/num_point_total

a = estimate_pi(100000)
print(a)

