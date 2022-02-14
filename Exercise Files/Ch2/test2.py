#
# Example file for working with loops
#

def main():
  data = [10,2,2,1,1,1,1,1,1,2,2,2,2,4,4,4,4,4,4,4,4]  
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0): sum=sum+d
  return sum


if __name__ == "__main__":
  print(main())
  
