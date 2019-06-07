import base64

file = "zhouyongxu.jpg"


def img_to_base64(filename):
    with open(filename, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        # print('data:image/jpeg;base64,%s' % s)
        f1name = filename+'.txt'
        f1 = open(f1name,'w')
        f1.write(s)
        f1.close()
    return s


# img_to_base64()
