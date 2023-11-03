import subprocess


def pipeline_example():
    try:
        data = 'Hello! How are you?'
        echo_process = subprocess.Popen(['echo', data], stdout=subprocess.PIPE)
        grep_process = subprocess.Popen(['grep', 'Hello'], stdin=echo_process.stdout, stdout=subprocess.PIPE, text=True)
        echo_process.stdout.close()
        output = grep_process.communicate()[0].decode('utf-8')
        print(output)

    except Exception as e:
        print('error: ', e)


if __name__ == '__main__':
    pipeline_example()