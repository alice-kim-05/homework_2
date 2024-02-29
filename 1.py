silver=96
gold=silver/16
cost_silver=48
all_cost=float(input())
cost_gold=(all_cost-silver*cost_silver)/gold
print(int(cost_gold))