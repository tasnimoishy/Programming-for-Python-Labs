def find_unavailable(resources):
    for r in resources:
        if r[3] == 0:
            print(r)

find_unavailable(resources)
