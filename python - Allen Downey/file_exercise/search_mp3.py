import os


def search_mp3s(dirname, suffix):
    mp3list = []
    # mp3_dict = dict()

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path) and path.endswith(suffix):
            mp3list.append(path)
            # mp3_dict[name] = [path]
        elif os.path.isfile(path) and not path.endswith(suffix):
            continue
        else:
            mp3list.extend(search_mp3s(path, suffix))
            # mp3_dict[dirname].append(search_mp3s(path,suffix))

    return mp3list


print(search_mp3s("C:\\users\\nah\\music", '.mp3'))
