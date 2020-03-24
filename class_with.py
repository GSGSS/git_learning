class Testwith():
    def __enter__(self):
        print('fun')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('done')
        # print('type %s' % exc_type)
        # print('val  %s' % exc_val)
        if exc_tb is None:
            print('正常结束')
        else:
            print('myerror is  %s' %exc_tb)


with Testwith():
    print('run')
    raise NameError('testError')
