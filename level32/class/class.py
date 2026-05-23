def my_join(seperator, items):
    result = ""

    for i in range(len(items)):
        result += items[i]

        if i != len(items) - 1:
            
            result += seperator

        return result

