import numpy as np


def main():
   res = np.random.rand(100,100)
   print(res)
   np.savetxt('test.out', res, delimiter=',')


if __name__ == '__main__':
   main()
