def towersOfHanoi(num,src,dest,temp):
    if num < 1:
        return 
    towersOfHanoi(num - 1, src, temp, dest)
    print(f"Move {num} disk from peg {src} to peg {dest}")
    towersOfHanoi(num - 1, temp, dest, src)

if __name__== '__main__':
    num = 4
    towersOfHanoi(num, 'A','C','B')
