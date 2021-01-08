from collections import deque


lookup = {'a':1, 'b':1, 'c':1, 'd':1, 'e': 1}

tracker = deque(lookup.keys(), 6)

def update_cache(key, lookup, tracker):

    def check_key(key, lookup):
        try: 
            lookup[key]
        except KeyError:
            return True
        else:
            return False

    is_new_key = check_key(key, lookup)
    print(f"new key? {is_new_key}")

    if is_new_key:
        if len(tracker) == 5:
            lrk = tracker.popleft()
            del lookup[lrk]
        lookup[key] = 1
    else:
        del lookup[key]
        lookup[key] = 1
        tracker.remove(key)
    tracker.append(key)
    print("b", lookup, '-', tracker)

update_cache('a', lookup, tracker)
import ipdb; ipdb.set_trace()






