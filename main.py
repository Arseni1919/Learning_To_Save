import numpy as np

def main():
    with open('test.npy', 'wb') as f:
        np.save(f, np.array([1, 2]))
        np.save(f, np.array([1, 3]))
    with open('test.npy', 'rb') as f:
        a = np.load(f)
        b = np.load(f)
    print(a, b)


if __name__ == '__main__':
    main()


