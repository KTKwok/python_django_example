org_l=[]
dedup_l=[]

val=int(input("Enter number of elements in the list: "))

for i in range(1,val+1):
    org_l.append(int(input(f"Please input number {i}: ")))

# Deduplicate list method 1
for i in org_l:
    if i not in dedup_l:
        dedup_l.append(i)

# Deduplicate list method 2
# dedup_l=list(set(org_l))

print(f"Original list with {len(org_l)} items: {org_l}, sorted {sorted(org_l)}")
print(f"Deduplicated list with {len(dedup_l)} items: {dedup_l}, sorted {sorted(dedup_l)}")
print(f"Max value is {max(dedup_l)}")
print(f"Min value is {min(dedup_l)}")