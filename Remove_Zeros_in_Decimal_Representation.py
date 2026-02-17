def remove_zeros(n):

    s = str(n)

    s = s.replace('0', '')

    return int(s)

print(remove_zeros(1020030))
print(remove_zeros(1))


